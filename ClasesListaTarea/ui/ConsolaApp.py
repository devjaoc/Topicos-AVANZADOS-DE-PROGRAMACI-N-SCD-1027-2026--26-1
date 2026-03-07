from repository.ListaTareasRespository import ListaTareasRespository
from model.OpcionMenu import OpcionMenu
class ConsolaApp:
    def __init__(self, lista: ListaTareasRespository) -> None:
        self.lista = lista

    def mostrar_menu(self) -> None:
        print("\n===== LISTA DE TAREAS =====")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("===========================")

    def pedir_opcion(self) -> OpcionMenu | None:
        opcion = input("Elige una opción: ").strip()
        try:
            return OpcionMenu(opcion)
        except ValueError:
            return None

    def agregar_tarea(self) -> None:
        tarea = input("Escribe la nueva tarea: ").strip()
        if self.lista.agregar(tarea):
            print("✔ Tarea agregada.")
        else:
            print("❌ No puedes agregar una tarea vacía.")

    def mostrar_tareas(self) -> None:
        if self.lista.esta_vacia():
            print("No hay tareas registradas.")
            return

        print("\n--- TAREAS ---")
        for i, t in enumerate(self.lista.todas(), start=1):
            estado = "✔ Completada" if t.completada else "⏳ Pendiente"
            print(f"{i}. {t.descripcion}  --> {estado}")

    def completar_tarea(self) -> None:
        self.mostrar_tareas()
        if self.lista.esta_vacia():
            return
        try:
            num = int(input("Número de tarea a completar: "))
        except ValueError:
            print("❌ Número inválido.")
            return

        if self.lista.completar(num):
            print("✔ Tarea marcada como completada.")
        else:
            print("❌ Número inválido.")

    def eliminar_tarea(self) -> None:
        self.mostrar_tareas()
        if self.lista.esta_vacia():
            return
        try:
            num = int(input("Número de tarea a eliminar: "))
        except ValueError:
            print("❌ Número inválido.")
            return

        if self.lista.eliminar(num):
            print("🗑 Tarea eliminada.")
        else:
            print("❌ Número inválido.")

    def run(self) -> None:
        while True:
            self.mostrar_menu()
            opcion = self.pedir_opcion()

            if opcion == OpcionMenu.AGREGAR:
                self.agregar_tarea()
            elif opcion == OpcionMenu.MOSTRAR:
                self.mostrar_tareas()
            elif opcion == OpcionMenu.COMPLETAR:
                self.completar_tarea()
            elif opcion == OpcionMenu.ELIMINAR:
                self.eliminar_tarea()
            elif opcion == OpcionMenu.SALIR:
                print("Saliendo del programa...")
                break
            else:
                print("❌ Opción inválida, intenta de nuevo.")

