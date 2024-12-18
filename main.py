# main.py

from handlers.destino_handler import DestinoHandler

"""
Este es el archivo principal del sistema de reservas 'Viajes Aventura'.
"""

def main():
    """
    Función principal que inicia la ejecución del programa.
    """
    print("Bienvenido al sistema de reservas 'Viajes Aventura'.")

    handler = DestinoHandler()
    handler.menu_destinos()

if __name__ == "__main__":
    main()
