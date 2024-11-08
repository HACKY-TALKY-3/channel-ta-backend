from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoint.function.route import router as function_router
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(function_router)



