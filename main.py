from fastapi import FastAPI

from typing import Optional

from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return {'data': 'home'}


@app.get("")
async def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}


@app.get("/blog/unpublished")
def unpublished():
    return {'data': {'nhung blog chua duoc cong khai'}}


@app.get("/blog/{id}")
async def show_blog(id: int):
    #tim nap blog voi id = id
    return {'data': id}


@app.get("/blog/{id}/comments")
async def comments(id: int, limit=10):
    #tim nap comment trong blog voi id = id
    return {'data': {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog/")
def create_blog(blog: Blog):
    return {'data': f"Blog is created { blog.title }"}
