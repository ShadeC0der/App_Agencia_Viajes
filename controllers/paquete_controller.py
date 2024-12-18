from config.database import create_connection
from models.paquetes import Paquete

class PaqueteController:
    """
    Controlador que maneja las operaciones CRUD para paquetes turísticos.
    """
    def __init__(self):
        self.connection = create_connection()
        
    def calcular_precio_total(self, destinos):
        """
        Calcula el precio total de un paquete sumando los costos de los destinos seleccionados.
        :param destinos: Lista de IDs de destinos.
        :return: Precio total del paquete.
        """
        if not destinos:
            return 0.0

        query = "SELECT SUM(costo) FROM destinos WHERE id_destino IN (%s)" % (
            ",".join(["%s"] * len(destinos))
        )

        cursor = self.connection.cursor()
        cursor.execute(query, destinos)
        resultado = cursor.fetchone()
        return resultado[0] if resultado[0] else 0.0


    def agregar_paquete(self, paquete, destinos):
        """
        Agrega un nuevo paquete a la base de datos y relaciona los destinos seleccionados.
        """
        query_paquete = "INSERT INTO Paquetes (nombre, fecha_inicio, fecha_fin, precio_total) VALUES (%s, %s, %s, %s)"
        values_paquete = (paquete.nombre, paquete.fecha_inicio, paquete.fecha_fin, paquete.precio_total)

        cursor = self.connection.cursor()
        cursor.execute(query_paquete, values_paquete)
        id_paquete = cursor.lastrowid

        # Asociar destinos al paquete
        query_relacion = "INSERT INTO Paquete_Destino (id_paquete, id_destino, fecha_asignacion) VALUES (%s, %s, NOW())"
        for id_destino in destinos:
            cursor.execute(query_relacion, (id_paquete, id_destino))

        self.connection.commit()
        print(f"Paquete '{paquete.nombre}' agregado exitosamente.")


    def listar_paquetes(self):
        """
        Lista todos los paquetes y sus destinos asociados, incluyendo el nombre del paquete.
        """
        query = """
            SELECT p.id_paquete, p.nombre, p.fecha_inicio, p.fecha_fin, p.precio_total, 
                GROUP_CONCAT(d.nombre SEPARATOR ', ') AS destinos
            FROM Paquetes p
            LEFT JOIN Paquete_Destino pd ON p.id_paquete = pd.id_paquete
            LEFT JOIN Destinos d ON pd.id_destino = d.id_destino
            GROUP BY p.id_paquete
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()

        paquetes = []
        for row in resultados:
            id_paquete, nombre, fecha_inicio, fecha_fin, precio_total, destinos = row
            paquetes.append({
                "id_paquete": id_paquete,
                "nombre": nombre,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "precio_total": precio_total,
                "destinos": destinos.split(", ") if destinos else []
            })
        return paquetes



    def eliminar_paquete(self, id_paquete):
        """
        Elimina un paquete y sus relaciones con destinos.
        """
        query = "DELETE FROM Paquetes WHERE id_paquete=%s"
        cursor = self.connection.cursor()
        cursor.execute(query, (id_paquete,))
        self.connection.commit()
        print("Paquete eliminado exitosamente.")
