from typing import List, Union

from pydantic_settings import BaseSettings


class Request(BaseSettings):
    request: str
    chat_id: int


class Response(BaseSettings):
    response: str


class Messages:
    messages: List[Union[Request, Response]]


# class Chat(BaseSettings):
#     id : int
#     messages: List[Messages]
