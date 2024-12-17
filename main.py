# main.py

"""
Este es el archivo principal del sistema de reservas 'Viajes Aventura'.
Se utiliza como punto de entrada al programa.
"""

from config.database import create_connection

def main():
    """
    Función principal que inicia la ejecución del programa y prueba la conexión a la base de datos.
    """
    print("Iniciando el sistema de reservas 'Viajes Aventura'...")

    # Probar la conexión a la base de datos
    create_connection()

if __name__ == "__main__":
    main()
