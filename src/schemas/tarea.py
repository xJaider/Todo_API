# src/schemas/tareas.py

from pydantic import BaseModel, ConfigDict
from enum import Enum
from datetime import date

class EstadoTarea(str, Enum):
    pendiente = "pendiente"
    completado = "completado"

class TareaCreate(BaseModel):
    titulo: str
    descripcion: str
    estado: EstadoTarea
    fecha_vencimiento: date

class TareaOut(BaseModel):
    id: int
    titulo: str
    descripcion: str
    estado: EstadoTarea
    fecha_vencimiento: date
    creado_en: date
    usuario_id: int

model_config = ConfigDict(from_attributes=True)