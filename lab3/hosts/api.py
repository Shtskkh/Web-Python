from typing import List, Annotated

from fastapi import APIRouter
from pydantic import Field
from starlette.responses import JSONResponse

from contracts.create_user_dto import CreateUserDto
from contracts.message_dto import MessageDto
from contracts.update_user_dto import UpdateUserDto
from contracts.user_dto import UserDto
from domain.user import User

users = []

router = APIRouter(prefix="/api/v1/users")


@router.get("/", response_model=List[UserDto], responses={404: {"model": MessageDto}})
def get_users():
    if len(users) == 0:
        return JSONResponse(status_code=404, content={"message": "No users found"})
    return users


@router.get("/{id}", response_model=UserDto, responses={404: {"model": MessageDto}})
def get_user(id: Annotated[int, Field(ge=1)]):
    for user in users:
        if user.id == id:
            return user
    return JSONResponse(status_code=404, content={"message": f"User with id: {id} not found"})


@router.post("/", response_model=UserDto)
def create_user(new_user: CreateUserDto):
    user = User(id=len(users) + 1, username=new_user.username, password=new_user.password)
    users.append(user)
    return user


@router.put("/{id}", response_model=UserDto, responses={404: {"model": MessageDto}})
def update_user(id: Annotated[int, Field(ge=1)], update_user: UpdateUserDto):
    for user in users:
        if user.id == id:
            if update_user.username is not None:
                user.username = update_user.username
            if update_user.password is not None:
                user.password = update_user.password
            return user
    return JSONResponse(status_code=404, content={"message": f"User with id: {id} not found"})


@router.delete("/{id}", response_model=bool, responses={404: {"model": MessageDto}})
def delete_user(id: Annotated[int, Field(ge=1)]):
    for user in users:
        if user.id == id:
            users.remove(user)
            return True
    return JSONResponse(status_code=404, content={"message": f"User with id: {id} not found"})
