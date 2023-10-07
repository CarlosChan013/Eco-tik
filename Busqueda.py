import os

class BusquedaPorCategoria:
    def __init__(self, categoria, directorio):
        self.categoria = categoria
        self.directorio = directorio
    
    def buscar_archivos(self):
        resultados = []
        try:
            for archivo in os.listdir(self.directorio):
                if archivo.endswith('.py'):
                    with open(os.path.join(self.directorio, archivo), 'r') as file:
                        lineas = file.readlines()
                        for linea in lineas:
                            if self.categoria in linea:
                                resultados.append(linea.strip())  # Agrega la línea que contiene la categoría a la lista de resultados
        except FileNotFoundError:
            print(f'Directorio {self.directorio} no encontrado.')
        return resultados

# Ejemplo de uso
if __name__ == "__main__":
    # Crea una instancia de la clase BusquedaPorCategoria para la categoría 'A'
    busqueda_categoria_A = BusquedaPorCategoria('CategoriaA', 'ruta/a/tu/directorio')
    # Realiza la búsqueda en la categoría 'A'
    resultados_categoria_A = busqueda_categoria_A.buscar_archivos()
    # Imprime los resultados encontrados en la categoría 'A'
    print('Resultados en la categoría A:')
    print(resultados_categoria_A)

