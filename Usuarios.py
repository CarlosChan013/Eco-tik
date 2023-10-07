from Reporte import crear_reporte,mostrar_reportes_por_categoria
from Categorias import visualizar_categorias
from Notificaciones import Notificaciones
notificador = Notificaciones()

# Definimos la clase User 
class User:
    contador_id = 0
    def __init__(self, nombre, apellido, password, tipo_usuario):
        User.contador_id += 1
        self.id = User.contador_id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.tipo_usuario = tipo_usuario

usuarios = {}  # Diccionario para almacenar los usuarios registrados
# Logica para realizar el Inicio de Sesión si escogen la opción 1
def iniciar_sesion():
    print("Iniciar sesión")
    nombre = input("Introduce tu nombre: ")
    password = input("Introduce tu contraseña: ")

    if nombre in usuarios:
        usuario = usuarios[nombre]
        if usuario.password == password:
            usuario.sesion = True
            print("Sesión iniciada con éxito.")
            return usuario
        else:
            print("Contraseña incorrecta.")
            return None
    else:
        print("Usuario no encontrado.")
# Logica para realizar el registro de usuarios si escogen la opción 2
def registrar_usuario():
    print(" Bienvenido a registro de ciudadano ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    password = input("Contraseña: ")
    tipo_usuario = "Ciudadano"  # Asegúrate de que el tipo de usuario sea "Ciudadano"
    usuario = User(nombre, apellido, password, tipo_usuario)  # Crea una instancia de la clase User
    usuarios[nombre] = usuario
    print("Usuario registrado con éxito.")

def menu_ciudadano(usuario_actual, categorias):
    while True:
        print("\n-- Menú Ciudadano --")
        print("1. Crear reporte")
        print("2. Categorías")
        print("3. Buscar")
        print("4. Mis notificaciones")
        print("5. Salir")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            crear_reporte(usuario_actual, categorias) 
    #se despliega solo un menu para ver las categorias que hay con 1 puede salir y volver al menu ciudadano
        if eleccion == "2":
            visualizar_categorias()
    #logica para realizar una busqueda
        if eleccion == "3":
            mostrar_reportes_por_categoria()
    # Verificar y mostrar notificaciones
        elif eleccion == "4":
            notificador.obtener_notificaciones()
        elif eleccion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
# si el rol es agente puede visualizar dicho reporte Falta la logica
def visualizar_usuarios():
    pass