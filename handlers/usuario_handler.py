import re
from controllers.usuario_controller import UsuarioController
from models.usuarios import Usuario

class UsuarioHandler:
    """
    Handler que empaqueta la interacción del usuario con el controlador de usuarios.
    """
    def __init__(self):
        self.controller = UsuarioController()

    def menu_usuarios(self):
        while True:
            print("\n--- Gestión de Usuarios ---")
            print("1. Registrarse")
            print("2. Iniciar Sesión")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                usuario = self.iniciar_sesion()
                if usuario:
                    return usuario
            elif opcion == "3":
                print("Saliendo del menú de usuarios...")
                return None
            else:
                print("Opción no válida. Intente nuevamente.")

    def registrar_usuario(self):
        nombre = input("Nombre del usuario: ")
        correo = input("Correo del usuario: ")

        # Validar contraseña segura
        contraseña = self.obtener_contraseña_segura()

        usuario = Usuario(nombre=nombre, correo=correo, contraseña=contraseña)
        self.controller.registrar_usuario(usuario)

    def iniciar_sesion(self):
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")

        usuario = self.controller.autenticar_usuario(correo, contraseña)
        if usuario:
            print(f"Bienvenido, {usuario.nombre}.")
            return usuario
        else:
            print("Credenciales incorrectas. Intente nuevamente.")
            return None

    def obtener_contraseña_segura(self):
        """
        Solicita al usuario una contraseña que cumpla con los requisitos mínimos de seguridad.
        """
        while True:
            contraseña = input("Contraseña (mínimo 8 caracteres, al menos un número, una mayúscula y un carácter especial): ")
            if self.validar_contraseña(contraseña):
                return contraseña
            else:
                print("La contraseña no cumple con los requisitos mínimos. Intente nuevamente.")

    @staticmethod
    def validar_contraseña(contraseña):
        """
        Valida si una contraseña cumple con los requisitos mínimos.
        """
        if len(contraseña) < 8:
            return False
        if not re.search(r"[A-Z]", contraseña):
            return False
        if not re.search(r"[0-9]", contraseña):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
            return False
        return True
