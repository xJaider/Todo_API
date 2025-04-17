from sqlalchemy import create_engine # para crear el motor de SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

dialecto = os.getenv("DB_CONNECTION")
username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DATABASE")

database_url = f"{dialecto}://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(database_url, echo=True) # Creando el motor de conexion

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base() # Creando la clase Base para que los modelos puedan heredarlas

