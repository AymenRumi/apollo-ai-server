from fastapi import Depends
from sqlalchemy.orm import Session

from src.db import db_session
from src.db.models import Chat, Request
from src.interfaces import IRepository


class RequestRepository(IRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, chat_id: int, query: str):
        entry = Request(query=query, chat_id=chat_id)
        self.session.add(entry)
        self.session.commit()
        return entry.id

    def get(self, _id):
        pass

    def get_all(self):
        return Chat.query.all()

    def update():
        pass

    def delete():
        pass


def get_request_repository(db: Session = Depends(db_session)):
    return RequestRepository(session=db)
