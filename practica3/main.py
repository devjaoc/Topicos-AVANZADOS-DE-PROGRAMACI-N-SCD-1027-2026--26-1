# archivo: ventana_con_layout.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt


class VentanaConLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana con Layout - Ejemplo Básico")
        self.resize(380, 200)
        self.setWindowTitle("Layouts")
        self.label = QLabel("Pulsa el botón")
        self.boton = QPushButton("Aceptar")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.boton)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = VentanaConLayout()
    w.show()
    sys.exit(app.exec_())