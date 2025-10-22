import time
from fastapi import Request
from app.core.logging import logger

async def log_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000

    logger.info({
        "message":"Request Proceed",
        "method":request.method,
        "path":request.url.path,
        "status":response.status_code,
        "time_ms":round(process_time, 2)
    })

    return response

async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode = block"
    response.headers["Referrer-Policy"] = "no-referrer"
    return response