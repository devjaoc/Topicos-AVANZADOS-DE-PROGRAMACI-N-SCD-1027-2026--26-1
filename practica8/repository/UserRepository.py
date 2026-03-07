from typing import List, Optional
from models.User import User

class UserRepository:
    """Repositorio específico de Usuario. Recibe una sesión por operación."""

    def __init__(self, session):
        self.session = session

    def list(self) -> List[User]:
        return self.session.query(User).order_by(User.id.desc()).all()

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter_by(id=user_id).first()

    def create(self, name: str, password: str, email: str ) -> User:
        obj = User(name=name, password=password, email=email)
        self.session.add(obj)
        

    def find_by_user_password(self, name: str, password: str) -> Optional[User]:
        return (
            self.session.query(User)
            .filter(User.name == name, User.password == password)
            .first()
        )
