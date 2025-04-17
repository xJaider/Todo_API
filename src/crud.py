from sqlalchemy.orm import Session
from .models import Tarea
from .schemas.tarea import TareaCreate

from .models import Usuario, RolUsuario
from datetime import date

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

def crear_usuario_prueba(db: Session):
    usuario_existente = db.query(Usuario).filter(Usuario.email == "test@demo.com").first()
    if usuario_existente:
        return usuario_existente
    
    nuevo_usuario = Usuario(
        username="testuser",
        email="test@demo.com",
        password_hash="hash123",  # Este valor es solo de prueba. En producción, ¡siempre hashea!
        role=RolUsuario.USUARIO,
        created_at=date.today()
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario