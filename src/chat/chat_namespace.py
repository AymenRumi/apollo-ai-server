import socketio

from src.decorator import pydantic
from src.schemas import Request
from src.services.rag import handle_request


class ChatNamespace(socketio.AsyncNamespace):
    async def on_connect(self, sid, environ):
        print(f"{sid} connected to chat")

    async def on_join_chat(self, sid, data):
        pass

    async def on_disconnect(self, sid):
        print(f"{sid} disconnected from chat")

    @pydantic(Request)
    async def on_chat_message(self, sid, request: Request):
        print(f"Message from {sid}: {request}")
        print(request.chat_id)
        response = handle_request(request.request)
        await self.emit("chat_reply", response, to=sid)
