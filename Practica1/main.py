import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)       # 1) Crear la app
    label = QLabel("¡Hola, PyQt5!")    # 2) Crear un widget (etiqueta)
    label.resize(200, 50)
    label.show()                       # 3) Mostrarlo
    sys.exit(app.exec_())              # 4) Iniciar el loop de eventos