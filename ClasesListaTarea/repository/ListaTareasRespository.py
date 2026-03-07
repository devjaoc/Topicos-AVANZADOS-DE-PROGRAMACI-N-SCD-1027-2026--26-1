from typing import List
from model.Tarea import Tarea
# 2) Lógica de negocio (gestión de tareas)
class ListaTareasRespository:
    def __init__(self) -> None:
        self._tareas: List[Tarea] = []

    def agregar(self, descripcion: str) -> bool:
        descripcion = descripcion.strip()
        if not descripcion:
            return False
        self._tareas.append(Tarea(descripcion))
        return True

    def todas(self) -> List[Tarea]:
        return list(self._tareas)  # copia superficial para no exponer la lista interna

    def completar(self, indice_1_base: int) -> bool:
        idx = indice_1_base - 1
        if 0 <= idx < len(self._tareas):
            self._tareas[idx].marcar_completada()
            return True
        return False

    def eliminar(self, indice_1_base: int) -> bool:
        idx = indice_1_base - 1
        if 0 <= idx < len(self._tareas):
            self._tareas.pop(idx)
            return True
        return False

    def esta_vacia(self) -> bool:
        return len(self._tareas) == 0
