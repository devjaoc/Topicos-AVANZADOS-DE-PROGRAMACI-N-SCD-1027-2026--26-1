# practica1_crear_bd.py
from sqlalchemy import (
    create_engine, Column, Integer, String, Table, ForeignKey, UniqueConstraint, Index
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Cambia usuario, password, host y base según tu entorno
ENGINE_URL = "mysql+pymysql://root:@localhost:3306/practicas_roles?charset=utf8mb4"

# pool_pre_ping ayuda con desconexiones; echo=True muestra SQL (útil en prácticas)
engine = create_engine(
    ENGINE_URL,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

Base = declarative_base()

# Tabla de asociación N:M
user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("role_id", ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
    UniqueConstraint("user_id", "role_id", name="uq_user_role"),
    mysql_engine="InnoDB",         # asegurar soporte FK/cascade en MySQL
    mysql_charset="utf8mb4",
)

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8mb4"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(120), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)

    roles = relationship(
        "Role",
        secondary=user_roles,
        back_populates="users",
        lazy="selectin",
        cascade="save-update",
    )

    def __repr__(self):
        return f"<User id={self.id} username={self.username!r}>"

class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8mb4"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    description = Column(String(200), nullable=True)

    users = relationship(
        "User",
        secondary=user_roles,
        back_populates="roles",
        lazy="selectin",
    )

    def __repr__(self):
        return f"<Role id={self.id} name={self.name!r}>"



# Crear tablas físicas
Base.metadata.create_all(engine)

# Session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

if __name__ == "__main__":
    with SessionLocal() as session:
        print("Base y tablas creadas correctamente en MySQL (users, roles, user_roles).")