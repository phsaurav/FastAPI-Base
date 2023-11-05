"""
Blogs related pydantic schemas
"""
from pydantic import BaseModel
from accounts.schemas import ShowUser


class BlogBase(BaseModel):
    """
    Base Schema
    """

    title: str
    body: str


class Blog(BlogBase):
    """
    ORM Functionality added
    """

    class Config:
        """Pydantic Schema Configuration"""

        from_attributes = True


class ShowBlog(BaseModel):
    """
    Blog with creator information
    """

    title: str
    body: str
    creator: ShowUser

    class Config:
        """Pydantic Schema Configuration"""

        from_attributes = True
