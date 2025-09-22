import uuid
from datetime import datetime, timedelta, timezone
from jose import jwt
from pydantic import BaseModel
from .config import settings

class JWTPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

NOW = lambda: datetime.now(timezone.utc)

def _encode_jwt(sub: str, minutes: int, jti: str | None = None) -> str:
    exp = NOW() + timedelta(minutes=minutes)
    payload = {
        "sub": sub, 
        "exp": exp, 
        "iat": NOW(), 
        "jti": jti or str(uuid.uuid4())
        }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_alg)