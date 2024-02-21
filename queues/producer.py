# Convertir en un flask para poder publicar un EP donde envien eventos

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

notifications_channel = connection.channel()
monitor_channel = connection.channel()

notifications_channel.queue_declare(queue="notifications_queue")
monitor_channel.queue_declare(queue="monitor_queue")


message = "Hello RabbitMQ!"

notifications_channel.basic_publish(
    exchange="", routing_key="notifications_queue", body=message
)
monitor_channel.basic_publish(exchange="", routing_key="monitor_queue", body=message)

print(f" [x] Sent '{message}'")

connection.close()
