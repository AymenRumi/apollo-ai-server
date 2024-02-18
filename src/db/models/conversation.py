from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime, default=datetime.utcnow())
    summary = Column(String, default="")
    messages = relationship("Message", back_populates="conversation")


class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    time = Column(DateTime, default=datetime.utcnow)
    content = Column(Text)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))

    conversation = relationship("Conversation", back_populates="requests")
    response = relationship("Response", back_populates="request", uselist=False)


class Response(Base):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True)
    user = Column(String)
    time = Column(DateTime, default=datetime.utcnow)
    content = Column(Text)
    request_id = Column(Integer, ForeignKey("requests.id"), unique=True)

    request = relationship("Request", back_populates="response")
