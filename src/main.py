from fastapi import FastAPI
from src.routers import tarea, auth, usuario

app = FastAPI()

app.include_router(tarea.router)
app.include_router(auth.router)
app.include_router(usuario.router)

@app.get("/")
def read_root():
    return {"Hello World!"}
