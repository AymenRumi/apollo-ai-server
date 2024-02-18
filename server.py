import uvicorn
from fastapi import FastAPI

from scripts import available_port
from src.db import create_db
from src.routes.db import db_api

app = FastAPI()


@app.on_event("startup")
async def app_startup():
    create_db()


app.include_router(db_api)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=available_port())
