from fastapi import FastAPI

from hosts.api import router

app = FastAPI()

app.include_router(router)
