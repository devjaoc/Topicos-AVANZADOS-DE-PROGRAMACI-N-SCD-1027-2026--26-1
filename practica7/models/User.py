from sqlalchemy import Column, Integer, String
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    def __repr__(self):
        return f"<User id={self.id} name={self.name} >"