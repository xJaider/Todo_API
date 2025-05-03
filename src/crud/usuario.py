# src/crud/usuario.py

from datetime import date

from sqlalchemy.orm import Session

from ..schemas.usuario import UsuarioCreate, UsuarioResponse
from ..models.usuario import Usuario, RolUsuario
from ..auth import hash_password

def crear_usuario_prueba(db: Session):
    usuario_existente = db.query(Usuario).filter(Usuario.email == "test@demo.com").first()
    if usuario_existente:
        return usuario_existente
    
    nuevo_usuario = Usuario(
        username="testuser",
        email="test@demo.com",
        password_hash="hash123",
        role=RolUsuario.usuario,
        created_at=date.today()
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario

def crear_usuario(db:Session, usuario:UsuarioCreate):

    if db.query(Usuario).filter(Usuario.email == usuario.email).first():
        return None

    if db.query(Usuario).filter(Usuario.username == usuario.username).first():
        return None
    
    nuevo_usuario = Usuario(
        username=usuario.username,
        email=usuario.email,
        password_hash=hash_password(usuario.password),
        role=RolUsuario.usuario
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario

def obtener_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None
    usuario_schema = UsuarioResponse.model_validate(usuario).model_dump()
    return usuario_schema
