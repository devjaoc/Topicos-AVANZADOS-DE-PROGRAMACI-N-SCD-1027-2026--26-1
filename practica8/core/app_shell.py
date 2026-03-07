# core/app_shell.py
from core.config import AppConfig
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.main_view_alumno import MainViewAlumno
from ui.main_view_maestro import MainViewMaestro
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter
from lib.logger import logger

import os
#hereda la clase QSTACKEDWidget
class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_MAIN = 1
    PAGE_MAIN_ALUMNO = 2
    PAGE_MAIN_MAESTRO = 3

    def __init__(self):
        super().__init__() 

        #generar objetos de vista  UI
        self.login_view = LoginView()
        self.main_view = MainView()
        self.main_view_alumno = MainViewAlumno()
        self.main_view_maestro = MainViewMaestro()
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
        self.addWidget(self.main_view_alumno)
        self.addWidget(self.main_view_maestro)
        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(640, 400)

    def _go_main(self, username: str,role :int):
        logger.info("-------------------->Usuario: "+username+str(role))
        self.main_view_alumno.set_welcome(username)
        self.setCurrentIndex(role)
