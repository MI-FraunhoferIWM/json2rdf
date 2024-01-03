from pydantic import AnyUrl, BaseModel


class Mapping(BaseModel):
    mapping_url: AnyUrl
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "mapping_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_mapping.yaml"
                }
            ]
        }
    }


class MappingAndData(BaseModel):
    mapping_url: AnyUrl
    data_url: AnyUrl
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "mapping_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_mapping.yaml",
                    "data_url": "https://raw.githubusercontent.com/MI-FraunhoferIWM/json2rdf_data/main/1_data.json",
                }
            ]
        }
    }


class MappingAndDataStr(BaseModel):
    mapping_str: str
    data_str: str
