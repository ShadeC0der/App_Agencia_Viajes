from controllers.destino_controller import DestinoController
from models.destinos import Destino

class DestinoHandler:
    """
    Handler que empaqueta la interacción del usuario con el controlador de destinos.
    """
    def __init__(self):
        self.controller = DestinoController()

    def menu_destinos(self):
        while True:
            print("\n--- Gestión de Destinos ---")
            print("1. Agregar destino")
            print("2. Listar destinos")
            print("3. Actualizar destino")
            print("4. Eliminar destino")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_destino()
            elif opcion == "2":
                self.listar_destinos()
            elif opcion == "3":
                self.actualizar_destino()
            elif opcion == "4":
                self.eliminar_destino()
            elif opcion == "5":
                print("Saliendo del menú de destinos...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def agregar_destino(self):
        nombre = input("Nombre del destino: ")
        descripcion = input("Descripción: ")
        actividades = input("Actividades: ")
        costo = float(input("Costo: "))
        destino = Destino(nombre=nombre, descripcion=descripcion, actividades=actividades, costo=costo)
        self.controller.agregar_destino(destino)

    def listar_destinos(self):
        """
        Lista todos los destinos de la base de datos.
        """
        destinos = self.controller.listar_destinos()
        print("\nLista de Destinos:")
        for destino in destinos:
            print(
                f"ID: {destino.id_destino}, "
                f"Nombre: {destino.nombre}, "
                f"Descripción: {destino.descripcion}, "
                f"Actividades: {destino.actividades}, "
                f"Costo: {destino.costo:.2f}"
            )


    def actualizar_destino(self):
        """
        Permite actualizar los datos de un destino existente.
        Si un campo se deja en blanco, mantiene el valor original.
        """
        id_destino = input("ID del destino a actualizar: ").strip()

        # Verificar que el ID sea válido
        if not id_destino.isdigit():
            print("ID no válido. Debe ser un número.")
            return

        id_destino = int(id_destino)

        # Obtener el destino actual
        destinos = self.controller.listar_destinos()
        destino_actual = next((dest for dest in destinos if dest.id_destino == id_destino), None)

        if not destino_actual:
            print(f"No se encontró un destino con el ID {id_destino}.")
            return

        # Solicitar nuevos valores, con posibilidad de mantener los existentes
        print(f"Nombre actual: {destino_actual.nombre}")
        nombre = input("Nuevo nombre (deja en blanco para mantener): ").strip() or destino_actual.nombre

        print(f"Descripción actual: {destino_actual.descripcion}")
        descripcion = input("Nueva descripción (deja en blanco para mantener): ").strip() or destino_actual.descripcion

        print(f"Actividades actuales: {destino_actual.actividades}")
        actividades = input("Nuevas actividades (deja en blanco para mantener): ").strip() or destino_actual.actividades

        print(f"Costo actual: {destino_actual.costo:.2f}")
        costo_input = input("Nuevo costo (deja en blanco para mantener): ").strip()

        try:
            costo = float(costo_input) if costo_input else destino_actual.costo
        except ValueError:
            print("Entrada no válida para costo. Se mantendrá el valor actual.")
            costo = destino_actual.costo

        # Crear el destino actualizado
        destino_actualizado = Destino(id_destino, nombre, descripcion, actividades, costo)

        # Actualizar en la base de datos
        self.controller.actualizar_destino(destino_actualizado)



    def eliminar_destino(self):
        id_destino = int(input("ID del destino a eliminar: "))
        self.controller.eliminar_destino(id_destino)
