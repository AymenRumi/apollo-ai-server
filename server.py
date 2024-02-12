from fastapi import FastAPI
from src.routes.db import db_api
import uvicorn

app = FastAPI()

app.include_router(db_api)

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)