# services/auth_service.py
from dataclasses import dataclass

from repository.UserRepository import UserRepository
from services.unit_of_work import UnitOfWork
from models.db import SessionLocal
from lib.logger import logger
@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role:int=-1

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self, valid_user: str = "admin", valid_password: str = "1234"):
        self._user = valid_user
        self._password = valid_password
    def login(self, username: str, password: str) -> AuthResult:                   
        if not username or not password:
            return AuthResult(False, "Usuario o contraseña incorrectos.")
        with UnitOfWork(SessionLocal) as uow:
           repo = UserRepository(uow.session)
           user =  repo.find_by_user_password(username,password)
           uow.commit() 
           if user:                           
               user_name = user.name        

        if user:           
            logger.info("Usuario: "+username+" password: "+password+" roles: "+str(roles.get(user_name)))
            return AuthResult(True, user_name,roles.get(user_name))        
        logger.warning("Error "+username+" "+password)
        return AuthResult(False, "Usuario y contraseña son requeridos.")
      
        
