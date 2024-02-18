from sqlalchemy.orm import sessionmaker

from src.db.db import engine


def db_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
