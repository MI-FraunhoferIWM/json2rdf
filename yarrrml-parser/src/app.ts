// @ts-ignore
// @ts-nocheck
import Yarrrml from "@rmlio/yarrrml-parser/lib/rml-generator";
import express from "express";
import bodyParser from "body-parser"


const namespaces = require('@rmlio/yarrrml-parser/lib/namespaces').asMap();
const N3 = require('n3');
const Logger = require('@rmlio/yarrrml-parser/lib/logger');

const app = express();
const port = 3001;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// take yarrrml as input and return triples
app.post('/', (req, res) => {
    console.log(req.body)
    console.log(req.body.yarrrml)
    const y2r = new Yarrrml();
    const yarrrml_query = req.body.yarrrml;
    if (yarrrml_query) {
        let triples
        triples = y2r.convert(yarrrml_query);

        let prefixes = {
            rr: namespaces.rr,
            rdf: namespaces.rdf,
            rdfs: namespaces.rdfs,
            fnml: namespaces.fnml,
            fno: namespaces.fno,
            d2rq: namespaces.d2rq,
            void: namespaces.void,
            dc: namespaces.dc,
            foaf: namespaces.foaf,
            rml: namespaces.rml,
            ql: namespaces.ql
        };


        prefixes.rml = namespaces.rml;
        prefixes.ql = namespaces.ql;
        prefixes[''] = y2r.getBaseIRI();
        prefixes = Object.assign({}, prefixes, y2r.getPrefixes());
        const writer = new N3.Writer({ prefixes });

        writer.addQuads(triples);


        writer.end(async (error, result) => {
            Logger.log(result);
            return res.send(result);

        });


        if (y2r.getLogger().has('error')) {
            return res.status(400).send(y2r.getLogger().getAll());
        }
        return res.send(triples.join('\r\n'));
    }
    return res.status(422).send();
})

app.listen(port, () => {
    return console.log(`server is listening on ${port}`);
});