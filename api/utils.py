import requests
from rdflib import Graph
import json


def get_url_content(url):
    response = requests.get(url)
    return response


def yarrrml_to_rml(mapping_data):
    response = requests.post(
        "http://localhost" + ":" + "3001", data={"yarrrml": mapping_data}
    )

    print(response.text)

    if (response.status_code == 200):
        response = response
    else:
        print("Data not processed")
        return

    return response.text


def rml_mapper(rml, data_content):

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
    print(knowledge_graph)
    g = Graph()
    g.parse(data=knowledge_graph, format="nt")
    knowledge_graph = g.serialize(format="n3")
    return knowledge_graph
