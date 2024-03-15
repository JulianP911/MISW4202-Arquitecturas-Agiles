
## Arquitecturas Ágiles de Software
### Alistamiento Experimento Seguridad

En primer lugar, se debe clonar el repositorio de manera local:

```bash
git clone https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles.git
```

2. Ubicarse en la carpeta "Experimento - Seguridad":

```bash
cd '.\Experimento - Seguridad'
```

En esta carpeta encontrarás tres subcarpetas correspondientes a los componentes autorizador, de registro y de socio. Las funcionalidades de cada uno de ellos son las siguientes:

##### Registro:

- Crear un usuario en la base de datos a partir de un nombre de usuario y una contraseña (la contraseña se almacena encriptada).
- Entregar el hash correspondiente de la contraseña registrada a partir de un nombre de usuario.

##### Autorizador:

- Validar la contraseña a partir de un usuario y una contraseña. Esto se realiza haciendo una solicitud al microservicio de registro y comparando el hash recibido. Si la contraseña es válida, se envía un OTP.
- Verificar la autenticidad de un OTP recibido. Si es válido, se genera y envía un token.
- Validar la autenticidad de un token recibido.

##### Socio:

- Proporcionar información sobre deportistas si el token del usuario es válido. Esta validación se realiza consumiendo el servicio de autenticación.
#### Iniciar los componentes
Instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

Ingresar a la carpeta "Autorizador":

```bash
cd Autorizador
```

Correr el archivo:

```bash
flask run
```

Asegurarse de que está corriendo en el puerto 5000.

En otra terminal ingresar a la carpeta "Registro":

```bash
cd Registro
```

Correr el archivo:

```bash
flask run --port 8080
```

Asegurarse de que está corriendo en el puerto 8080.

En otra terminal ingresar a la carpeta "Socio":

```bash
cd Socio
```

Correr el archivo:

```bash
flask run --port 8000
```

Asegurarse de que está corriendo en el puerto 8000.

#### Realizar las peticiones 
Teniendo los tres componentes activos se ingresa a Postman para lanzar las peticiones personificando un usuario

Las colecciones predefinidas están disponibles en la carpeta `Experimento - Seguridad/Seguridad.postman_collection.json`. Puedes importar estas colecciones en tu instancia de Postman para un acceso rápido a las solicitudes necesarias.
![image](https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles/assets/60227230/44493e3e-c45e-4f1d-8666-4321e8681a72)

#### Video demostrativo

https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles/assets/60227230/3de2bea9-39e7-4a66-96f6-a85fb35e6729


----

---


### Alistamiento Experimento Disponibilidad

En primer lugar, se debe clonar el repositorio de manera local:

```bash
git clone https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles.git
```

1. Bajar la imagen de RabbitMQ a Docker:

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

Asegurarse de que RabbitMQ se encuentra en ejecución.
![image](https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles/assets/60227230/3d910e77-df55-47df-9d79-7a2a654f1087)


2. Ubicarse en la carpeta "Experimento - Disponibilidad":

```bash
cd '.\Experimento - Disponibilidad'
```

En esta carpeta, encontrarás tres subcarpetas correspondientes a la plataforma de mensajería (queues), el monitor (monitor), y el componente de notificaciones (gestor_notificaciones).

Instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

Ingresar a la carpeta "queues":

```bash
cd queues
```

Correr el archivo `producer.py`:

```bash
python producer.py
```

Asegurarse de que está corriendo en el puerto 5000.

![image](https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles/assets/60227230/6a785e36-3c8c-4a5a-b4c8-10d8478de341)

Ingresar a la carpeta "gestor_notificaciones":

```bash
cd gestor_notificaciones
```

Correr el archivo `app.py`:

```bash
flask run
```

Ingresar a la carpeta "monitor":

```bash
cd monitor
```

Correr el archivo `app.py`:

```bash
python app.py
```

Asegurarse de que está corriendo en un puerto distinto al 5000.

![image](https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles/assets/60227230/33212cf5-bdf4-421b-a8cc-7f041ba9c99c)

3. Ingresar a Postman y realizar la petición GET a la siguiente URL:

```bash
http://127.0.0.1:8000/estado
```

Asegurarse de cambiar el puerto si el monitor está corriendo en un puerto distinto.
![image](https://github.com/JulianP911/MISW4202-Arquitecturas-Agiles/assets/60227230/8b429a50-f984-4b8c-9c2a-7e6bc8cc6726)

