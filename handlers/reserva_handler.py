from controllers.reserva_controller import ReservaController
from models.reservas import Reserva
from datetime import date

class ReservaHandler:
    """
    Handler que empaqueta la interacción del usuario con el controlador de reservas.
    """
    def __init__(self, usuario_autenticado):
        self.controller = ReservaController()
        self.usuario_autenticado = usuario_autenticado

    def menu_reservas(self):
        while True:
            print("\n--- Gestión de Reservas ---")
            print("1. Crear reserva")
            print("2. Listar reservas")
            print("3. Cancelar reserva")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_reserva()
            elif opcion == "2":
                self.listar_reservas()
            elif opcion == "3":
                self.cancelar_reserva()
            elif opcion == "4":
                print("Saliendo del menú de reservas...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def crear_reserva(self):
        """
        Permite al usuario crear una reserva para un paquete turístico.
        """
        id_paquete = input("ID del paquete a reservar: ")

        if not id_paquete.isdigit():
            print("El ID del paquete debe ser un número.")
            return

        reserva = Reserva(
            id_usuario=self.usuario_autenticado.id_usuario,
            id_paquete=int(id_paquete),
            fecha_reserva=date.today()
        )
        self.controller.crear_reserva(reserva)

    def listar_reservas(self):
        """
        Lista todas las reservas del usuario autenticado.
        """
        reservas = self.controller.listar_reservas(self.usuario_autenticado.id_usuario)
        print("\nReservas:")
        for reserva in reservas:
            print(
                f"ID Reserva: {reserva['id_reserva']}, Paquete: {reserva['nombre_paquete']}, "
                f"Fecha Inicio: {reserva['fecha_inicio']}, Fecha Fin: {reserva['fecha_fin']}, "
                f"Precio: {reserva['precio_total']:.2f}, Fecha Reserva: {reserva['fecha_reserva']}"
            )

    def cancelar_reserva(self):
        """
        Permite al usuario cancelar una reserva específica.
        """
        id_reserva = input("ID de la reserva a cancelar: ")

        if not id_reserva.isdigit():
            print("El ID de la reserva debe ser un número.")
            return

        self.controller.cancelar_reserva(int(id_reserva))
    