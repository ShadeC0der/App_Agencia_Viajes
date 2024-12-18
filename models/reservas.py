class Reserva:
    """
    Modelo para representar una reserva realizada por un usuario.
    """
    def __init__(self, id_reserva=None, id_usuario=None, id_paquete=None, fecha_reserva=None):
        self.id_reserva = id_reserva
        self.id_usuario = id_usuario
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva

    def __str__(self):
        return (
            f"ID Reserva: {self.id_reserva}, ID Usuario: {self.id_usuario}, "
            f"ID Paquete: {self.id_paquete}, Fecha Reserva: {self.fecha_reserva}"
        )
