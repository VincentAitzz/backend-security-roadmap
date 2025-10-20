from fastapi import APIRouter
from app.models.echo import EchoRequest

router = APIRouter()

@router.post("/echo")
async def echo(payload: EchoRequest):
    return {"recieved": payload.model_dump(), "note": "Esto es un hecho seguro"}