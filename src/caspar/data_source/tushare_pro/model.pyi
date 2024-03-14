from pydantic import BaseModel
from typing import Any

class TushareResponseData(BaseModel):
    fields: list[str]
    items: list[list[Any]]

class TushareResponse(BaseModel):
    request_id: str
    code: int
    msg: str
    data: TushareResponseData

class TushareResponseError(Exception):
    code: int
    msg: str
    message: str
    data: None
    def __init__(self, code: int, msg: str, message: str, data: None) -> None: ...
