from fastapi import FastAPI
import json
from utils import read_input, to_rml, rml_mapper

app = FastAPI()


@app.get("/")
def read_root():
    yaarrml_file = read_input("mapping.yaml")
    rml = to_rml(yaarrml_file)
    data = read_input("data.json")
    payload = {
        "rml": rml,
        "sources": {
            "data.json": data
        }
    }

    resposne = rml_mapper(payload)
    print(resposne.text)
    return {"hello"}

@app.post("/to_yarrml")
