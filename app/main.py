from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.middleware import log_request, security_headers
from app.api.routes import status, echo, secure, time as time_router

app = FastAPI(title="Backend Security Roadmap")

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET","POST"],
    allow_headers = ["Content-Type","Autorization","X-API-Key"]
)

app.middleware("http")(log_request)
app.middleware("http")(security_headers)

app.include_router(status.router)
app.include_router(echo.router)
app.include_router(secure.router)
app.include_router(time_router.router)
