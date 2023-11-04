"""Accounts related API Routes"""
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core import database, token

from accounts import schemas, models
from accounts.api.v1 import service
from accounts.utils import Hash

router = APIRouter(prefix="/api/accounts", tags=["Users"])


get_db = database.get_db


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    """Create a new user"""
    return service.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    """Get a particular user"""
    return service.show(id, db)


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    """Login Authorization"""
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
