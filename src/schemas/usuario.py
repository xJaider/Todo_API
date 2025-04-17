# src/schemas/usuario.py

from pydantic import BaseModel, ConfigDict

from enum import Enum
from datetime import date

class RolUsuario(str, Enum):
    admin = "admin"
    usuario = "usuario"

class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str

class UsuarioOut(BaseModel):
    username: str
    email: str

class UsuarioLogin(BaseModel):
    email: str
    password: str


model_config = ConfigDict(from_attributes=True)