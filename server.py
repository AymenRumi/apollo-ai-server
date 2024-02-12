import uvicorn
from fastapi import FastAPI

from scripts import create_db
from src.routes.db import db_api

app = FastAPI()

app.include_router(db_api)

if __name__ == "__main__":

    create_db()

    uvicorn.run(app, host="127.0.0.1", port=8000)
