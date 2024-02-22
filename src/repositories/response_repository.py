from sqlalchemy.orm import Session

from src.interfaces import IRepository


class ChatRepository(IRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self):
        pass
