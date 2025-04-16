from fastapi import APIRouter

router = APIRouter()

# para el CRUD de tareas

@router.get("/tarea")
def example():
    return {"Ruta desde tarea"}
