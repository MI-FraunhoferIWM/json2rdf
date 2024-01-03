from fastapi import FastAPI, Response, UploadFile
from models.request_models import Mapping, MappingAndData, MappingAndDataStr
from utils import get_url_content, response_to_ttl, rml_mapper, yarrrml_to_rml

app = FastAPI(title="Json2rdf")


@app.post("/api/url/yarrrmltorml")
def yarrml_to_rml(yarrrml: Mapping, response: Response):
    print("yarrml_to_rml", flush=True)
    mapping_content = get_url_content(yarrrml.mapping_url).content
    rml, response_code = yarrrml_to_rml(mapping_content)
    response.status_code = response_code
    if response_code == 200:
        return Response(content=rml, media_type="application/xml")
    return {"error": "Data not processed by Yarrrml parser"}


@app.post("/api/url/tordf")
def to_rdf(mapping_and_data: MappingAndData, response: Response):
    print("to_rdf", flush=True)
    mapping_content = get_url_content(mapping_and_data.mapping_url).content
    data_content = get_url_content(mapping_and_data.data_url).text
    print("data_content", data_content, flush=True)
    rml, response_code = yarrrml_to_rml(mapping_content)
    response.status_code = response_code
    if response_code != 200:
        return {"error": "Data not processed by Yarrrml parser"}

    mapped_rdf, response_code = rml_mapper(rml, data_content)
    response.status_code = response_code

    if response_code != 200:
        return {"error": "Data not processed by mapper"}

    knowledge_graph = response_to_ttl(mapped_rdf)
    return Response(content=knowledge_graph, media_type="application/rdf+xml")


@app.post("/api/file/yarrrmltorml")
async def yaml_to_rml(mapping_file: UploadFile, response: Response):
    mapping_content = await mapping_file.read()
    rml, response_code = yarrrml_to_rml(mapping_content)
    response.status_code = response_code
    if response_code == 200:
        return Response(content=rml, media_type="application/xml")
    return {"error": "Data not processed by Yarrrml parser"}


@app.post("/api/file/tordf")
async def file_to_rdf(
    mapping_file: UploadFile, data_file: UploadFile, response: Response
):
    mapping_content = await mapping_file.read()
    data_content = await data_file.read()
    data_content = data_content.decode()

    rml, response_code = yarrrml_to_rml(mapping_content)
    print("RML", rml, flush=True)
    response.status_code = response_code
    if response_code != 200:
        return {"error": "Data not processed by Yarrrml parser"}

    print("data_content", data_content, flush=True)
    mapped_rdf, response_code = rml_mapper(rml, data_content)
    response.status_code = response_code

    if response_code != 200:
        return {"error": "Data not processed by mapper"}

    knowledge_graph = response_to_ttl(mapped_rdf)
    return Response(content=knowledge_graph, media_type="application/rdf+xml")


@app.post("/api/raw/tordf")
def test(mapping_and_data: MappingAndDataStr, response: Response):
    mapping_content = mapping_and_data.mapping_str
    data_content = mapping_and_data.data_str

    rml, response_code = yarrrml_to_rml(mapping_content)
    response.status_code = response_code
    if response_code != 200:
        return {"error": "Data not processed by Yarrrml parser"}

    mapped_rdf, response_code = rml_mapper(rml, data_content)
    response.status_code = response_code

    if response_code != 200:
        return {"error": "Data not processed by mapper"}

    knowledge_graph = response_to_ttl(mapped_rdf)
    return Response(content=knowledge_graph, media_type="application/rdf+xml")
