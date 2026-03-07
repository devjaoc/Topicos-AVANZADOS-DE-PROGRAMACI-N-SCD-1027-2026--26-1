from dataclasses import dataclass, field
# 1) Modelo de dominio
@dataclass
class Tarea:
    descripcion: str
    completada: bool = field(default=False)

    def marcar_completada(self) -> None:
        self.completada = True