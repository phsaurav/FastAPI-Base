"""
All Accounts App Utility Functions
"""
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """
    Hashing related functionality
    """

    @staticmethod
    def bcrypt(password: str):
        """
        Encrypt the provided string password
        """
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        """
        Compare hashed_password against plain_password and verify
        """
        return pwd_cxt.verify(plain_password, hashed_password)
