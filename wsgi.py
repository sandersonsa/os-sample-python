from flask import Flask, jsonify
from kafka import KafkaConsumer
from flask import request
from minio import Minio
import json

application = Flask(__name__)

# Flask endpoint
@application.route('/process', methods=['GET'])
def process():
    # Kafka configuration
    # kafka_bootstrap_servers = 'amq-streams-kafka-bootstrap.kafka-cluster.svc.cluster.local:9092'  # Replace with your Kafka broker address
    # kafka_topic = 'quarkus-topic'

    # consumer = KafkaConsumer(kafka_topic, bootstrap_servers=[kafka_bootstrap_servers])
    # for message in consumer:
    #     print(message.value.decode())
        
    # Create a MinIO client
    minio_client = Minio('minio-service.minio.svc.cluster.local:9000',
        access_key='efSZjPmIfTtGUH7NKP4H',
        secret_key='m5CwKsaFxXMxYwZHH3wu6gPlCf0Q7WrNWxkcdA97',
        secure=False  # Set to True if using HTTPS   
    )
    
    bucket_name = 'logs'
    object_name = 'kafka-quickstart-processor/kafka-quickstart-processor-1.txt'
    temp_file = '/tmp/kafka-quickstart-processor-1.txt'

    # Get the object from the bucket
    # result = minio_client.fget_object(bucket_name, object_name, temp_file)
    response = minio_client.get_object('logs', 'kafka-quickstart-processor/kafka-quickstart-processor-1.txt')

    # Read the file line by line
    # for line in response.stream(decode_content=True).splitlines():
    #     print(line.decode('utf-8'))  # Print each line
        
    # Read line by line
    for line in response['Body'].iter_lines():
        line = line.decode('utf-8')
        print(line)  # Output the line to the console

    response.close()
    response.release_conn()

    # Initialize Kafka client
    # kafka_client = KafkaClient(kafka_bootstrap_servers, kafka_topic)

    # Consume messages from Kafka
    # messages = kafka_client.consume_messages()
    # print(messages)
    # for message in messages:
    #     print(message.value.decode())
    # return jsonify(messages)
    return "Hello World!"

if __name__ == "__main__":
    application.run( host='0.0.0.0', port=8080 )
