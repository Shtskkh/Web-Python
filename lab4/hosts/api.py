from typing import List, Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import Field
from starlette.responses import JSONResponse

from contracts.create_user_dto import CreateUserDto
from contracts.message_dto import MessageDto
from contracts.update_user_dto import UpdateUserDto
from contracts.user_dto import UserDto
from infrastructure.repositories.users_repository import UsersRepository, get_users_repository

router = APIRouter(prefix="/api/v1/users")


@router.get("/", response_model=List[UserDto], responses={404: {"model": MessageDto}})
def get_users(repo: UsersRepository = Depends(get_users_repository)):
    users = repo.get_all()
    if len(users) == 0:
        return JSONResponse(status_code=404, content={"message": "No users found"})
    return users


@router.get("/{id}", response_model=UserDto, responses={404: {"model": MessageDto}})
def get_user(id: Annotated[int, Field(ge=1)], repo: UsersRepository = Depends(get_users_repository)):
    user = repo.get_by_id(id)
    if user is not None:
        return user
    return JSONResponse(status_code=404, content={"message": f"User with id: {id} not found"})


@router.post("/", response_model=UserDto)
def create_user(new_user: CreateUserDto, repo: UsersRepository = Depends(get_users_repository)):
    result = repo.create(new_user)
    return result


@router.put("/{id}", response_model=UserDto, responses={404: {"model": MessageDto}})
def update_user(id: Annotated[int, Field(ge=1)], update_user: UpdateUserDto,
                repo: UsersRepository = Depends(get_users_repository)):
    user = repo.update(id, update_user)
    if user is not None:
        return user
    return JSONResponse(status_code=404, content={"message": f"User with id: {id} not found"})


@router.delete("/{id}", response_model=bool, responses={404: {"model": MessageDto}})
def delete_user(id: Annotated[int, Field(ge=1)], repo: UsersRepository = Depends(get_users_repository)):
    user = repo.delete(id)
    if user is not None:
        return True
    return JSONResponse(status_code=404, content={"message": f"User with id: {id} not found"})
