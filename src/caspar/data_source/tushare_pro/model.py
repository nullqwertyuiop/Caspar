from typing import Any

from pydantic import BaseModel

from caspar.data_source.model import Response, ResponseError


class TushareResponseData(BaseModel):
    fields: list[str]
    items: list[list[Any]]


class TushareResponse(Response):
    request_id: str
    code: int
    msg: str
    data: TushareResponseData


class TushareResponseError(ResponseError):
    code: int
    msg: str
    message: str
    data: None

    def __init__(self, code: int, msg: str, message: str, data: None):
        self.code = code
        self.msg = msg
        self.message = message
        self.data = data
        super().__init__(message)
