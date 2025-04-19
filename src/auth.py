# src/auth.py
import os

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import datetime

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
        return usuario
    else:
        return None
    
def generar_token(id:int, role:str):
    key = os.getenv("SECRET_KEY_TOKEN")
    payload = {
        "sub": id,
        "role": role,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
        "iat": datetime.datetime.now(datetime.timezone.utc)
    }
    token = jwt.encode(payload, key, algorithm="HS256")
    return {
        "access_token": token,
        "token_type": "bearer"
    }