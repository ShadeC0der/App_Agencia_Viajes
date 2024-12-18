class Usuario:
    """
    Modelo para representar un usuario del sistema.
    """
    def __init__(self, id_usuario=None, nombre="", correo="", contraseña=""):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def __str__(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}, Correo: {self.correo}"
