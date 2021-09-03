import logging

#from confluent_kafka import Producer
from kafka import KafkaProducer

import json
from json import dumps
import datetime

#import socket


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

#conf = {'bootstrap.servers': "kafkacluster-0.kafkacluster-headless.default.svc.cluster.local:9092",
#                'client.id': socket.gethostname()}
#producer = Producer(conf)
#topic = "visits"

producer = KafkaProducer(bootstrap_servers=['kafkacluster-0.kafkacluster-headless.default.svc.cluster.local:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
topic = "visits"



class VisitService:

    @staticmethod
    def create(location):
        location['creation_time']=datetime.datetime.now().isoformat()
        #producer.produce(topic, json.dumps(location))
        producer.send(topic, location)
    #producer.poll(1)
        #producer.flush()  
        return ({"status": "ok"})    
