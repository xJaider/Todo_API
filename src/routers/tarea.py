# src/routers/tarea.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..schemas.tarea import TareaCreate
from ..crud.tarea import crear_tarea, obtener_tareas, obtener_tarea, actualizar_tarea, eliminar_tarea
from ..schemas.respuesta import RespuestaBase, RespuestaError
# from ..crud.usuario import crear_usuario_prueba
from ..database import get_db
from ..auth import verificar_token

router = APIRouter()

# para el CRUD de tareas

@router.get("/tarea")
def example():
    return {"Ruta desde tarea"}

def error_detalles(mensaje: str, detalle: str | None = None):
    return RespuestaError(status="error", mensaje=mensaje, detail=detalle).model_dump()

@router.post("/tareas/")
def crear_tarea_endpoint(tarea: TareaCreate, db: Session = Depends(get_db), usuario:dict = Depends(verificar_token)):
    try:
        # Crear usuario de prueba si no existe
        # usuario = crear_usuario_prueba(db)
        
        nueva_tarea = crear_tarea(db=db, tarea=tarea, usuario_id=usuario["user_id"])
        return RespuestaBase(status="success", mensaje="Tarea creada exitosamente", data=nueva_tarea)
    except Exception as e:
        raise HTTPException(status_code=400, detail=error_detalles("Error al crear la tarea", str(e)))
    
@router.get("/tareas/")                         # Obtener todas las tareas
def obtener_tareas_endpoint(db: Session = Depends(get_db), usuario:dict = Depends(verificar_token)):
    try:
        tareas = obtener_tareas(db=db, usuario_id=usuario["user_id"])
        if tareas is None:
            raise HTTPException(status_code=401, detail=error_detalles("Tareas nos encontradas"))
        return RespuestaBase(status="success", mensaje="Tareas obtenidas exitosamente", data=tareas)
    except Exception as e:
        raise HTTPException(status_code=400, detail=error_detalles("Error al obtener las tareas", str(e)))

@router.get("/tareas/{tarea_id}")               # Obtener una sola tarea por ID
def obtener_tarea_endpoint(tarea_id: int, db: Session = Depends(get_db), usuario: dict = Depends(verificar_token)):
    try:
        tarea = obtener_tarea(db=db, tarea_id=tarea_id, usuario_id=usuario["user_id"])
        if tarea is None:
            raise HTTPException(status_code=401, detail=error_detalles("Tarea no encontrada"))
        if tarea.usuario_id != usuario["user_id"]:
            raise HTTPException(status_code=403, detail=error_detalles("La tarea actual no pertenece al usuario"))
        return RespuestaBase(status="success", mensaje="Tarea obtenida exitosamente", data=tarea)
    except Exception as e:
        raise HTTPException(status_code=400, detail=error_detalles("Error al obtener la tarea", str(e)))

@router.put("/tareas/{tarea_id}")
def actualizar_tarea_endpoint(tarea_id: int, tarea_actualizar: TareaCreate, db: Session = Depends(get_db), usuario: dict = Depends(verificar_token)):
    try:
        tarea_actualizada = actualizar_tarea(db=db, tarea_id=tarea_id, usuario_id=usuario["user_id"], tarea_actualizada=tarea_actualizar)
        if tarea_actualizada is None:
            raise HTTPException(status_code=401, detail=error_detalles("No se ha podido actualizar la tarea"))
        if tarea_actualizada.usuario_id != usuario["user_id"]:
            raise HTTPException(status_code=403, detail=error_detalles("La tarea actual no pertenece al usuario"))
        return RespuestaBase(status="success", mensaje="Tarea actualizada exitosamente", data=tarea_actualizada)  
    except Exception as e:
        raise HTTPException(status_code=400, detail=error_detalles("Error al actualizar la tarea", str(e)))

@router.delete("/tareas/{tarea_id}")
def eliminar_tarea_endpoint(tarea_id: int, db: Session = Depends(get_db), usuario: dict = Depends(verificar_token)):
    try:
        tarea_eliminada = eliminar_tarea(db=db, tarea_id=tarea_id, usuario_id=usuario["user_id"])
        if tarea_eliminada is None:
            raise HTTPException(status_code=401, detail=error_detalles("Tarea no encontrada"))
        if tarea_eliminada.usuario_id != usuario["user_id"]:
            raise HTTPException(status_code=403, detail=error_detalles("La tarea actual no pertenece al usuario"))
        return RespuestaBase(status="success", mensaje="Tarea eliminada exitosamente", data=tarea_eliminada)
    except Exception as e:
        raise HTTPException(status_code=400, detail=error_detalles("Error al obtener la tarea", str(e)))
