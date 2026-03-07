# ui/main_view.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel

class MainStudentView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal - MVP Estudiante")
        self.resize(520, 320)
        self._label = QLabel("Bienvenido student, has iniciado sesión correctamente.", alignment=Qt.AlignCenter)
        self.setCentralWidget(self._label)

    def set_welcome(self, user: str):
        self._label.setText(f"Bienvenido student, {user}. ¡Sesión iniciada!")
