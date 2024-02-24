import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="monitor_queue")
channel.basic_consume(
    queue="monitor_queue", on_message_callback=callback, auto_ack=True
)
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
