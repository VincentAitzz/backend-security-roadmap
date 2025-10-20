from fastapi import FastAPI
from app.api.middleware import log_request
from app.api.routes import status, echo, secure, time

app = FastAPI(title="Backend Security Roadmap")

app.middleware("http")(log_request)

app.include_router(status.router)
app.include_router(echo.router)
app.include_router(secure.router)
app.include_router(time.router)
