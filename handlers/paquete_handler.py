from controllers.paquete_controller import PaqueteController
from models.paquetes import Paquete

class PaqueteHandler:
    """
    Handler que empaqueta la interacción del usuario con el controlador de paquetes.
    """
    def __init__(self):
        self.controller = PaqueteController()

    def menu_paquetes(self):
        while True:
            print("\n--- Gestión de Paquetes Turísticos ---")
            print("1. Agregar paquete")
            print("2. Listar paquetes")
            print("3. Eliminar paquete")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_paquete()
            elif opcion == "2":
                self.listar_paquetes()
            elif opcion == "3":
                self.eliminar_paquete()
            elif opcion == "4":
                print("Saliendo del menú de paquetes...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def agregar_paquete(self):
        """
        Permite al usuario agregar un paquete turístico y selecciona los destinos asociados.
        """
        nombre = input("Nombre del paquete: ")
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")

        # Seleccionar destinos
        print("Ingrese los IDs de los destinos separados por comas (Ej: 1,2,3):")
        destinos = list(map(int, input().split(",")))

        # Calcular precio total sumando el costo de los destinos seleccionados
        precio_total = self.controller.calcular_precio_total(destinos)

        paquete = Paquete(nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, precio_total=precio_total)
        self.controller.agregar_paquete(paquete, destinos)


    def listar_paquetes(self):
        """
        Lista todos los paquetes turísticos y sus destinos asociados.
        """
        paquetes = self.controller.listar_paquetes()
        print("\nLista de Paquetes:")
        for paquete in paquetes:
            print(
                f"ID: {paquete['id_paquete']}, Nombre: {paquete['nombre']}, "
                f"Fecha Inicio: {paquete['fecha_inicio']}, Fecha Fin: {paquete['fecha_fin']}, "
                f"Precio Total: {paquete['precio_total']:.2f}, "
                f"Destinos: {', '.join(paquete['destinos'])}"
            )

    def eliminar_paquete(self):
        id_paquete = int(input("ID del paquete a eliminar: "))
        self.controller.eliminar_paquete(id_paquete)
