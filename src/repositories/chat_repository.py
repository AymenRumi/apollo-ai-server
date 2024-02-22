from fastapi import Depends
from sqlalchemy.orm import Session

from src.db import db_session
from src.db.models import Chat
from src.interfaces import IRepository


class ChatRepository(IRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self):
        entry = Chat()
        self.session.add(entry)
        self.session.commit()
        return entry.id

    def get(self, _id):
        try:
            return self.session.query(Chat).filter_by(id=_id).first()
        except:
            return None

    def get_all(self):
        return [chat.get_details() for chat in Chat.query.all()]

    def update():
        pass

    def delete():
        pass


def get_chat_repository(db: Session = Depends(db_session)):
    return ChatRepository(session=db)
