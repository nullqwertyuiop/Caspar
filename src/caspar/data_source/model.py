from abc import abstractmethod

from requests import Session
from pydantic import BaseModel


class DataSource:
    session: Session | None

    def __init__(self):
        self.session = None

    @abstractmethod
    def _run_query(self, *args, **kwargs):
        pass

    def _query(self, *args, **kwargs):
        if not self.session:
            self.session = Session()
        return self._run_query(*args, **kwargs)

    def __del__(self):
        if self.session:
            self.session.close()


class Response(BaseModel):
    pass


class ResponseError(Exception):
    pass
