from config.database import create_connection
from models.usuarios import Usuario
import bcrypt

class UsuarioController:
    """
    Controlador que maneja las operaciones CRUD y autenticación para usuarios.
    """
    def __init__(self):
        self.connection = create_connection()

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario con contraseña segura hasheada.
        """
        hashed_password = bcrypt.hashpw(usuario.contraseña.encode('utf-8'), bcrypt.gensalt())
        query = "INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)"
        values = (usuario.nombre, usuario.correo, hashed_password)

        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        print("Usuario registrado exitosamente.")

    def autenticar_usuario(self, correo, contraseña):
        """
        Autentica un usuario verificando el correo y la contraseña.
        """
        query = "SELECT id_usuario, nombre, correo, contraseña FROM usuarios WHERE correo=%s"
        cursor = self.connection.cursor()
        cursor.execute(query, (correo,))
        resultado = cursor.fetchone()

        if resultado:
            id_usuario, nombre, correo_db, hashed_password = resultado
            if bcrypt.checkpw(contraseña.encode('utf-8'), hashed_password.encode('utf-8')):
                return Usuario(id_usuario, nombre, correo_db)
        return None
