# src/routers/usuario.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.usuario import UsuarioCreate
from ..auth import verificar_token
from ..schemas.respuesta import RespuestaBase, RespuestaError

from ..crud.usuario import crear_usuario, obtener_usuario

router = APIRouter()

@router.get("/usuario")
def example():
    return {"Ruta desde usuario"}

def error_detalles(mensaje: str, detalle: str | None = None):
    return RespuestaError(status="error", mensaje=mensaje, detail=detalle).model_dump()

@router.post("/usuarios/")
def crear_nuevo_usuario(usuario:UsuarioCreate, db: Session = Depends(get_db)):
    try:
        nuevo_usuario = crear_usuario(db=db, usuario=usuario)
        if nuevo_usuario is None:
            raise HTTPException(status_code=400, detail=error_detalles("Error al crear nuevo usuario", "Email o username ya registrado"))
        return RespuestaBase(status="success", mensaje="Usuario creado exitosamente", data=nuevo_usuario)
    except Exception as e:
        raise HTTPException(status_code=400, detail=error_detalles("Error al crear nuevo usuario", str(e)))
    
@router.get("/usuarios/me")
def obtener_usuario_actual(usuario: dict = Depends(verificar_token), db: Session = Depends(get_db)):
    try:
        usuario_actual = obtener_usuario(db=db, usuario_id=usuario["user_id"])
        if usuario_actual is None:
            raise HTTPException(status_code=401, detail=error_detalles("Usuario no encontrado"))
        return RespuestaBase(status="success", mensaje="Usuario encontrado", data=usuario_actual)
    except Exception as e:
        raise HTTPException(status_code=400, detail=error_detalles("Error al obtener usuario", str(e)))
