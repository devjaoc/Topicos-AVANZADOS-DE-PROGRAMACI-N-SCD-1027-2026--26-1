# app.py
import sys
from PyQt5.QtWidgets import QApplication
from core.app_shell import AppShell

def main():
    app = QApplication(sys.argv)
    shell = AppShell()
    shell.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
