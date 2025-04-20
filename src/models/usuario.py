# src/models/usuario.py

import enum

from sqlalchemy import Column, Integer, String, Enum, Date
from datetime import date
from ..database import Base

class RolUsuario(enum.Enum):
    admin = "admin"
    usuario = "usuario"

class Usuario(Base):
    __tablename__="usuarios"

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    username  = Column(String(255), index=True, nullable=False, unique=True)
    email = Column(String, index=True, nullable=False, unique=True)
    password_hash = Column(String, index=True, nullable=False)
    role = Column(Enum(RolUsuario), nullable=False)
    created_at = Column(Date, default=date.today, nullable=False)