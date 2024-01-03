# Json2RDF

An application for converting JSON files into RDF data.

## Installation

Clone the repository:
```
git clone https://github.com/MI-FraunhoferIWM/json2rdf.git
```

Optionally, edit the app port that in defined in the [`.env`](./.env) file under the variable name `JSON2RDF_PORT`.

Build and run the docker images:
```
    docker compose up --build
```

Go to `http://<your-ip-address>:{JSON2RDF_PORT}/docs`.
