# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter
from dotenv import load_dotenv
import os
#hereda la clase QSTACKEDWidget
class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_MAIN = 1

    def __init__(self):
        super().__init__()
        #Cargar archivo .env
        load_dotenv()
        db_url = os.getenv("SECRET", "")
        print("SECRET:", db_url)
        #generar objetos de vista  UI
        self.login_view = LoginView()
        self.main_view = MainView()
        #Service para la autecticacion
        self.auth_service = AuthService()
        #Presentacion 
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_main
        )
        self.addWidget(self.login_view)
        self.addWidget(self.main_view)
        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(640, 400)

    def _go_main(self, username: str):
        self.main_view.set_welcome(username)
        self.setCurrentIndex(self.PAGE_MAIN)
