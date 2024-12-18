from config.database import create_connection
from models.reservas import Reserva

class ReservaController:
    """
    Controlador que maneja las operaciones CRUD para reservas.
    """
    def __init__(self):
        self.connection = create_connection()

    def crear_reserva(self, reserva):
        """
        Crea una nueva reserva en la base de datos.
        """
        query = "INSERT INTO reservas (id_usuario, id_paquete, fecha_reserva) VALUES (%s, %s, %s)"
        values = (reserva.id_usuario, reserva.id_paquete, reserva.fecha_reserva)

        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        print("Reserva creada exitosamente.")

    def listar_reservas(self, id_usuario):
        """
        Lista todas las reservas de un usuario.
        """
        query = """
            SELECT r.id_reserva, r.fecha_reserva, p.nombre, p.fecha_inicio, p.fecha_fin, p.precio_total
            FROM reservas r
            JOIN paquetes p ON r.id_paquete = p.id_paquete
            WHERE r.id_usuario = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (id_usuario,))
        resultados = cursor.fetchall()

        reservas = []
        for row in resultados:
            id_reserva, fecha_reserva, nombre_paquete, fecha_inicio, fecha_fin, precio_total = row
            reservas.append({
                "id_reserva": id_reserva,
                "fecha_reserva": fecha_reserva,
                "nombre_paquete": nombre_paquete,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "precio_total": precio_total
            })
        return reservas

    def cancelar_reserva(self, id_reserva):
        """
        Cancela una reserva específica.
        """
        query = "DELETE FROM reservas WHERE id_reserva=%s"
        cursor = self.connection.cursor()
        cursor.execute(query, (id_reserva,))
        self.connection.commit()
        print("Reserva cancelada exitosamente.")
