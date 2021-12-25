from fastapi import FastAPI

from .database import engine
from .schemas import Blog
from .models import Base

app = FastAPI()

Base.metadata.create_all(engine)


@app.post('/blog/')
def create(request: Blog):
    return request