from flask import Flask, jsonify
from kafka import KafkaConsumer
from flask import request
import json

app = Flask(__name__)

# Separate Kafka client logic
class KafkaClient:
    def __init__(self, bootstrap_servers, topic):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

    def consume_messages(self):
        messages = []
        for message in self.consumer:
            messages.append(message.value)
        return messages

# Flask endpoint
@app.route('/process', methods=['GET'])
def process():
    # Kafka configuration
    kafka_bootstrap_servers = 'amq-streams-kafka-bootstrap.kafka-cluster.svc.cluster.local:9092'  # Replace with your Kafka broker address
    kafka_topic = 'quarkus-topic'

    # Initialize Kafka client
    kafka_client = KafkaClient(kafka_bootstrap_servers, kafka_topic)

    # Consume messages from Kafka
    messages = kafka_client.consume_messages()
    for message in messages:
        print(message.value.decode())
    # return jsonify(messages)
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
