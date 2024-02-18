from fastapi import Depends
from sqlalchemy.orm import Session

from src.db import db_session
from src.db.models import Conversation
from src.interfaces import IRepository


class ConversationRepository(IRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self):
        entry = Conversation()
        self.session.add(entry)
        self.session.commit()
        return entry.id

    def get(self, id):
        return Conversation.query.filter_by(id=id).first()

    def get_all(self):
        return Conversation.query.all()

    def update():
        pass

    def delete():
        pass


def get_conversation_repository(db: Session = Depends(db_session)):
    return ConversationRepository(session=db)
