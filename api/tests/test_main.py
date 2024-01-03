import os
import sys

from fastapi.testclient import TestClient

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)

from main import app

client = TestClient(app)


def test_yarrrml_parser():
    json_data = {
        "mapping_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_mapping.yaml",
    }

    response = client.post(
        "http://localhost:5004/api/url/yarrrmltorml", json=json_data
    )
    assert response.status_code == 200


def test_mapper():
    json_data = {
        "data_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_data.json",
        "mapping_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_mapping.yaml",
    }

    response = client.post(
        "http://localhost:5004/api/url/tordf", json=json_data
    )
    assert response.status_code == 200
