"""
Accounts pydantic schemas
"""
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    """
    User Base schema
    """

    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    """
    User Display schema
    """

    name: str
    email: str

    class Config:
        """Pydantic Model Config"""

        from_attributes = True


class Login(BaseModel):
    """
    Login schema
    """

    username: str
    password: str


class Token(BaseModel):
    """
    Token schema
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Token data schema
    """

    email: Optional[str] = None
