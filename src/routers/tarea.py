# src/routers/tarea.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..schemas.tarea import TareaCreate
from ..crud.tarea import crear_tarea, obtener_tareas, obtener_tarea, actualizar_tarea, eliminar_tarea
# from ..crud.usuario import crear_usuario_prueba
from ..database import get_db
from ..auth import verificar_token

router = APIRouter()

# para el CRUD de tareas

@router.get("/tarea")
def example():
    return {"Ruta desde tarea"}

@router.post("/tareas/")
def crear_tarea_endpoint(tarea: TareaCreate, db: Session = Depends(get_db), usuario:dict = Depends(verificar_token)):
    try:
        # Crear usuario de prueba si no existe
        # usuario = crear_usuario_prueba(db)
        
        nueva_tarea = crear_tarea(db=db, tarea=tarea, usuario_id=usuario["user_id"])
        return {"mensaje": "Tarea creada exitosamente", "tarea": nueva_tarea}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear la tarea: {str(e)}")
    
@router.get("/tareas/")                         # Obtener todas las tareas
def obtener_tareas_endpoint(db: Session = Depends(get_db), usuario:dict = Depends(verificar_token)):
    try:
        tareas = obtener_tareas(db=db, usuario_id=usuario["user_id"])
        if tareas is None:
            raise HTTPException(status_code=401, detail="Tareas nos encontradas")
        return {
            "mensaje": "Tareas obtenidas exitosamente",
            "tareas": tareas
            }
        pass
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener las tareas: {str(e)}")

@router.get("/tareas/{tarea_id}")               # Obtener una sola tarea por ID
def obtener_tarea_endpoint(tarea_id: int, db: Session = Depends(get_db), usuario: dict = Depends(verificar_token)):
    try:
        tarea = obtener_tarea(db=db, tarea_id=tarea_id, usuario_id=usuario["user_id"])
        if tarea is None:
            raise HTTPException(status_code=401, detail="Tarea no encontrada")
        if tarea.usuario_id != usuario["user_id"]:
            raise HTTPException(status_code=403, detail="La tarea actual no pertenece al usuario")
        return {
            "mensaje": "Tarea obtenida exitosamente",
            "tarea": tarea
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener la tarea: {str(e)}")

@router.put("/tareas/{tarea_id}")
def actualizar_tarea_endpoint(tarea_id: int, tarea_actualizar: TareaCreate, db: Session = Depends(get_db), usuario: dict = Depends(verificar_token)):
    try:
        tarea_actualizada = actualizar_tarea(db=db, tarea_id=tarea_id, usuario_id=usuario["user_id"], tarea_actualizada=tarea_actualizar)
        if tarea_actualizada is None:
            raise HTTPException(status_code=401, detail="No se ha podido actualizar la tarea")
        if tarea_actualizada.usuario_id != usuario["user_id"]:
            raise HTTPException(status_code=403, detail="La tarea actual no pertenece al usuario")
        return {
            "mensaje": "Tarea actualizada exitosamente",
            "tarea_actualizada": tarea_actualizada
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al actualizar la tarea: {str(e)}")

@router.delete("/tareas/{tarea_id}")
def eliminar_tarea_endpoint(tarea_id: int, db: Session = Depends(get_db), usuario: dict = Depends(verificar_token)):
    try:
        tarea_eliminada = eliminar_tarea(db=db, tarea_id=tarea_id, usuario_id=usuario["user_id"])
        if tarea_eliminada is None:
            raise HTTPException(status_code=401, detail="Tarea no encontrada")
        if tarea_eliminada.usuario_id != usuario["user_id"]:
            raise HTTPException(status_code=403, detail="La tarea actual no pertenece al usuario")
        return {
            "mensaje": "Tarea eliminada exitosamente",
            "tarea_eliminada": tarea_eliminada
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener la tarea: {str(e)}")
