from PyQt5 import QtWidgets, QtCore
import sys

class TareasApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tareas (solo descripción)")
        self.resize(420, 360)

        # -----------------------------
        # Modelo en memoria: una lista
        # -----------------------------
        self.tareas = []  # <- Aquí se guardan las descripciones (strings)

        # -----------------------------
        # Widgets
        # -----------------------------
        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText("Escribe la descripción de la tarea...")

        self.btnAgregar = QtWidgets.QPushButton("Agregar")
        self.btnEliminar = QtWidgets.QPushButton("Eliminar seleccionadas")
        self.btnLimpiar = QtWidgets.QPushButton("Limpiar todo")

        self.lista = QtWidgets.QListWidget()
        self.lista.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        # -----------------------------
        # Layout
        # -----------------------------
        filaEntrada = QtWidgets.QHBoxLayout()
        filaEntrada.addWidget(self.input)
        filaEntrada.addWidget(self.btnAgregar)

        filaBotones = QtWidgets.QHBoxLayout()
        filaBotones.addWidget(self.btnEliminar)
        filaBotones.addWidget(self.btnLimpiar)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(filaEntrada)
        layout.addWidget(self.lista)
        layout.addLayout(filaBotones)

        # -----------------------------
        # Conexiones (signals/slots)
        # -----------------------------
        self.btnAgregar.clicked.connect(self.agregar_tarea)
        self.btnEliminar.clicked.connect(self.eliminar_seleccionadas)
        self.btnLimpiar.clicked.connect(self.limpiar_todo)
        self.input.returnPressed.connect(self.agregar_tarea)  # Enter agrega

    # -----------------------------
    # Lógica
    # -----------------------------
    def agregar_tarea(self):
        descripcion = self.input.text().strip()
        if not descripcion:
            QtWidgets.QMessageBox.information(self, "Aviso", "Escribe una descripción.")
            return

        # Agregar al modelo (lista)
        self.tareas.append(descripcion)

        # Reflejar en la vista (QListWidget)
        self.lista.addItem(descripcion)

        # Limpiar input y enfocar
        self.input.clear()
        self.input.setFocus()

    def eliminar_seleccionadas(self):
        # Obtenemos índices de elementos seleccionados (de mayor a menor)
        seleccion = self.lista.selectedIndexes()
        if not seleccion:
            QtWidgets.QMessageBox.information(self, "Aviso", "No hay tareas seleccionadas.")
            return

        # Importante: eliminar del final al inicio para no desfasar índices
        for index in sorted(seleccion, key=lambda i: i.row(), reverse=True):
            fila = index.row()
            # Eliminar del modelo
            del self.tareas[fila]
            # Eliminar de la vista
            self.lista.takeItem(fila)

    def limpiar_todo(self):
        if not self.tareas:
            QtWidgets.QMessageBox.information(self, "Aviso", "La lista ya está vacía.")
            return

        respuesta = QtWidgets.QMessageBox.question(
            self,
            "Confirmar",
            "¿Seguro que deseas eliminar TODAS las tareas?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if respuesta == QtWidgets.QMessageBox.Yes:
            self.tareas.clear()
            self.lista.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = TareasApp()
    ventana.show()
    sys.exit(app.exec_())