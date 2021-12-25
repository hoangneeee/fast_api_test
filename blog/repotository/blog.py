from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all_blog(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_with_id(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # Method 1
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}

        # Method 2
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog


def create_blog(request, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Done'


def update_blog(id: int, request, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.update(dict(request))
    db.commit()
    return 'Update'

