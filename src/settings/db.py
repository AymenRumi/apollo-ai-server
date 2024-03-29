from pydantic_settings import BaseSettings


class SQLiteSettings(BaseSettings):
    database_url: str = "sqlite:///./apollo.db"
