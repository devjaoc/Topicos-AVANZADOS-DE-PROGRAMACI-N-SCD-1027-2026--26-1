from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Para escritorio con SQLite
#DATABASE_URL = "sqlite:///app.db"
DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost/materiaTopicos"

# future=True activa la API 2.0; echo=False quita logs SQL
engine = create_engine(DATABASE_URL, echo=False, future=True,
    pool_size=5,          # tamaño del pool
    max_overflow=10,      # conexiones extra si se satura el pool
    pool_pre_ping=True,   # valida conexiones antes de usarlas
)

# Session local: una por operación/UI-interacción
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

Base = declarative_base()

def init_db():
    # Importa entidades y crea tablas
    from .User import User  # noqa: F401
    Base.metadata.create_all(bind=engine)