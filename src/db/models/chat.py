from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, default=datetime.utcnow())
    query = Column(Text)
    chat_id = Column(Integer, ForeignKey("chats.id"))

    chat = relationship("Chat", back_populates="requests")
    response = relationship("Response", back_populates="request", uselist=False)

    def get_request_response(self):
        return {
            "request": {
                "query": self.query,
                "time": self.time.isoformat(),
                "id": self.id,
            },
            "response": {
                "content": self.response.content,
                "time": self.response.time.isoformat(),
                "id": self.response.request_id,
            }
            if self.response
            else None,
            "response_time": (self.response.time - self.time).total_seconds()
            if self.response
            else None,
        }


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime, default=datetime.utcnow())
    summary = Column(String, default="New Chat")
    requests = relationship("Request", back_populates="chat")

    def get_details(self):
        return {self.id, self.summary, self.time_created.isoformat()}

    def get_messages(self):
        return [message.get_request_response() for message in self.requests]


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    time = Column(DateTime, default=datetime.utcnow())
    content = Column(Text)
    request_id = Column(Integer, ForeignKey("requests.id"), unique=True)

    request = relationship("Request", back_populates="response", uselist=False)
