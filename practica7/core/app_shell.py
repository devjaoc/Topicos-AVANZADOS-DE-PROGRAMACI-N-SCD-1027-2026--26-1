# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget, QWidget
from ui.login_view import LoginView

from services.auth_service import AuthService
from repository.view_repository import ViewRepository
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_MAIN = 1

    def __init__(self):
        super().__init__()        
        self.login_view = LoginView()        
        self.auth_service = AuthService()    
          
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_main
        )
        self.addWidget(self.login_view)
        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(640, 400)

    def _go_main(self, username: str, role: str):
        self.view_repository= ViewRepository()
        view = self.view_repository.get_view_for_role(role)        
        self.main_view = view
        self.main_view.set_welcome(username)
        self.addWidget(self.main_view)
        self.setCurrentIndex(self.PAGE_MAIN)
        