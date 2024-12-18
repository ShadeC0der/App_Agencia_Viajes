from handlers.destino_handler import DestinoHandler
from handlers.paquete_handler import PaqueteHandler

"""
Este es el archivo principal del sistema de reservas 'Viajes Aventura'.
"""

def main():
    """
    Función principal que inicia la ejecución del programa.
    """
    print("Bienvenido al sistema de reservas 'Viajes Aventura'.")
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Destinos")
        print("2. Gestión de Paquetes Turísticos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            destino_handler = DestinoHandler()
            destino_handler.menu_destinos()
        elif opcion == "2":
            paquete_handler = PaqueteHandler()
            paquete_handler.menu_paquetes()
        elif opcion == "3":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
