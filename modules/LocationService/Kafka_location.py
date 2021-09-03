from kafka import KafkaConsumer
from json import loads, dumps
import logging
import requests

CONNECTION_SERVICE_ENDPOINT = "http://connection-api:5000/"

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

def readMessage():
    consumer = KafkaConsumer(
    'visits',
     bootstrap_servers=['kafkacluster.default.svc.cluster.local:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='visit-group1',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        logger.warning(f"read data from Kafka: {message.value}")
        location = message.value
        new_location = requests.post(CONNECTION_SERVICE_ENDPOINT + "api/locations", json=location)
           #new_location=LocationService.create(message.value)
        logger.warning("finished writing to DB")

readMessage()
