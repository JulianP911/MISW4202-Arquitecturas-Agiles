from flask import Flask, jsonify, request
import pika

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
          # Get the JSON data from the POST request
        data = request.get_json()
        # Extract message and queue from the JSON data
        message = data.get("message", "")
        queue = data.get("queue", "")
        # Publish the message to the specified queue
        if queue == "notifications":
            print("peticion de notifications")
            notifications_channel.basic_publish(exchange="", routing_key="notifications_queue", body=message)
        elif queue == "monitor":
            print("peticion de monitor")
            monitor_channel.basic_publish(exchange="", routing_key="monitor_queue", body=message)
        else:
            raise ValueError(f"Invalid queue name: {queue}")
       
        print(f" [x] Sent '{message}' to {queue}")


        return jsonify({"status": "success", "message": f"Message '{message}' sent successfully to '{queue}'"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
     # Establish RabbitMQ connection
    try:
        # connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq-3.onrender.com")) 
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        notifications_channel = connection.channel()
        monitor_channel = connection.channel()

        # Declare queues
        notifications_channel.queue_declare(queue="notifications_queue")
        monitor_channel.queue_declare(queue="monitor_queue")

        app.run(debug=True)
    except KeyboardInterrupt:
        # Close the RabbitMQ connection
        connection.close()
