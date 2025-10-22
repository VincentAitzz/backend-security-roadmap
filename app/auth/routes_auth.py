from fastapi import APIRouter, HTTPException, Header, Depends
from pydantic import BaseModel, Field
from app.auth.hashing import hash_password, verify_password
from app.auth.jwt_handler import create_token, verify_token
from typing import Optional

router = APIRouter()

USERS_DB = {}

class RegisterRequest(BaseModel):
    username: str = Field(...,min_length=3,max_length=30)
    password: str = Field(...,min_length=6)
    
class LoginRequest(BaseModel):
    username: str
    password: str
    
@router.post("/register")
async def register(payload: RegisterRequest):
    if payload.username in USERS_DB:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    hashed_pw = hash_password(payload.password)
    USERS_DB[payload.username] = hashed_pw
    return {"message":f"Uuario {payload.username} registrado correctamente"}
@router.post("/login")
async def login(payload: LoginRequest):
    stored_hash = USERS_DB.get(payload.username)
    
    if not stored_hash or not verify_password(payload.password, stored_hash):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    token = create_token({"sub":payload.username})
    return {"access_token":token, "token_type":"bearer"}

@router.get("/protected")
async def protected_route(autorization: Optional[str] = Header(None)):
    if not autorization:
        raise HTTPException(status_code=401,detail="Falta token")
    token = autorization.replace("Bearer ","")
    decoded = verify_token(token)
    if not decoded:
        raise HTTPException(status_code=401,detail="Token invalido o expirado")
    return {"message": f"Bienvenido {decoded['sub']} - acceso concedido"}    