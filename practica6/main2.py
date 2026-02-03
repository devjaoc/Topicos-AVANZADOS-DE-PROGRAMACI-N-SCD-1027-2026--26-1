# stacked_demo.py
import sys
from PyQt5.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QLabel, QFrame, QShortcut, QGraphicsOpacityEffect
)

# Índices semánticos para páginas
PAGE_HOME = 0
PAGE_SETTINGS = 1
PAGE_ABOUT = 2


class PageHome(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("🏠 Inicio")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        desc = QLabel("Bienvenido. Usa el menú lateral o Ctrl+1/2/3 para navegar.")
        desc.setWordWrap(True)
        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch(1)


class PageSettings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("⚙️ Configuración")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        layout.addWidget(title)

        # Contenido “dummy”
        layout.addWidget(QLabel("• Tema: Claro"))
        layout.addWidget(QLabel("• Idioma: Español (MX)"))
        layout.addWidget(QLabel("• Auto-guardado: Activado"))
        layout.addStretch(1)


class PageAbout(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("ℹ️ Acerca de")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        info = QLabel(
            "Demostración de QStackedWidget con menú lateral, atajos y animación.\n"
            "Autor: Ejemplo educativo.\n"
            "Licencia: Uso libre para aprendizaje."
        )
        info.setWordWrap(True)
        layout.addWidget(title)
        layout.addWidget(info)
        layout.addStretch(1)


class SideMenu(QWidget):
    """Menú lateral con botones. Emite navegación llamando a un callback."""
    def __init__(self, on_nav):
        super().__init__()
        self.on_nav = on_nav
        self.setFixedWidth(180)

        self.btn_home = QPushButton("Inicio   (Ctrl+1)")
        self.btn_settings = QPushButton("Configuración   (Ctrl+2)")
        self.btn_about = QPushButton("Acerca de   (Ctrl+3)")



        self.btn_home.clicked.connect(lambda: self.on_nav(PAGE_HOME))
        self.btn_settings.clicked.connect(lambda: self.on_nav(PAGE_SETTINGS))
        self.btn_about.clicked.connect(lambda: self.on_nav(PAGE_ABOUT))

        # Layout vertical y separador visual
        lay = QVBoxLayout(self)
        lay.addWidget(self.btn_home)
        lay.addWidget(self.btn_settings)
        lay.addWidget(self.btn_about)
        lay.addStretch(1)

        self.setStyleSheet("""
            QWidget#SideMenu {
                background: #f4f6f8;
                border-right: 1px solid #d0d7de;
            }
        """)
        self.setObjectName("SideMenu")

    def set_active(self, index: int):
        self.btn_home.setChecked(index == PAGE_HOME)
        self.btn_settings.setChecked(index == PAGE_SETTINGS)
        self.btn_about.setChecked(index == PAGE_ABOUT)


class FadeStack(QStackedWidget):
    """QStackedWidget con animación de fade al cambiar de página."""
    def __init__(self):
        super().__init__()
        self._duration = 250  # ms
        self._easing = QEasingCurve.InOutQuad

        # Efecto de opacidad aplicado al propio stacked
        self._effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._effect)
        self._effect.setOpacity(1.0)

        self._anim = QPropertyAnimation(self._effect, b"opacity", self)
        self._anim.setDuration(self._duration)
        self._anim.setEasingCurve(self._easing)

    def setCurrentIndexAnimated(self, index: int):
        if index == self.currentIndex():
            return
        # Secuencia: fade-out -> cambiar página -> fade-in
        self._anim.stop()
        self._anim.setStartValue(1.0)
        self._anim.setEndValue(0.0)
        self._anim.finished.connect(lambda: self._on_fade_out_done(index))
        self._anim.start()

    def _on_fade_out_done(self, index: int):
        # Desconectar el slot previo para no acumular conexiones
        try:
            self._anim.finished.disconnect()
        except TypeError:
            pass

        super().setCurrentIndex(index)

        # Fade-in
        self._anim.stop()
        self._anim.setStartValue(0.0)
        self._anim.setEndValue(1.0)
        self._anim.start()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demostración QStackedWidget")
        self.resize(800, 480)

        # Menú lateral y contenedor central
        self.stack = FadeStack()
        self.menu = SideMenu(self.navigate_to)

        # Páginas
        self.page_home = PageHome()
        self.page_settings = PageSettings()
        self.page_about = PageAbout()

        self.stack.addWidget(self.page_home)      # 0
        self.stack.addWidget(self.page_settings)  # 1
        self.stack.addWidget(self.page_about)     # 2

        # Layout principal
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        # Envolver menú en un frame para borde visual
        left = QFrame()
        left.setFrameShape(QFrame.NoFrame)
        left.setLayout(QVBoxLayout())
        left.layout().setContentsMargins(0, 0, 0, 0)
        left.layout().addWidget(self.menu)

        root.addWidget(left)
        root.addWidget(self.stack, stretch=1)

        # Estado inicial
        self.menu.set_active(PAGE_HOME)
        self.stack.setCurrentIndex(PAGE_HOME)

        # Atajos de teclado
        QShortcut(Qt.CTRL + Qt.Key_1, self, activated=lambda: self.navigate_to(PAGE_HOME))
        QShortcut(Qt.CTRL + Qt.Key_2, self, activated=lambda: self.navigate_to(PAGE_SETTINGS))
        QShortcut(Qt.CTRL + Qt.Key_3, self, activated=lambda: self.navigate_to(PAGE_ABOUT))

        # Estilo visual básico
        self.setStyleSheet("""
            QWidget { font-family: Segoe UI, Arial; font-size: 10.5pt; }
            QFrame { background: #ffffff; }
        """)

    def navigate_to(self, index: int):
        """Navegación centralizada con animación y actualización del menú."""
        self.menu.set_active(index)
        self.stack.setCurrentIndexAnimated(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())