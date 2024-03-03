from pydantic_settings import BaseSettings


class FastAPISettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 5000
    # port: int = available_port()
