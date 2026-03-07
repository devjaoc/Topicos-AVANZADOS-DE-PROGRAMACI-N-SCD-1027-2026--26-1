# practica2_insertar.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practica1_crear_bd import ENGINE_URL,  User, Role

engine = create_engine(ENGINE_URL, echo=False, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def poblar():
    with SessionLocal() as session:
        # 1) Roles
        admin = Role(name="admin", description="Acceso total")
        editor = Role(name="teacher", description="Calificar")
        viewer = Role(name="student", description="ver Calificaciones")
        session.add_all([admin, editor, viewer])
        session.commit()

        # 2) Usuarios (en producción guarda hash real)
        u1 = User(username="admin", email="jose@example.com", password_hash="hash1")
        u2 = User(username="teacher", email="antonoi@example.com", password_hash="hash2")
        u3 = User(username="alumno", email="luis@example.com", password_hash="hash3")

        # 3) Asignaciones
        u1.roles.extend([admin, editor])
        u2.roles.append(viewer)
        u3.roles.extend([editor, viewer])

        session.add_all([u1, u2, u3])
        session.commit()
        print("Usuarios y roles insertados, asignaciones realizadas (MySQL).")

if __name__ == "__main__":
    poblar()
