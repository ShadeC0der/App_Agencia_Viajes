class Paquete:
    """
    Modelo para representar un paquete turístico.
    """
    def __init__(self, id_paquete=None, fecha_inicio=None, fecha_fin=None, precio_total=0.0):
        self.id_paquete = id_paquete
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = precio_total

    def __str__(self):
        return (
            f"ID: {self.id_paquete}, Fecha Inicio: {self.fecha_inicio}, "
            f"Fecha Fin: {self.fecha_fin}, Precio Total: {self.precio_total:.2f}"
        )
