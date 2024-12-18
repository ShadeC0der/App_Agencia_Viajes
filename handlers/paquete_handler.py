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
        Permite al usuario agregar un paquete turístico con validaciones de campos obligatorios.
        """
        def obtener_campo_obligatorio(mensaje):
            """
            Solicita un campo obligatorio y no permite continuar hasta que se ingrese un valor válido.
            """
            while True:
                valor = input(f"{mensaje} (obligatorio): ").strip()
                if valor:
                    return valor
                else:
                    print("Este campo es obligatorio. Por favor, ingrese un valor.")

        def obtener_campo_fecha(mensaje):
            """
            Solicita una fecha y no permite continuar hasta que se ingrese una fecha válida en formato YYYY-MM-DD.
            """
            while True:
                valor = input(f"{mensaje} (obligatorio, formato YYYY-MM-DD): ").strip()
                try:
                    # Validar formato de fecha
                    parts = valor.split("-")
                    if len(parts) == 3 and len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2:
                        return valor
                    else:
                        raise ValueError
                except ValueError:
                    print("Debe ingresar una fecha válida en el formato YYYY-MM-DD.")

        def obtener_destinos():
            """
            Solicita los IDs de los destinos asociados y no permite continuar hasta que se ingresen valores válidos.
            """
            while True:
                valor = input("Ingrese los IDs de los destinos separados por comas (Ej: 1,2,3) (obligatorio): ").strip()
                if valor:
                    try:
                        destinos = list(map(int, valor.split(",")))
                        return destinos
                    except ValueError:
                        print("Debe ingresar una lista de IDs numéricos separados por comas.")
                else:
                    print("Debe ingresar al menos un destino.")

        # Solicitar los datos del paquete
        nombre = obtener_campo_obligatorio("Nombre del paquete")
        fecha_inicio = obtener_campo_fecha("Fecha de inicio")
        fecha_fin = obtener_campo_fecha("Fecha de fin")
        destinos = obtener_destinos()

        # Calcular precio total sumando el costo de los destinos seleccionados
        precio_total = self.controller.calcular_precio_total(destinos)

        # Crear el paquete y agregarlo a la base de datos
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
