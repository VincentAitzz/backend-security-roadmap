from fastapi import APIRouter, Header, HTTPException, Request
from app.core.config import API_KEY
from app.core.logging import logger
from datetime import datetime, timezone

router = APIRouter()

#   ! Deprecated method
#   async def secure_data(x_api_key: str | None = Header(default=None)):
#       if x_api_key != API_KEY:
#           raise HTTPException(status_code=401, detail="Invalid or missing API Key")

@router.get("/secure-data")
async def secure_data(request: Request, x_api_key: str | None = Header(default=None)):
    client_host = request.client.host
    timestamp = datetime.now(timezone.utc).isoformat()
    
    # ? Header Validation
    if x_api_key != API_KEY:
        logger.warning(
            {
                "event":"unauthorized_access_attempt",
                "path": str(request.url.path),
                "client_ip": client_host,
                "provided_key": x_api_key,
                "time_utc": timestamp,
                "status": 401
            }
        )
        raise HTTPException(status_code=401, detail="Invalid or Missing Api Key")
    
    # ? Autorized access log
    logger.info({
        "event": "authorized_access",
        "path": str(request.url.path),
        "client_ip": client_host,
        "time_utc": timestamp,
        "status": 200
    }) 
    return {"secret": "backend-ready", "owner":"VincentAitzz"}
    