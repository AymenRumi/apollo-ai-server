from contextlib import asynccontextmanager

import socketio
import uvicorn
from fastapi import FastAPI

from src.chat import ChatNamespace
from src.db import create_db
from src.routes.chat_route import db_api
from src.settings import FastAPISettings


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(lifespan=lifespan)

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")

socket_app = socketio.ASGIApp(socketio_server=sio, other_asgi_app=app)

sio.register_namespace(ChatNamespace("/chat"))

app.include_router(db_api)


if __name__ == "__main__":
    uvicorn.run(
        "server:socket_app",
        host=FastAPISettings().host,
        port=FastAPISettings().port,
        reload=True,
    )
