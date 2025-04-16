from fastapi import FastAPI
from src.routers import tarea

app = FastAPI()

app.include_router(tarea.router)

@app.get("/")
def read_root():
    return {"Hello World!"}
