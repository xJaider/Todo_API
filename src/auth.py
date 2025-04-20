# src/auth.py
import os

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
import datetime

from .models.usuario import Usuario

bearer_scheme = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
key = os.getenv("SECRET_KEY_TOKEN")

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
    payload = {
        "sub": str(id),
        "role": role,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
        "iat": datetime.datetime.now(datetime.timezone.utc)
    }
    token = jwt.encode(payload, key, algorithm="HS256")
    print(key)
    print(token)
    return {
        "access_token": token,
        "token_type": "bearer"
    }

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        token = credentials.credentials.strip().replace('"', '')
        print(f"TOKEN LIMPIO: >{token}<")

        payload = jwt.decode(token, key, algorithms="HS256")
        user_id = int(payload.get("sub"))
        role:str = payload.get("role")

        if user_id is None or role is None:
            raise HTTPException(status_code=401, detail="Token invalido")

        return {
            "user_id": user_id,
            "role": role
        }
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except JWTError as e:
        print("Error JWT:", str(e))
        raise HTTPException(status_code=401, detail="Token no valido")