import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="notifications_queue")
channel.basic_consume(
    queue="notifications_queue", on_message_callback=callback, auto_ack=True
)
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
