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

def obtener_tareas(db:Session, usuario_id:int):
    tareas = db.query(Tarea).filter(Tarea.usuario_id == usuario_id).all()
    return tareas

def obtener_tarea(db: Session, tarea_id: int, usuario_id: int):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == usuario_id).first()
    return tarea

def actualizar_tarea(db: Session, tarea_id: int, usuario_id: int, tarea_actualizada: TareaCreate):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == usuario_id).first()

    if tarea:
        tarea.titulo = tarea_actualizada.titulo
        tarea.descripcion = tarea_actualizada.descripcion
        tarea.estado = tarea_actualizada.estado.value
        tarea.fecha_vencimiento = tarea_actualizada.fecha_vencimiento

    db.commit()
    db.refresh(tarea)
    return tarea

def eliminar_tarea (db: Session, tarea_id: int, usuario_id: int):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == usuario_id).delete()
    db.commit()
    return tarea