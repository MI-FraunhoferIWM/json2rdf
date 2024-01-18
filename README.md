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

Go to `http://<your-ip-address>:{JSON2RDF_PORT}/docs`.

### Development mode

Build and run docker by running the following command:

```
    docker compose -f docker-compose.dev.yml up --build
```

## Contributions
https://github.com/Mat-O-Lab/RDFConverter
