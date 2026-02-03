import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QStackedWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QComboBox
)
from PyQt5.QtCore import Qt

class Pagina(QWidget):
    def __init__(self, titulo: str, color: str):
        super().__init__()
        self.setStyleSheet(f"background-color: {color};")
        layout = QVBoxLayout(self)
        label = QLabel(titulo)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(label)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo QStackedWidget (simple)")
        self.resize(520, 360)

        # 1) Crear el QStackedWidget y sus "páginas"
        self.stacked = QStackedWidget()
        self.p1 = Pagina("Página 1 - Inicio", "#3b82f6")   # azul
        self.p2 = Pagina("Página 2 - Datos",  "#10b981")   # verde
        self.p3 = Pagina("Página 3 - Resumen", "#f59e0b") # naranja
        self.stacked.addWidget(self.p1)  # índice 0
        self.stacked.addWidget(self.p2)  # índice 1
        self.stacked.addWidget(self.p3)  # índice 2

        # 2) Controles de navegación
        btn_prev = QPushButton("◀ Anterior")
        btn_next = QPushButton("Siguiente ▶")
        btn_ir_p1 = QPushButton("Ir a P1")
        btn_ir_p2 = QPushButton("Ir a P2")
        btn_ir_p3 = QPushButton("Ir a P3")

        # 3) Combo para elegir página por nombre
        combo = QComboBox()
        combo.addItems(["Página 1", "Página 2", "Página 3"])
        combo.setCurrentIndex(0)

        # 4) Conexiones de señales
        btn_prev.clicked.connect(self.ir_anterior)
        btn_next.clicked.connect(self.ir_siguiente)
        btn_ir_p1.clicked.connect(lambda: self.ir_a(0))
        btn_ir_p2.clicked.connect(lambda: self.ir_a(1))
        btn_ir_p3.clicked.connect(lambda: self.ir_a(2))
        combo.currentIndexChanged.connect(self.ir_a)

        # 5) Layouts
        fila_nav = QHBoxLayout()
        fila_nav.addWidget(btn_prev)
        fila_nav.addWidget(combo)
        fila_nav.addWidget(btn_next)

        fila_directo = QHBoxLayout()
        fila_directo.addWidget(btn_ir_p1)
        fila_directo.addWidget(btn_ir_p2)
        fila_directo.addWidget(btn_ir_p3)

        root = QVBoxLayout(self)
        root.addLayout(fila_nav)
        root.addWidget(self.stacked, stretch=1)
        root.addLayout(fila_directo)

    # --- Métodos de navegación ---
    def ir_a(self, indice: int):
        """Ir a una página específica por índice."""
        if 0 <= indice < self.stacked.count():
            self.stacked.setCurrentIndex(indice)

    def ir_anterior(self):
        i = self.stacked.currentIndex()
        self.ir_a(max(0, i - 1))

    def ir_siguiente(self):
        i = self.stacked.currentIndex()
        self.ir_a(min(self.stacked.count() - 1, i + 1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = VentanaPrincipal()
    w.show()
    sys.exit(app.exec_())