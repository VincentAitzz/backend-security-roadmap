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