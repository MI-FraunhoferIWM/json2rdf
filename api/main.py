from fastapi import FastAPI, Response, UploadFile
from utils import yarrrml_to_rml, rml_mapper, response_to_ttl ,get_url_content
from models.request_models import Mapping , MappingAndData , MappingAndDataStr
app = FastAPI(title="Json2rdf")

@app.post("/api/url/yarrrmltorml")
def yarrml_to_rml(yarrrml: Mapping, reposne: Response):
    mapping_content = get_url_content(yarrrml.mapping_url).content
    rml = yarrrml_to_rml(mapping_content)
    if (rml == None):
        reposne.status_code = 422
        return "Data not processed by yarrrml parser"
    return rml


@app.post("/api/url/tordf")
def to_rdf(mapping_and_data: MappingAndData, response: Response):
    mapping_content = get_url_content(mapping_and_data.mapping_url).content
    data_content = get_url_content(mapping_and_data.data_url).text

    rml = yarrrml_to_rml(mapping_content)
    if (rml == None):
        response.status_code = 422
        return "Data not processed by yarrrml parser"

    response = rml_mapper(rml, data_content)
    knowledge_graph = response_to_ttl(response)
    print(knowledge_graph)
    return knowledge_graph


@app.post("/api/file/yarrrmltorml")
async def yaml_to_rml(mapping_file: UploadFile, response: Response):
    mapping_content = await mapping_file.read()
    rml = yarrrml_to_rml(mapping_content)
    if (rml == None):
        response.status_code = 422
        return "Data not processed by yarrrml parser"
    return rml


@app.post("/api/file/tordf")
async def file_to_rdf(mapping_file: UploadFile, data_file: UploadFile, response: Response):
    mapping_content = await mapping_file.read()
    data_content = await data_file.read()
    data_content = data_content.decode()

    rml = yarrrml_to_rml(mapping_content)
    if (rml == None):
        response.status_code = 422
        return "Data not processed by yarrrml parser"

    response = rml_mapper(rml, data_content)
    knowledge_graph = response_to_ttl(response)
    print(knowledge_graph)
    return knowledge_graph


@app.post("/api/raw/tordf")
def test(mapping_and_data: MappingAndDataStr, response: Response):
    mapping_content = mapping_and_data.mapping_str
    data_content = mapping_and_data.data_str

    rml = yarrrml_to_rml(mapping_content)
    if (rml == None):
        response.status_code = 422
        return "Data not processed by yarrrml parser"

    response = rml_mapper(rml, data_content)
    knowledge_graph = response_to_ttl(response)
    return knowledge_graph
