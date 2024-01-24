# Json2Rdf

An application for generating RDF representation of data in JSON format.

## Installation

Clone the repository:
```
git clone https://github.com/MI-FraunhoferIWM/json2rdf.git
cd json2rdf
```

Optionally, edit the app port that in defined in the [`.env`](./.env) file under the variable name `JSON2RDF_PORT`.


### Production mode

Build and run the docker images:
```
    docker compose up --build
```

### Development mode

Build and run docker by running the following command:

```
    docker compose -f docker-compose.dev.yml up --build
```

## Usage

Go to `http://<your-ip-address>:{JSON2RDF_PORT}/docs`.

### API Usage examples

#### 1. Json2Rdf

```
curl -X 'POST' \
  'http://localhost:6001/api/url/tordf' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_data.json",
  "mapping_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_mapping.yaml"
}'
```

#### 2. YARRRML to RML 

```
curl -X 'POST' \
  'http://localhost:6001/api/url/yarrrmltorml' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "mapping_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_mapping.yaml"
}'
```



## Acknowledgement

This repository is adapted from https://github.com/Mat-O-Lab/RDFConverter .
