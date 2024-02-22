from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.interfaces import IRepository
from src.repositories import get_chat_repository, get_request_repository
from src.utils.logging import logger

# from src.schemas import Chat

db_api = APIRouter(tags=["SQLite"])


@db_api.post("/chats")
def add_chat(reposity: IRepository = Depends(get_chat_repository)):
    chat_id = reposity.add()
    return JSONResponse(content={"chat_id": chat_id, "success": True}, status_code=200)


@db_api.get("/chats/{id}")
def get_chat(id: int, repository: IRepository = Depends(get_chat_repository)):

    chat_instance = repository.get(id)
    if not chat_instance:
        raise HTTPException(status_code=404, detail="Chat not found")

    return JSONResponse(
        content={"chat": [i.query for i in chat_instance.requests], "success": True},
        status_code=200,
    )


# @db_api.delete("/chats/{chat}")
# def delete_chat(reposity: IRepository = Depends(get_response_repository)):
#     pass


@db_api.post("/request/{chat_id}")
def send_request(
    chat_id: int, query: str, reposity: IRepository = Depends(get_request_repository)
):
    response_id = reposity.add(chat_id, query)
    logger.debug(response_id)
    return JSONResponse(
        content={"response_id": response_id, "success": True}, status_code=200
    )
