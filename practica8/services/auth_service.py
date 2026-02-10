# services/auth_service.py
from dataclasses import dataclass

from models.UserRepository import UserRepository
from services.unit_of_work import UnitOfWork
from models.db import SessionLocal

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self, valid_user: str = "admin", valid_password: str = "1234"):
        self._user = valid_user
        self._password = valid_password

    def login(self, username: str, password: str) -> AuthResult:
        
        with UnitOfWork(SessionLocal) as uow:
            repo = UserRepository(uow.session)
            repo.find_by_id(1)
            uow.commit()
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        if username == self._user and password == self._password:
            return AuthResult(True, "Autenticación exitosa.")
        return AuthResult(False, "Usuario o contraseña incorrectos.")
