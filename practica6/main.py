from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout
import sys

class Pagina1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        btn = QPushButton("Ir a página 2")
        layout.addWidget(btn)
        btn.clicked.connect(lambda: parent.setCurrentIndex(1))

class Pagina2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        btn = QPushButton("Regresar a página 1")
        layout.addWidget(btn)
        btn.clicked.connect(lambda: parent.setCurrentIndex(0))

app = QApplication(sys.argv)

stack = QStackedWidget()
stack.addWidget(Pagina1(parent=stack))  # Página 0
stack.addWidget(Pagina2(parent=stack))  # Página 1

stack.show()
app.exec_()