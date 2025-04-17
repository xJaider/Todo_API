from datetime import date

from sqlalchemy.orm import Session
from ..models.usuario import Usuario, RolUsuario

def crear_usuario_prueba(db: Session):
    usuario_existente = db.query(Usuario).filter(Usuario.email == "test@demo.com").first()
    if usuario_existente:
        return usuario_existente
    
    nuevo_usuario = Usuario(
        username="testuser",
        email="test@demo.com",
        password_hash="hash123",  # Este valor es solo de prueba. En producción, ¡siempre hashea!
        role=RolUsuario.usuario,
        created_at=date.today()
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario