
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

password_hash = PasswordHash.recommended()

ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 30


def authenticate_admin(username: str, password: str) -> bool:
    if username != settings.admin_username:
        return False

    return password_hash.verify(
        password,
        settings.admin_password_hash,
    )


def create_access_token(username: str) -> str:
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=ALGORITHM,
    )


def verify_access_token(token: str) -> str | None:
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[ALGORITHM],
        )

        username = payload.get("sub")

        if username != settings.admin_username:
            return None

        return username

    except jwt.InvalidTokenError:
        return None
