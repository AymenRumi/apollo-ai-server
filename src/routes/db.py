from fastapi import APIRouter
from fastapi.responses import JSONResponse

db_api = APIRouter(tags=["Db"])


@db_api.get("/")
def home():
    return JSONResponse(content={"success": True}, status_code=200)


