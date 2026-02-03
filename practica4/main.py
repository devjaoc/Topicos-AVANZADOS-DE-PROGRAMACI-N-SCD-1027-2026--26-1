from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
import sys

class DemoSignals(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Señales y Slots")
        self.btn = QPushButton("Saludar")
        self.btn.clicked.connect(self.saludar)  # conectar señal 'clicked' al slot

        layout = QVBoxLayout(self)
        layout.addWidget(self.btn)

    def saludar(self):
        print("¡Hola desde el slot!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DemoSignals()
    w.show()
    sys.exit(app.exec_())