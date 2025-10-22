import jwt
from datetime import datetime, timedelta
from app.core.config import SECRET_KEY

ALGORITHM = "HS256"

def create_token(data: dict,expires_in_minutes: int = 30):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(expires_in_minutes)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token:str):
    try:
        decoded = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None