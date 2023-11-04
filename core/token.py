"""
Token related functionality
"""
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from core.constants import Constants


def create_access_token(data: dict):
    """Create a new access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=Constants.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, Constants.SECRET_KEY, algorithm=Constants.ALGORITHM
    )
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    """Verify the access token"""
    try:
        payload = jwt.decode(
            token, Constants.SECRET_KEY, algorithms=[Constants.ALGORITHM]
        )
        email: Optional[str] = payload.get("sub")
        if email is None:
            raise credentials_exception
        # token_data = schemas.TokenData(email=email)
    except JWTError as exc:
        raise credentials_exception from exc
