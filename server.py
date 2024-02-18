from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from scripts import available_port
from src.db import create_db
from src.routes.db import db_api


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(db_api)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=available_port())
