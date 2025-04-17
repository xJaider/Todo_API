from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.tarea import TareaCreate
from ..crud.tarea import crear_tarea
from ..crud.usuario import crear_usuario_prueba
from ..database import get_db

router = APIRouter()

# para el CRUD de tareas

@router.get("/tarea")
def example():
    return {"Ruta desde tarea"}

@router.post("/tareas/")
def crear_tarea_endpoint(tarea: TareaCreate, db: Session = Depends(get_db)):
    try:
        # Crear usuario de prueba si no existe
        usuario = crear_usuario_prueba(db)

        nueva_tarea = crear_tarea(db=db, tarea=tarea, usuario_id=usuario.id)
        return {"mensaje": "Tarea creada exitosamente", "tarea": nueva_tarea}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear la tarea: {str(e)}")
