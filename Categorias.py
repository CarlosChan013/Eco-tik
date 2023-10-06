class Categorias:
    categorias_disponibles = ["Contaminación del agua", "Deforestación", "Contaminación del aire"]

    def mostrar_categorias(self):
        print("Categorías disponibles:")
        for i, categoria in enumerate(Categorias.categorias_disponibles, start=1):
            print(f"{i}. {categoria}")

    def elegir_categoria(self):
        while True:
            try:
                opcion = int(input("Seleccione una categoría (1-3): "))
                if 1 <= opcion <= 3:
                    return Categorias.categorias_disponibles[opcion - 1]
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Ingrese un número válido.")
    # Función para mostrar las categorías
def visualizar_categorias():
    print("\n-- CATEGORIAS --")
    print(" Contaminación del agua")
    print(" Deforestación")
    print(" Contaminación del aire")
    print("1. Salir")