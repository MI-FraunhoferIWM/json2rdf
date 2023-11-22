
from pydantic import BaseModel, AnyUrl

class Mapping(BaseModel):
    mapping_url: AnyUrl


class MappingAndData(BaseModel):
    mapping_url: AnyUrl
    data_url: AnyUrl


class MappingAndDataStr(BaseModel):
    mapping_str: str
    data_str: str
