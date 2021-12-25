from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import schemas, models, hashing
from blog.database import get_db


router = APIRouter()


'''Create User'''
@router.post('/user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED, tags=['user'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


'''Show User'''
@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['user'])
def show_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return user