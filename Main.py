from Usuarios import iniciar_sesion, registrar_usuario, menu_ciudadano
from Agentes import registrar_agente_del_gobierno, menu_agente_gobierno
from Categorias import Categorias
if __name__ == "__main__":
    usuario_actual = None
    categorias = Categorias()
    def menu_principal():
        global usuario_actual

        while True:
            print("\n-- Menú Principal --")
            print("1. Iniciar Sesión")
            print("2. Registrarse como Ciudadano")
            print("3. Registrarse como Agente del Gobierno")
            print("4. Salir")
            eleccion = input("Seleccione una opción: ")

            if eleccion == "1":
                usuario_actual = iniciar_sesion()
                if usuario_actual and usuario_actual.tipo_usuario == "Ciudadano":
                    menu_ciudadano(usuario_actual, categorias)  # Pasa usuario_actual como argumento
                elif usuario_actual and usuario_actual.tipo_usuario == "Agente":
                    menu_agente_gobierno()  # Llama al menú de agente del gobierno
            elif eleccion == "2":
                registrar_usuario()       
            elif eleccion == "3":
                registrar_agente_del_gobierno() 
            elif eleccion == "4":
                print("Hasta luego.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    menu_principal()