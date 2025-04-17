# src/crud/tarea.py

from sqlalchemy.orm import Session
from ..models.tarea import Tarea
from ..schemas.tarea import TareaCreate

def crear_tarea(db:Session, tarea:TareaCreate, usuario_id:int):
    nueva_tarea = Tarea(
        titulo = tarea.titulo,
        descripcion = tarea.descripcion,
        estado = tarea.estado.value,
        fecha_vencimiento = tarea.fecha_vencimiento,
        usuario_id=usuario_id
    )
    
    db.add(nueva_tarea)
    db.commit()

    db.refresh(nueva_tarea)

    return nueva_tarea