from datetime import datetime

from pydantic import BaseModel


class ReadStudent(BaseModel):
    id: int
    name: str
    gender: str


class CreateStudent(BaseModel):
    name: str
    gender: str
