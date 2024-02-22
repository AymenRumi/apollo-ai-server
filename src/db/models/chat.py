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


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime, default=datetime.utcnow())
    summary = Column(String, default="New Chat")
    requests = relationship("Request", back_populates="chat")


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    time = Column(DateTime, default=datetime.utcnow())
    content = Column(Text)
    request_id = Column(Integer, ForeignKey("requests.id"), unique=True)

    request = relationship("Request", back_populates="response", uselist=False)
