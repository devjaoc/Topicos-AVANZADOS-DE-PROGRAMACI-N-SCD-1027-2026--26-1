# practica4_actualizar.py
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from practica1_crear_bd import ENGINE_URL, User, Role

engine = create_engine(ENGINE_URL, echo=False, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def actualizar():
    with SessionLocal() as session:
        # 1) Cambiar email de 'jose'
        jose = session.execute(
            select(User).where(User.username == "jose")
        ).scalar_one_or_none()
        if jose:
            jose.email = "jose.ortiz@example.com"
            session.commit()
            print("Email de jose actualizado:", jose.email)

        # 2) Agregar 'editor' a 'ana' si no lo tiene
        ana = session.execute(select(User).where(User.username == "ana")).scalar_one_or_none()
        editor = session.execute(select(Role).where(Role.name == "editor")).scalar_one_or_none()
        if ana and editor and editor not in ana.roles:
            ana.roles.append(editor)
            session.commit()
            print("Se agregó rol 'editor' a ana.")

        # 3) Reemplazar roles de 'luis' a solo 'viewer'
        luis = session.execute(select(User).where(User.username == "luis")).scalar_one_or_none()
        viewer = session.execute(select(Role).where(Role.name == "viewer")).scalar_one_or_none()
        if luis and viewer:
            luis.roles = [viewer]
            session.commit()
            print("Roles de luis actualizados a solo 'viewer'.")

if __name__ == "__main__":
    actualizar()