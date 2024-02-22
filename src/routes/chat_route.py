from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.interfaces import IRepository
from src.repositories import (
    get_chat_repository,
    get_request_repository,
    get_response_repository,
)
from src.utils.logging import logger

# from src.schemas import Chat

db_api = APIRouter(tags=["SQLite"])


@db_api.post("/chats")
def add_chat(reposity: IRepository = Depends(get_chat_repository)):
    chat_id = reposity.add()
    return JSONResponse(content={"chat_id": chat_id, "success": True}, status_code=200)


@db_api.get("/chats")
def get_chats(reposity: IRepository = Depends(get_chat_repository)):

    return JSONResponse(content=reposity.get_all(), status_code=200)


@db_api.get("/chats/{id}")
def get_chat(id: int, repository: IRepository = Depends(get_chat_repository)):

    chat_instance = repository.get(id)
    if not chat_instance:
        raise HTTPException(status_code=404, detail="Chat not found")

    logger.debug(chat_instance.get_messages())
    return JSONResponse(
        content={"chat": chat_instance.get_messages(), "success": True},
        status_code=200,
    )


# @db_api.delete("/chats/{chat}")
# def delete_chat(reposity: IRepository = Depends(get_response_repository)):
#     pass


@db_api.post("/request/{chat_id}")
def send_request(
    chat_id: int, query: str, reposity: IRepository = Depends(get_request_repository)
):
    request_id = reposity.add(chat_id, query)
    logger.debug(request_id)
    return JSONResponse(
        content={"request_id": request_id, "success": True}, status_code=200
    )


@db_api.post("/response/{request_id}")
def get_response(
    request_id: int, reposity: IRepository = Depends(get_response_repository)
):
    response_id = reposity.add(request_id)
    logger.debug(response_id)
    return JSONResponse(
        content={"response_id": response_id, "success": True}, status_code=200
    )
