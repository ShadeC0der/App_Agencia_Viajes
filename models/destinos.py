# models/destinos.py

class Destino:
    """
    Modelo para representar un destino turístico.
    """
    def __init__(self, id_destino=None, nombre="", descripcion="", actividades="", costo=0.0):
        self.id_destino = id_destino
        self.nombre = nombre
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo

    def __str__(self):
        return f"ID: {self.id_destino}, Nombre: {self.nombre}, Costo: {self.costo}"
