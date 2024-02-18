from pydantic_settings import BaseSettings

from scripts.find_socket import available_port


class FastAPISettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = available_port()
