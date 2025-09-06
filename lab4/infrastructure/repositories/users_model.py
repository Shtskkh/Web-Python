from sqlalchemy import Column, String, Integer

from infrastructure.data_access import Base


class UsersModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
