from flask import Flask, jsonify
from kafka import KafkaConsumer
from flask import request
import json

application = Flask(__name__)

# Separate Kafka client logic
class KafkaClient:
    def __init__(self, bootstrap_servers, topic):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest'
        )
    
    def consume_messages(self):
        messages = []
        for message in self.consumer:
            messages.append(message.value.decode())
        return messages

# Flask endpoint
@application.route('/process', methods=['GET'])
def process():
    # Kafka configuration
    kafka_bootstrap_servers = 'amq-streams-kafka-bootstrap.kafka-cluster.svc.cluster.local:9092'  # Replace with your Kafka broker address
    kafka_topic = 'quarkus-topic'


    # Initialize Kafka client
    kafka_client = KafkaClient(kafka_bootstrap_servers, kafka_topic)

    # Consume messages from Kafka
    messages = kafka_client.consume_messages()
    print(messages)
    for message in messages:
        print(message.value.decode())
    return jsonify(messages)

if __name__ == "__main__":
    application.run( host='0.0.0.0', port=8080, timeout=120)
