from fastapi import Depends
from sqlalchemy.orm import Session

from contracts.create_user_dto import CreateUserDto
from contracts.update_user_dto import UpdateUserDto
from contracts.user_dto import UserDto
from infrastructure.data_access import get_db
from infrastructure.repositories.users_model import UsersModel


class UsersRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        users = self.db.query(UsersModel).all()
        return [UserDto(id=u.id, username=u.username) for u in users]

    def get_by_id(self, user_id: int):
        user = self.db.query(UsersModel).get(user_id)
        if user is None:
            return None
        return UserDto(id=user.id, username=user.username)

    def create(self, create_user_dto: CreateUserDto):
        new_user = UsersModel(username=create_user_dto.username, password=create_user_dto.password)
        self.db.add(new_user)
        self.db.commit()
        return UserDto(id=new_user.id, username=new_user.username)

    def update(self, id: int, update_user_dto: UpdateUserDto):
        user = self.db.query(UsersModel).get(id)
        if user is None:
            return None
        if update_user_dto.username is not None:
            user.username = update_user_dto.username
        if update_user_dto.password is not None:
            user.password = update_user_dto.password
        self.db.commit()
        return UserDto(id=user.id, username=user.username)

    def delete(self, id: int):
        user = self.db.query(UsersModel).get(id)
        if user is None:
            return None
        self.db.delete(user)
        self.db.commit()
        return user


def get_users_repository(db: Session = Depends(get_db)):
    return UsersRepository(db)
