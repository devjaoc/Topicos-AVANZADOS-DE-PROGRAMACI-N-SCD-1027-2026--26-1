# ui/login_view.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class LoginView(QWidget):
    loginRequested = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - MVP")
        self.resize(360, 200)

        self.lbl_titulo = QLabel("Iniciar sesión")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_titulo.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.txt_usuario = QLineEdit()
        self.txt_usuario.setPlaceholderText("Usuario")

        self.txt_password = QLineEdit()
        self.txt_password.setPlaceholderText("Contraseña")
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.btn_toggle_pw = QPushButton("👁")
        self.btn_toggle_pw.setCheckable(True)
        self.btn_toggle_pw.setToolTip("Mostrar/Ocultar contraseña")
        self.btn_toggle_pw.setFixedWidth(36)
        self.btn_toggle_pw.toggled.connect(self._toggle_password)

        pw_row = QHBoxLayout()
        pw_row.addWidget(self.txt_password)
        pw_row.addWidget(self.btn_toggle_pw)

        self.btn_login = QPushButton("Entrar")
        self.btn_login.clicked.connect(self._emit_login)

        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl_titulo)
        layout.addSpacing(8)
        layout.addWidget(self.txt_usuario)
        layout.addLayout(pw_row)
        layout.addSpacing(8)
        layout.addWidget(self.btn_login)
        layout.addStretch(1)

        self.txt_usuario.returnPressed.connect(self._emit_login)
        self.txt_password.returnPressed.connect(self._emit_login)

    def get_credentials(self) -> tuple:
        return self.txt_usuario.text().strip(), self.txt_password.text()

    def clear_password(self):
        self.txt_password.clear()
        self.txt_password.setFocus()

    def show_error(self, message: str):
        self.lbl_titulo.setText(f"❌ {message}")
        self.lbl_titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #b00020;")

    def show_info(self, message: str):
        self.lbl_titulo.setText(message)
        self.lbl_titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #1b5e20;")

    def _toggle_password(self, checked: bool):
        self.txt_password.setEchoMode(QLineEdit.Normal if checked else QLineEdit.Password)

    def _emit_login(self):
        user, pw = self.get_credentials()
        self.loginRequested.emit(user, pw)
