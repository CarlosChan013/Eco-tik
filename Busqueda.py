class SistemaReportes:
    def __init__(self):
        self.reportes = {
            "CategoriaA": ["Reporte1", "Reporte2"],
            "CategoriaB": ["Reporte3", "Reporte4"]
            
        }

    def buscar_por_categoria(self, categoria):
        if categoria in self.reportes:
            return self.reportes[categoria]
        else:
            return []

    def buscar_por_reporte(self, nombre_reporte):
        resultados = []
        for categoria, reportes in self.reportes.items():
            if nombre_reporte in reportes:
                resultados.append((categoria, nombre_reporte))
        return resultados

if __name__ == "__main__":
    sistema = SistemaReportes()

    tipo_busqueda = input("¿Qué tipo de búsqueda desea realizar? (categoria/reporte): ")

    if tipo_busqueda.lower() == "categoria":
        categoria = input("Por favor, introduzca la categoría que desea buscar: ")
        resultados = sistema.buscar_por_categoria(categoria)
        print("Reportes encontrados en la categoría {}: {}".format(categoria, resultados))
    elif tipo_busqueda.lower() == "reporte":
        nombre_reporte = input("Por favor, introduzca el nombre del reporte que desea buscar: ")
        resultados = sistema.buscar_por_reporte(nombre_reporte)
        if resultados:
            print("Reporte(s) encontrado(s):")
            for categoria, reporte in resultados:
                print("- Categoría: {}, Reporte: {}".format(categoria, reporte))
        else:
            print("No se encontraron reportes con ese nombre.")
    else:
        print("Opción de búsqueda no válida. Por favor, seleccione 'categoria' o 'reporte'.")
