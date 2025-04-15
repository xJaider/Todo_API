from src.database import engine, Base
from src import models

Base.metadata.create_all(engine)