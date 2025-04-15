import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .database import Base

class RolUsuario(enum.Enum):
    ADMIN = "admin"
    USUARIO = "usuario"

class EstadoTarea(enum.Enum):
    PENDIENTE = "pendiente"
    COMPLETADO = "completado"

class Usuario(Base):
    __tablename__="usuarios"
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    username  = Column(String(255), index=True, nullable=False, unique=True)
    email = Column(String, index=True, nullable=False, unique=True)
    password_hash = Column(String, index=True, nullable=False)
    role = Column(Enum(RolUsuario), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

class Tarea(Base):
    __tablename__="tareas"
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    titulo = Column(String, index=True, nullable=False, unique=True)
    descripcion = Column(String, index=True, nullable=False, unique=True)
    estado = Column(Enum(EstadoTarea), nullable=False)
    creado_en = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario")
