# Proyecto Viajes Aventura

## Descripción
Sistema de reservas para una agencia de viajes llamado **"Viajes Aventura"**. Implementa un sistema completo utilizando **Python**, **programación orientada a objetos (POO)**, y la arquitectura **MVC**. Permite gestionar destinos, paquetes turísticos, usuarios y reservas con conexión a una base de datos **MySQL**.

## Funcionalidades
- **Gestor de Destinos**: Crear, leer, actualizar y eliminar destinos.
- **Gestor de Paquetes**: Crear y administrar paquetes turísticos con destinos seleccionados.
- **Autenticación de Usuarios**: Registro seguro y autenticación con contraseñas cifradas.
- **Sistema de Reservas**: Permite a los usuarios realizar y gestionar reservas.

## Tecnologías Utilizadas
- **Lenguaje**: Python
- **Base de Datos**: MySQL
- **Bibliotecas**:
  - mysql-connector-python
  - bcrypt (para hashing de contraseñas)
- **Patrón de Diseño**: MVC (Modelo-Vista-Controlador)

## Estructura del Proyecto

```
/App_Agencia_Viajes/
    ├── config/                     # Configuraciones del proyecto (Ej: Base de Datos)
        └── database.py             # Archivo de conexión a la base de datos.
    ├── models/                     # Modelos que encapsulan datos y lógica de entidades.
    ├── controllers/                # Controladores con la lógica de funcionalidades.
    ├── views/                      # Vistas para la interacción (Ej: Menús).
    ├── handlers/                   # Permiten manejar lógica específica o errores.
    ├── utils/                      # Utilidades generales (Ej: hashing, validaciones).
    ├── main.py                     # Archivo principal que inicia el proyecto.
    ├── README.md                   # Documentación breve del proyecto.
    └── requirements.txt            # Requerimientos del proyecto (dependencias).
```

## Integrantes del Equipo
1. **Christian Gutiérrez** 
2. **Benjamín Velásquez**
3. **Ismael Aguila** 
4. **Jonathan Gallardo** 