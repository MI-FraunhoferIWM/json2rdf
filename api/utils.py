import os
from rdflib import Graph
from io import BytesIO
import requests
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


def get_url_content(url):
    response = requests.get(url)
    return response
