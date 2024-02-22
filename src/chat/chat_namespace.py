import socketio


class ChatNamespace(socketio.AsyncNamespace):
    async def on_connect(self, sid, environ):
        print(f"{sid} connected to chat")

    async def on_join_chat(self, sid, data):
        pass

    async def on_disconnect(self, sid):
        print(f"{sid} disconnected from chat")

    async def on_chat_message(self, sid, data):
        print(f"Message from {sid}: {data}")
        await self.emit("chat_reply", data, to=sid)
