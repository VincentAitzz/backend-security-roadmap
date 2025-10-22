from fastapi import APIRouter
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from app.core.config import SERVICE_NAME, SERVER_TZ, EXPOSE_SERVER_TZ

router = APIRouter()

### ! DEPRECATED FUNCTION
### async def now():
###     rNow = datetime.now().time()
###     return {"time":f"La hora en chile es {rNow}"}

@router.get("/time")
async def get_time():
    # Tiempo en UTC
    now_utc = datetime.now(timezone.utc)
    iso_utc = now_utc.isoformat()
    epoch_ms = int(now_utc.timestamp() * 1000)
    
    payload = {
        "service":SERVICE_NAME,
        "server_time_utc":iso_utc,
        "server_time_epoch_ms":epoch_ms
    }
    
    if EXPOSE_SERVER_TZ and SERVER_TZ:
        try:
            local_tz = ZoneInfo(SERVER_TZ)
            now_local = now_utc.astimezone(local_tz)
            payload["server_time_local"] = now_local.isoformat()
            payload["server_tz"] = SERVER_TZ
        except Exception:
            pass
        
    return payload