from pydantic import Field
from pydantic_settings import BaseSettings


class OpenAISettings(BaseSettings):
    endpoint: str = Field(env="OPENAI_API_BASE")
    key: str = Field(env="OPENAI_API_KEY")
    version: str = Field(env="OPENAI_API_VERSION")
    deployment: str = Field(env="OPENAI_MODEL_DEPLOYMENT")
