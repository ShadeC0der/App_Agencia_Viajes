from handlers.usuario_handler import UsuarioHandler
from handlers.destino_handler import DestinoHandler
from handlers.paquete_handler import PaqueteHandler
from handlers.reserva_handler import ReservaHandler

def main():
    """
    Función principal que inicia la ejecución del programa.
    """
    print("Bienvenido al sistema de reservas 'Viajes Aventura'.")

    usuario_handler = UsuarioHandler()
    usuario_autenticado = None

    while not usuario_autenticado:
        usuario_autenticado = usuario_handler.menu_usuarios()

    # Menú principal una vez autenticado
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Destinos")
        print("2. Gestión de Paquetes Turísticos")
        print("3. Gestión de Reservas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            destino_handler = DestinoHandler()
            destino_handler.menu_destinos()
        elif opcion == "2":
            paquete_handler = PaqueteHandler()
            paquete_handler.menu_paquetes()
        elif opcion == "3":
            reserva_handler = ReservaHandler(usuario_autenticado)
            reserva_handler.menu_reservas()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
