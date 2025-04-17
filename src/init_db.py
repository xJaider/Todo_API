from src.database import engine, Base
from .models.tarea import Tarea
from .models.usuario import Usuario

Base.metadata.create_all(engine)