# src/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.usuario import UsuarioLogin
from ..auth import comprobar_sesion

router = APIRouter()

@router.get("/auth")
def example():
    return {"Ruta desde auth"}

@router.post("/login")
def login(usuario:UsuarioLogin, db: Session = Depends(get_db)):
    try:
        verificacion = comprobar_sesion(db=db, email=usuario.email, password=usuario.password)
        
        if verificacion is None:
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        else:
            return {"mensaje": "Login exitoso"}
        pass
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al logearse: {str(e)}")
    
