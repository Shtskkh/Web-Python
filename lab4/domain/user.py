from pydantic.v1 import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str
