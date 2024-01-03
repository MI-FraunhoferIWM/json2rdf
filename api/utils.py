import json
import os

import requests
from rdflib import Graph


def get_url_content(url):
    response = requests.get(url)
    return response


def yarrrml_to_rml(mapping_data):
    print("1", flush=True)
    parser_url = os.environ.get(
        "parser_url", "http://localhost" + ":" + "3001"
    )

    response = requests.post(parser_url, data={"yarrrml": mapping_data})
    print("2", flush=True)

    return response.text, response.status_code


def rml_mapper(rml, data_content):
    payload = {"rml": rml, "sources": {"data.json": data_content}}

    mapper_url = os.environ.get(
        "mapper_url", "http://localhost" + ":" + "4000"
    )

    response = requests.post(mapper_url + "/execute", json=payload)
    response.raise_for_status()
    return response.text, response.status_code


def response_to_ttl(response):
    json_response = json.loads(response)
    knowledge_graph = json_response["output"]
    g = Graph()
    g.parse(data=knowledge_graph, format="nt")
    knowledge_graph = g.serialize(format="n3")
    print(knowledge_graph)

    return knowledge_graph
