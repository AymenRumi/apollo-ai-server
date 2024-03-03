from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings


class Base(BaseSettings):
    class Config:
        env_file = find_dotenv()
        load_dotenv(env_file)


class OpenAISettings(BaseSettings):
    endpoint: str
    key: str
    version: str
    model_deployment: str

    class Config:
        env_prefix = "OPENAI_API_"
