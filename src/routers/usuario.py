# src/routers/usuario.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.usuario import UsuarioCreate

from ..crud.usuario import crear_usuario

router = APIRouter()

@router.get("/usuario")
def example():
    return {"Ruta desde usuario"}

@router.post("/usuarios/")
def crear_nuevo_usuario(usuario:UsuarioCreate, db: Session = Depends(get_db)):
    try:
        nuevo_usuario = crear_usuario(db=db, usuario=usuario)
        return {"mensaje": "Usuario nuevo creada exitosamente", "usuario": nuevo_usuario}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear nuevo usuario: {str(e)}")