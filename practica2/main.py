import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QMainWindow")
        self.setCentralWidget(QLabel("Contenido central"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MiVentana()
    w.resize(400, 200)
    w.show()
    sys.exit(app.exec_())