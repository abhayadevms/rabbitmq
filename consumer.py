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

# Declare the queue (same configuration as producer)
channel.queue_declare(queue=QUEUE_NAME, arguments={'x-max-priority': 10})

# Callback function to process messages
def callback(ch, method, properties, body):
    print(f"Received {body.decode()} with priority {properties.priority}")
    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Consume messages from the queue
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
