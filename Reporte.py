from Categorias import Categorias

categorias = Categorias()

class Reporte:
    contador_id = 0

    def __init__(self, nombre_del_reporte, detalles, evidencias, categoria, ubicacion):
        Reporte.contador_id += 1
        self.id = Reporte.contador_id
        self.nombre_del_reporte = nombre_del_reporte
        self.detalles = detalles
        self.evidencias = evidencias
        self.categoria = categoria
        self.ubicacion = ubicacion

# Un diccionario para almacenar los reportes por categoría
reportes_por_categoria = {
    "Contaminación del agua": [],
    "Deforestación": [],
    "Contaminación del aire": []
}

# Función para crear un reporte y agregarlo a la categoría correspondiente
def crear_reporte(usuario_actual, categorias):
    if usuario_actual.tipo_usuario == 'Ciudadano':
        nombre_del_reporte = input("Nombre del reporte: ")
        detalles = input("Detalles del reporte: ")
        evidencias = input("Evidencias: ")

        print("Categorías disponibles:")
        categorias.mostrar_categorias()
        categoria = categorias.elegir_categoria()

        ubicacion = input("Ubicación: ")

        nuevo_reporte = Reporte(nombre_del_reporte, detalles, evidencias, categoria, ubicacion)
        reportes_por_categoria[categoria].append(nuevo_reporte)

        print("Reporte creado con éxito.")

# Función para mostrar los reportes de una categoría específica

# Función para mostrar los reportes de una categoría específica
def mostrar_reportes_por_categoria():
    while True:
        print("\n-- CATEGORIAS --")
        categorias.mostrar_categorias()
        print("0. Salir")
        eleccion = input("Seleccione una categoría (1-3) o 0 para salir: ")
        if eleccion == "0":
            break
        elif eleccion in categorias.categorias_disponibles:
            categoria_seleccionada = eleccion
            reportes = reportes_por_categoria[categoria_seleccionada]
            if reportes:
                print(f"Reportes en la categoría '{categoria_seleccionada}':")
                for reporte in reportes:
                    print(f"Nombre del reporte: {reporte.nombre_del_reporte}")
                    print(f"Detalles: {reporte.detalles}")
                    print(f"Evidencias: {reporte.evidencias}")
                    print(f"Ubicación: {reporte.ubicacion}")
                    print("\n")
            else:
                print(f"No hay reportes en la categoría '{categoria_seleccionada}'.")
        else:
            print("Opción no válida. Intente de nuevo.")