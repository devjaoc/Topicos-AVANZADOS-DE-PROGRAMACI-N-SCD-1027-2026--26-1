# practica3_consultar.py
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, selectinload
from practica1_crear_bd import ENGINE_URL, User, Role
from practica1_crear_bd import user_roles  # tabla de asociación

engine = create_engine(ENGINE_URL, echo=False, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def consultar():
    with SessionLocal() as session:
        # 1) Usuarios con roles
        usuarios = session.execute(
            select(User).options(selectinload(User.roles)).order_by(User.username)
        ).scalars().all()
        print("\nUsuarios con roles:")
        for u in usuarios:
            print(f"- {u.username}: {[r.name for r in u.roles]}")

        # 2) Conteo de usuarios por rol
        conteo = session.execute(
            select(Role.name, func.count(user_roles.c.user_id))
            .select_from(Role)
            .join(user_roles, Role.id == user_roles.c.role_id, isouter=True)
            .group_by(Role.name)
            .order_by(Role.name)
        ).all()
        print("\nConteo de usuarios por rol:")
        for rol, total in conteo:
            print(f"- {rol}: {total}")

        # 3) Usuarios con rol "editor"
        editores = session.execute(
            select(User)
            .join(user_roles, User.id == user_roles.c.user_id)
            .join(Role, Role.id == user_roles.c.role_id)
            .where(Role.name == "editor")
            .order_by(User.username)
        ).scalars().all()
        print("\nUsuarios con rol 'editor':", [u.username for u in editores])

        # 4) Usuarios sin ningún rol
        sin_rol = session.execute(
            select(User)
            .join(user_roles, User.id == user_roles.c.user_id, isouter=True)
            .where(user_roles.c.user_id.is_(None))
            .order_by(User.username)
        ).scalars().all()
        print("\nUsuarios sin rol:", [u.username for u in sin_rol])

if __name__ == "__main__":
    consultar()