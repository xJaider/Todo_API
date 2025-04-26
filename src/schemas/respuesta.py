# src/schemas/respuesta.py

from pydantic import BaseModel, ConfigDict

class RespuestaBase(BaseModel):
    status: str
    mensaje: str
    data: dict | None = None

class RespuestaError(BaseModel):
    status: str
    mensaje: str
    detail: str | None = None

model_config = ConfigDict(from_attributes=True)