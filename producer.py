import pika

RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'priority_queue'

# Connect to RabbitMQ
credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare a priority queue with maximum priority 10
channel.queue_declare(queue=QUEUE_NAME, arguments={'x-max-priority': 10})

# Function to send messages with different priorities
def send_message(message, priority):
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        body=message,
        properties=pika.BasicProperties(priority=priority)
    )
    print(f"Sent {message} with priority {priority}")

# Send messages with different priorities
send_message('Low priority message', priority=1)
send_message('High priority message', priority=10)
send_message('Medium priority message', priority=5)

# Close the connection
connection.close()
