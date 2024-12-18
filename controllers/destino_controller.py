from config.database import create_connection
from models.destinos import Destino

class DestinoController:
    """
    Controlador que maneja las operaciones CRUD para destinos.
    """
    def __init__(self):
        self.connection = create_connection()

    def agregar_destino(self, destino):
        query = "INSERT INTO destinos (nombre, descripcion, actividades, costo) VALUES (%s, %s, %s, %s)"
        values = (destino.nombre, destino.descripcion, destino.actividades, destino.costo)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        print("Destino agregado exitosamente.")

    def listar_destinos(self):
        query = "SELECT * FROM destinos"
        cursor = self.connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        destinos = [Destino(*row) for row in resultados]
        return destinos

    def actualizar_destino(self, destino):
        query = "UPDATE destinos SET nombre=%s, descripcion=%s, actividades=%s, costo=%s WHERE id_destino=%s"
        values = (destino.nombre, destino.descripcion, destino.actividades, destino.costo, destino.id_destino)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        print("Destino actualizado exitosamente.")

    def eliminar_destino(self, id_destino):
        query = "DELETE FROM destinos WHERE id_destino=%s"
        cursor = self.connection.cursor()
        cursor.execute(query, (id_destino,))
        self.connection.commit()
        print("Destino eliminado exitosamente.")
