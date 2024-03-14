# Flask SQLAlchemy User Authentication

Este es un microservicio que implementa el servicio de información asociado al socio deportologo utilizando Flask y SQLAlchemy.

## Requisitos

- Python 3.x
- Flask
- SQLAlchemy
- Requests

## Instalación

1. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:

    ```bash
    flask run -p 5002
    ```

2. La aplicación estará disponible en `http://127.0.0.1:5002/`.

## Endpoints

- **Obtener la información de los deportistas**: `POST /deportistas`
    - Permite obtener la información asociada de los deportistas que tiene a cargo el socio deportologo con el token de acceso.

## Ejemplo de solicitud

### Obtener la información de los deportistas

```bash
curl -X POST -H "Content-Type: application/json" -d '{"toke": "iJSAON392NSNmsna"}' http://127.0.0.1:5002/deportistas
```