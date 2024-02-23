from gestor_notificaciones import create_app
from .modelos import db, Notificacion
from flask_restful import Api
from .vistas import VistaNotificaciones
import pika
import random
from gestor_notificaciones.logger import setup_logger

logger = setup_logger()
app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaNotificaciones, '/notificaciones')

def callback(ch, method, properties, body):
    random_decimal_within_range = random.uniform(0, 9)
    if random_decimal_within_range < 2:
        logger.info('El servicio de notificaciones no esta disponible en este momento. - Resupesta 400')
        ans= ('El servicio de notificaciones no esta disponible en este momento.', 400)
    else:
        logger.info('El servicio de notificaciones esta disponible en este momento. - Resupesta 200')
        ans=('El servicio de notificaciones esta disponible en este momento.', 200)
    ch.basic_publish(exchange="", routing_key="monitor_queue", body=str(ans))
    print(f" [x] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="notifications_queue")
channel.basic_consume(
    queue="notifications_queue", on_message_callback=callback, auto_ack=True
)
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
