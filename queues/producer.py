from flask import Flask, jsonify, request
import pika

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Get the message from the POST request data
        message = request.get_data(as_text=True)

        # Establish RabbitMQ connection
        # connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq-3.onrender.com")) 
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        notifications_channel = connection.channel()
        monitor_channel = connection.channel()

        # Declare queues
        notifications_channel.queue_declare(queue="notifications_queue")
        monitor_channel.queue_declare(queue="monitor_queue")

        # Publish the message to queues
        notifications_channel.basic_publish(
            exchange="", routing_key="notifications_queue", body=message
        )
        monitor_channel.basic_publish(exchange="", routing_key="monitor_queue", body=message)

        print(f" [x] Sent '{message}'")

        # Close the RabbitMQ connection
        connection.close()

        return jsonify({"status": "success", "message": f"Message '{message}' sent successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
