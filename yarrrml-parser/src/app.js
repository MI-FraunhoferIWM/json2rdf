"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// @ts-ignore
const rml_generator_1 = __importDefault(require("@rmlio/yarrrml-parser/lib/rml-generator"));
const express_1 = __importDefault(require("express"));
const body_parser_1 = __importDefault(require("body-parser"));
const namespaces = require('@rmlio/yarrrml-parser/lib/namespaces').asMap();
const N3 = require('n3');
const Logger = require('@rmlio/yarrrml-parser/lib/logger');
const app = (0, express_1.default)();
const port = 3001;
app.use(body_parser_1.default.urlencoded({ extended: false }));
app.use(body_parser_1.default.json());
// take yarrrml as input and return triples
app.post('/', (req, res) => {
    console.log(req.body);
    console.log(req.body.yarrrml);
    const y2r = new rml_generator_1.default();
    const yarrrml_query = req.body.yarrrml;
    if (yarrrml_query) {
        let triples;
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
        writer.end((error, result) => __awaiter(void 0, void 0, void 0, function* () {
            Logger.log(result);
        }));
        if (y2r.getLogger().has('error')) {
            return res.status(400).send(y2r.getLogger().getAll());
        }
        return res.send(triples.join('\r\n'));
    }
    return res.status(422).send();
});
app.listen(port, () => {
    return console.log(`server is listening on ${port}`);
});
