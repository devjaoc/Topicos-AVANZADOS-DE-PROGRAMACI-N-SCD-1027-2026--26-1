from repository.ListaTareasRespository import ListaTareasRespository
from ui.ConsolaApp import ConsolaApp
# Ejecutar programa
def main():
    lista = ListaTareasRespository()
    app = ConsolaApp(lista)
    app.run()


if __name__ == "__main__":
    main()