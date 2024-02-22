from fastapi import Depends
from sqlalchemy.orm import Session

from src.db import db_session
from src.db.models import Response
from src.interfaces import IRepository


class ResponseRepository(IRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, request_id: int):
        entry = Response(content="This is a bot response", request_id=request_id)
        self.session.add(entry)
        self.session.commit()
        return entry.id

    def get(self, _id):
        pass

    def get_all(self):
        pass

    def update():
        pass

    def delete():
        pass


def get_response_repository(db: Session = Depends(db_session)):
    return ResponseRepository(session=db)
