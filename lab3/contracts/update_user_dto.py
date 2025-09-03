from typing import Annotated, Union

from pydantic import BaseModel, Field


class UpdateUserDto(BaseModel):
    username: Annotated[Union[str, None], Field(min_length=1, max_length=64)] = None
    password: Annotated[Union[str, None], Field(min_length=6, max_length=64)] = None
