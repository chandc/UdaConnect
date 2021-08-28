import logging

from confluent_kafka import Producer
import json
import socket


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

conf = {'bootstrap.servers': "kafkacluster-0.kafkacluster-headless.default.svc.cluster.local:9092",
                'client.id': socket.gethostname()}
producer = Producer(conf)
topic = "visits"



class VisitService:

    @staticmethod
    def create(location):

        producer.produce(topic, json.dumps(location))
    #producer.poll(1)
        producer.flush()  
        return ({"status": "ok"})    