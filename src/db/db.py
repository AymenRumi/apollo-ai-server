from models.base import Base
from sqlalchemy import create_engine

from ..settings.db import SQLiteSettings

engine = create_engine(
    SQLiteSettings().database_url, connect_args={"check_same_thread": False}
)


def create_db() -> None:
    Base.metadata.create_all(bind=engine)
