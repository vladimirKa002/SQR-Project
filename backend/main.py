from fastapi import FastAPI

from config import DEFAULT_SETTINGS
from db import setup_db
from auth import auth_router
from service import service_router

app = FastAPI()
app.include_router(service_router)
app.include_router(auth_router)


@app.on_event("startup")
def setup():
    setup_db(DEFAULT_SETTINGS.database_uri)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
