from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import schemas, models, hashing
from blog.database import get_db
from ..repotository import user


router = APIRouter(
    prefix="/user",
    tags=['User'],
)


'''Create User'''
@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


'''Show User'''
@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show_user(id, db)