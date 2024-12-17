# main.py

"""
Este es el archivo es el que configura la conexion a la base de datos
"""

import mysql.connector

def create_connection():
    """
    Paramentros para configurar la base de datos
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",          # Dirección del servidor
            user="root",               # Usuario de MySQL
            password="tu_contraseña",  # Contraseña de MySQL
            database="agencia_viajes"  # Nombre de la base de datos
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
