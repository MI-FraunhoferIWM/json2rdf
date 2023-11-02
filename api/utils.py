import os
from rdflib import Graph
from io import BytesIO
from requests import request
from urllib.parse import quote


def read_input(file_name):
    path = os.path.join("input", file_name)
    file = open(path, 'r')
    data = file.read()
    return data


def write_output(file_name, data):
    path = os.path.join(os.getcwd(), "output", file_name)
    file = open(path, 'w')
    data = file.write(data)


def to_rml(data):
    url = "http://localhost:3001"
    payload = "yarrrml=" + data
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = request("POST", url, headers=headers, data=payload)
    if (response.status_code == 200):
        response_text = response.text
    else:
        print("Data is not processed")
        exit()

    write_output('output.rml', response_text)

    # g = Graph()
    # a = BytesIO(response_text.encode())
    # g.parse(a , format='ttl')
    # rml = g.serialize(format="ttl")

    return response_text


def rml_mapper(payload):
    url = "http://localhost:4000/execute"

    response = request("POST", url=url, json=payload)
    return response
