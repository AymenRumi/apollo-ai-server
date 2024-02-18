from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.interfaces import IRepository
from src.repositories.conversation_repository import get_conversation_repository

db_api = APIRouter(tags=["SQLite"])


@db_api.post("/conversations")
def conversation(reposity: IRepository = Depends(get_conversation_repository)):
    reposity.add()
    return JSONResponse(content={"success": True}, status_code=200)
