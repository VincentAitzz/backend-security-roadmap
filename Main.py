from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title='Mi Api - Roadmap')

@app.get("/status")
async def status():
    return {"status":"ok","message":"API Levantada","service":"backend-security-roadmap"}

class EchoRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(...,ge=0,le=150)

@app.post("/echo")
async def echo(payload: EchoRequest):
    return {"received":payload.dict(),"note": "Esto es un hecho seguro"}