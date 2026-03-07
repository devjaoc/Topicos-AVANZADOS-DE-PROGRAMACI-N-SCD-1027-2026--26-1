# app.py
import sys
from PyQt5.QtWidgets import QApplication
from core.app_shell import AppShell
from lib.logger import logger
def handle_exception(exc_type, exc_value, exc_traceback):
    """Captura excepciones no controladas en PyQt5 y las registra en logs."""
    if issubclass(exc_type, KeyboardInterrupt):
        # Comportamiento normal para Ctrl + C
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error(
        "Excepción no controlada",
        exc_info=(exc_type, exc_value, exc_traceback)
    )
    
def main():
    sys.excepthook = handle_exception
    app = QApplication(sys.argv)
    shell = AppShell()
    shell.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




