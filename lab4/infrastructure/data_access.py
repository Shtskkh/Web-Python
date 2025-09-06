from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

connection_url = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password="l8z)t5C$S45?",
    host="localhost",
    port=5432,
    database="web_python")

engine = create_engine(connection_url)


class Base(DeclarativeBase):
    pass


session = Session(engine)


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()
