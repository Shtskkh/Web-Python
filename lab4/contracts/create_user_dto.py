from typing import Annotated

from pydantic import BaseModel, Field


class CreateUserDto(BaseModel):
    username: Annotated[str, Field(min_length=1, max_length=64)]
    password: Annotated[str, Field(min_length=6, max_length=64)]
