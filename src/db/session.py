from sqlalchemy import sessionMaker

from src.db.db import engine


def creat_session():
    Session = sessionMaker(bind=engine)
    return Session()
