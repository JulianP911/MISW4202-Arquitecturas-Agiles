from flask import Flask, jsonify
import requests
import pika

app = Flask(__name__)

# Configuración de RabbitMQ
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = "monitor_queue"

# Conexión a la cola de RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
)
channel = connection.channel()


# Ruta para consultar el estado
@app.route("/estado", methods=["GET"])
def get_estado():
    print("Se recibe peticion de consulta de estado")
    jsonPeticion = {"message": "prueba", "queue": "notifications"}

    # Envío de 10 peticiones POST al microservicio
    urls = ["http://localhost:5000/send_message" for _ in range(10)]
    respuestas = [requests.post(url, json=jsonPeticion) for url in urls]
    print("se enviaron las peticiones")
    # Recepción de resultados de la cola RabbitMQ
    resultados = []
    for _ in range(10):
        method, properties, body = channel.basic_get(RABBITMQ_QUEUE)
        if body:
            print("Body respuestas: ",body)
            resultados.append(int(body.decode().split(",")[1].split(")")[0]))

    # Codigos parametrizables que son considerados error
    codigosDeRespuestaNoSaludables=[400]
    # maxima cantidad de peticiones que se pueden recibir no saludables para determinar si esta disponible o no el servicio
    maximaCantidadDePeticionesNoSaludablesPermitidas = 1
    contador = 0
    for resultado in resultados:
        if resultado in codigosDeRespuestaNoSaludables:
            contador+=1
    if contador > maximaCantidadDePeticionesNoSaludablesPermitidas:
        return jsonify({"estado": "indisponible"})
    else:
        return jsonify({"estado": "disponible"})


if __name__ == "__main__":
    app.run(port=8000)
