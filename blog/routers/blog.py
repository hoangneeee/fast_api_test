from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session

from blog import schemas, models, oauth2
from blog.database import get_db
from blog.repotository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs'],
)


'''Get All Blog'''
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all_blog(db)


'''Create Blog'''
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_blog(request, db)


'''Get Blog with ID'''
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_with_id(id, db)


'''Update Blogs with ID'''
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),
                 get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)


'''Delete Blogs with ID'''
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,  db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy_blog(id, db)
