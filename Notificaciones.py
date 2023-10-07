import time

class Notificaciones:
   contador_id = 0

   def __init__(self):
      Notificaciones.contador_id += 1
      self.id = Notificaciones.contador_id
      self.notificaciones = []

   def obtener_notificaciones(self):
      mensaje = "Ver más+"
      print(f"Notificación : {mensaje}")
      return mensaje