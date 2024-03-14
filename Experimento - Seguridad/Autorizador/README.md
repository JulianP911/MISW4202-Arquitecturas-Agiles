# Flask SQLAlchemy User Authentication

Este es un microservicio que implementa un sistema de registro y autenticación de usuarios utilizando Flask y SQLAlchemy.

## Requisitos

- Python 3.x
- Flask
- requests
- jwt
- bcrypt
- PyJWT

## Instalación

1. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:

    ```bash
    flask run
    ```

2. La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Endpoints

- **Inicio de sesión**: `POST /login`
    - Permite iniciar sesión de un usuario enviando un JSON con el nombre de usuario y la contraseña.

- **Verifiacar OTP**: `POST /verify_otp`
    - Permite verificar que el otp proporcionado por parte del usuario es valido o invalido.

- **Verificar token**: `GET /verify_token`
    - Permite verificar que el token de acceso proporcionado por parte del usuario es valido o invalido.

## Ejemplo de solicitud

### Inicio de sesión

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "usuario", "password": "contraseña"}' http://127.0.0.1:5000/login
```

### Verifiacar OTP

```bash
curl -X POST -H "Content-Type: application/json" -d '{"otp": "9281"}' http://127.0.0.1:5000/verify_otp
```

### Verificar token

```bash
curl -X POST -H "Content-Type: application/json" -d '{"token": "iJSAON392NSNmsna"}' http://127.0.0.1:5000/verify_token
```