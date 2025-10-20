from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/time")
async def now():
    rNow = datetime.now().time()
    return {"time":f"La hora en chile es {rNow}"}