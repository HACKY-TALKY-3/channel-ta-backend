from pydantic import BaseModel


class Context(BaseModel):
    channel: dict
    caller: dict



class Method(BaseModel):
    method: str
    params: dict
    context: Context

