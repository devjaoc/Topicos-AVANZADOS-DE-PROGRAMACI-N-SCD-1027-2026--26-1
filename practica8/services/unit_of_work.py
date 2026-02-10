from contextlib import AbstractContextManager
from typing import Callable

class UnitOfWork(AbstractContextManager):
    """Controla la sesión y la transacción por operación.
       Uso:
           with UnitOfWork(SessionLocal) as uow:
               repo = PersonaRepository(uow.session)
               repo.crear(...)
               uow.commit()
    """
    def __init__(self, session_factory: Callable):
        self._session_factory = session_factory
        self.session = None
        self._committed = False

    def __enter__(self):
        self.session = self._session_factory()
        self._committed = False
        return self

    def commit(self):
        self.session.commit()
        self._committed = True

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type is not None or not self._committed:
                # Si hubo excepción o no se llamó commit(), hacemos rollback
                self.session.rollback()
        finally:
            self.session.close()
        # Propagar excepción si existió
        return False