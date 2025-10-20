from fastapi import APIRouter
from app.core.config import SERVICE_NAME

router = APIRouter()

@router.get("/status")
async def status():
    return {"status":"ok",
            "message":"API levantada",
            "service":SERVICE_NAME}

@router.get("/greet")
async def greet(name: str = "Mundo"):
    return {"message":f"Hola, {name}. Bienvenido a {SERVICE_NAME}"}