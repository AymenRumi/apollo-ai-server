from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.db import create_db
from src.routes.db import db_api
from src.settings import FastAPISettings


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(db_api)

if __name__ == "__main__":
    uvicorn.run(app, host=FastAPISettings().host, port=FastAPISettings().port)
