# src/auth.py

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from .models.usuario import Usuario

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_hash(password:str, hashed_password:str) -> bool:
    return pwd_context.verify(password, hashed_password)

def obtener_email(db:Session, email:str):
    return db.query(Usuario).filter(Usuario.email == email).first()
    
def comprobar_sesion(db: Session, email:str, password:str):
    usuario = obtener_email(db=db ,email=email)
    if usuario and verify_hash(password=password, hashed_password=usuario.password_hash):
        return usuario.username
    else:
        return None