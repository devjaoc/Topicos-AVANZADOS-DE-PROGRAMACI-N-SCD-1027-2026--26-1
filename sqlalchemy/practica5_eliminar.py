# practica5_eliminar.py
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from practica1_crear_bd import ENGINE_URL, User, Role

engine = create_engine(ENGINE_URL, echo=False, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def eliminar():
    with SessionLocal() as session:
        # 1) Quitar el rol 'editor' de 'jose'
        jose = session.execute(select(User).where(User.username == "jose")).scalar_one_or_none()
        editor = session.execute(select(Role).where(Role.name == "editor")).scalar_one_or_none()
        if jose and editor and editor in jose.roles:
            jose.roles.remove(editor)
            session.commit()
            print("Se quitó 'editor' de jose.")

        # 2) Eliminar usuario 'ana' (se limpian asociaciones por ondelete=CASCADE)
        ana = session.execute(select(User).where(User.username == "ana")).scalar_one_or_none()
        if ana:
            session.delete(ana)
            session.commit()
            print("Usuario 'ana' eliminado.")

        # 3) Eliminar rol 'admin' solo si no está asignado a nadie
        admin = session.execute(select(Role).where(Role.name == "admin")).scalar_one_or_none()
        if admin:
            usuarios_admin = list(admin.users)
            if len(usuarios_admin) == 0:
                session.delete(admin)
                session.commit()
                print("Rol 'admin' eliminado.")
            else:
                print(f"No se elimina 'admin'; asignado a {len(usuarios_admin)} usuario(s).")

if __name__ == "__main__":
    eliminar()