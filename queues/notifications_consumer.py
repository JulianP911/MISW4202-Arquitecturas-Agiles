import pika
import requests
import json
def callback(ch, method, properties, body):
    dictToSend={"tipo_notificacion": "EVENTOS", "titulo": "Mucha lluvia en carretera", "descripcion": "Ten cuidado al estar montando cicla"}
    res = requests.post('http://localhost:8000/notificaciones', data=json.dumps(dictToSend), headers={'Content-Type': 'application/json'})
    print ('response from server:',res.text)
    print(f" [x] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="notifications_queue")
channel.basic_consume(
    queue="notifications_queue", on_message_callback=callback, auto_ack=True
)
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
