from fastapi import FastAPI, status, Response
import json
import requests
from converters import yarrrml_to_rml, rml_mapper
from utils import get_url_content
from pydantic import BaseModel, AnyUrl
from rdflib import Graph

app = FastAPI()


class Mapping(BaseModel):
    mapping_url: AnyUrl


class MappingAndData(BaseModel):
    mapping_url: AnyUrl
    data_url: AnyUrl


@app.post("/api/url/yarrrmltorml")
def test(yarrrml: Mapping, reposne: Response):
    mapping_content = get_url_content(yarrrml.mapping_url).content
    rml = yarrrml_to_rml(mapping_content)
    if (rml == None):
        reposne.status_code = 422
        return "Data not processed by yarrrml parser"
    return rml


@app.post("/api/url/tordf")
def test(mapping_and_data: MappingAndData, reposne: Response):
    mapping_content = get_url_content(mapping_and_data.mapping_url).content
    data_content = get_url_content(mapping_and_data.data_url).text

    rml = yarrrml_to_rml(mapping_content)
    if (rml == None):
        reposne.status_code = 422
        return "Data not processed by yarrrml parser"

    response = rml_mapper(rml ,data_content )
    json_response = json.loads(response)
    knowledge_graph = json_response["output"]
    g = Graph()
    g.parse(data=knowledge_graph , format="n3")
    knowledge_graph = g.serialize(format="turtle")
    print(knowledge_graph)
    return knowledge_graph
