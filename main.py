from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'data': {'name': 'Hoang'}}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/about/")
async def about():
    return {'data': {'about page'}}
