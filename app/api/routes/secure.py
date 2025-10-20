from fastapi import APIRouter, Header, HTTPException
from app.core.config import API_KEY

router = APIRouter()
@router.get("/secure-data")
async def secure_data(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return {"secret": "backend-ready", "owner":"VincentAitzz"}