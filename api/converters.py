import requests
from utils import write_output
from rdflib import Graph
import json


def yarrrml_to_rml(mapping_data):
    response = requests.post(
        "http://localhost" + ":" + "3001", data={"yarrrml": mapping_data}
    )
    if (response.status_code == 200):
        response = response
    else:
        print("Data not processed")
        return

    write_output('output1.rml', response.text)
    return response.text


def rml_mapper(rml ,data_content):
    
    payload = {
        "rml": rml,
        "sources": {
            "data.json": data_content
        }
    } 
    url = "http://localhost:4000/execute"

    response = requests.post(url, json=payload)
    return response.text

def response_to_ttl(response):
    json_response = json.loads(response)
    knowledge_graph = json_response["output"]
    g = Graph()
    g.parse(data=knowledge_graph , format="n3")
    knowledge_graph = g.serialize(format="turtle")
    return knowledge_graph
