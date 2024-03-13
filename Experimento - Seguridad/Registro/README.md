# Flask SQLAlchemy User Authentication

Este es un microservicio que implementa un sistema de registro y autenticación de usuarios utilizando Flask y SQLAlchemy.

## Requisitos

- Python 3.x
- Flask
- SQLAlchemy

## Instalación

1. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:

    ```bash
    Flask run
    ```

2. La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Endpoints

- **Registro de usuario**: `POST /registro`
    - Permite registrar un nuevo usuario enviando un JSON con el nombre de usuario y la contraseña.

- **Autenticación de usuario**: `POST /autenticacion`
    - Permite autenticar a un usuario enviado un JSON con el nombre de usuario y la contraseña, devolviendo un booleano indicando si la autenticación fue exitosa.

## Ejemplo de solicitud

### Registro de usuario

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "usuario", "password": "contraseña"}' http://127.0.0.1:5000/registro
```
### Autenticación de usuario

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "usuario", "password": "contraseña"}' http://127.0.0.1:5000/autenticacion
