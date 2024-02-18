from fastapi import APIRouter
from fastapi.responses import JSONResponse

base_api = APIRouter(tags=["Base"])


@base_api.get("/")
def home():
    return JSONResponse(content={"success": True}, status_code=200)
