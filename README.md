
# RabbitMQ Priority Queue Example

This project demonstrates how to set up a RabbitMQ priority queue using Docker Compose, with Python scripts for producing and consuming messages.

<div align="center">
   <img src="https://github.com/abhayadevms/rabbitmq/assets/35250410/be3cdc80-df58-44c1-9ff8-32d0d87cd7b6" alt="Screenshot" width="400" height='200'>
</div>

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abhayadevms/rabbitmq.git
   cd rabbitmq
   ```
### Start RabbitMQ and other services using Docker Compose:

Ensure Docker and Docker Compose are installed on your system. Start the services defined in docker-compose.yml:

```bash

docker-compose up -d
```
#### This command launches RabbitMQ in a Docker container, exposing ports 5672 (AMQP) and 15672 (management interface).

### Install Python dependencies:

Install required Python packages specified in requirements.txt using pip:

```bash

pip install -r requirements.txt
```
### Run the Producer:

Use the producer.py script to send messages with different priorities to the RabbitMQ priority queue:

```bash

python producer.py
```
### Run the Consumer:

Use the consumer.py script to consume messages from the RabbitMQ priority queue:

```bash
python consumer.py
```
The consumer script processes incoming messages based on their priority levels, ensuring high-priority messages are handled first.

## RabbitMQ Management UI
To monitor and manage the RabbitMQ server, open your web browser and navigate to:
```
http://localhost:15672
```

Log in with the default credentials:

```bash
Username: rabbitmq
Password: rabbitmq
```
Support
For support or issues, please create an issue on GitHub: https://github.com/abhayadevms/rabbitmq/issues


