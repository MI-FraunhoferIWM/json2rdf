from fastapi import FastAPI
import json
import requests
from utils import read_input, write_output

app = FastAPI()


def to_rml(mapping_data):
    response = requests.post(
        "http://localhost" + ":" + "3001", data={"yarrrml": mapping_data}
    )

    if (response.status_code == 200):
        response_text = response.text
    else:
        print("Data is not processed")
        exit()

    write_output('output1.rml', response_text)
    return response_text


def rml_mapper(payload):
    url = "http://localhost:4000/execute"

    response = requests.post("http://localhost" + ":" +
                             '4000' + "/execute", json=payload).text
    return response


@app.get("/api/yarrrmltorml")
def yarrml_to_rml():
    yaarrml_file_data = read_input("mapping.yaml")
    rml = to_rml(yaarrml_file_data)
    data = read_input("data.json")
    payload = {
        "rml": rml,
        "sources": {
            "data.json": data
        }
    }

    resposne = rml_mapper(payload)
    return resposne


@app.get("/api/tordf")
def tordf():
    yaarrml_file_data = read_input("mapping.yaml")
    rml = to_rml(yaarrml_file_data)
    data = read_input("data.json")
    payload = {
        "rml": rml,
        "sources": {
            "data.json": data
        }
    }

    resposne = rml_mapper(payload)
    return resposne
