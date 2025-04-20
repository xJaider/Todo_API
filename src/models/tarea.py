# src/models/tarea.py

import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..database import Base

from ..models.usuario import Usuario

class EstadoTarea(enum.Enum):
    pendiente = "pendiente"
    completado = "completado"

class Tarea(Base):
    __tablename__="tareas"

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    titulo = Column(String, index=True, nullable=False, unique=True)
    descripcion = Column(String, index=True, nullable=False, unique=True)
    estado = Column(Enum(EstadoTarea), nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    creado_en = Column(Date, default=date.today, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario")