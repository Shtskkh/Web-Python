from fastapi import FastAPI

from hosts.api import router
from infrastructure.data_access import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
