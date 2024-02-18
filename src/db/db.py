from sqlalchemy import create_engine

from ..settings.db import SQLiteSettings

engine = create_engine(
    SQLiteSettings().database_url, connect_args={"check_same_thread": False}
)
