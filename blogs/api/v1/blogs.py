"""
Blogs related API routes
"""
from typing import List
from fastapi import APIRouter, Depends, status
from core import oauth2
from blogs import schemas
from sqlalchemy.orm import Session
from accounts.schemas import User
from core import database
from blogs.api.v1 import service

router = APIRouter(prefix="/api/blog/v1", tags=["Blogs"])

get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def all_blogs(
    db: Session = Depends(get_db),
):
    """
    Get all blogs
    """
    return service.get_all(db)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create(
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    """
    Create a Blog
    """
    return service.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    """
    Delete a Blog
    """
    return service.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    """
    Update a Blog
    """
    return service.update(id, request, db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(
    id: int,
    db: Session = Depends(get_db),
):
    "Show a particular Blog"
    return service.show(id, db)
