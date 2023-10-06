from Usuarios import User,usuarios


class Agente_del_gobierno(User):
    def __init__(self, nombre, apellido, password, tipo_usuario):
        super().__init__(nombre, apellido, password, tipo_usuario)
# Registro si el rol es agente
def registrar_agente_del_gobierno():
        print(" Bienvenido a registro de agente del gobierno")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        password = input("Contraseña: ")
        tipo_usuario = "Agente"
        usuario = User(nombre, apellido, password, tipo_usuario)  # Crea una instancia de la clase User
        usuarios[nombre] = usuario
        print("Usuario registrado con éxito.")
def menu_agente_gobierno():
    while True:
        print("\n-- Menú Agente del Gobierno --")
        print("1. Ver reportes")
        print("2. Ver usuarios")
        print("3. Categorías")
        print("4. Buscar")
        print("5. Salir")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
