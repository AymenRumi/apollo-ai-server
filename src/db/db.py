from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db.models.base import Base

from ..settings.db import SQLiteSettings

engine = create_engine(
    SQLiteSettings().database_url, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()


def create_db() -> None:
    Base.metadata.create_all(bind=engine)


def db_session():
    try:
        yield db
    finally:
        db.close()
