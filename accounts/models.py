"""
Accounts app DB models
"""
from sqlalchemy import Column, Integer, String, orm
from core.database import Base


class User(Base):
    """
    User Model
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = orm.relationship("Blog", back_populates="creator")
