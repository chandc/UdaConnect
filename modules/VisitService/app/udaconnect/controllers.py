from confluent_kafka import Producer
import socket
import json
from flask import request
from flask_restx import Namespace


api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

conf = {'bootstrap.servers': "kafkacluster.default.svc.cluster.local:9092",
        'client.id': socket.gethostname()}
producer = Producer(conf)
topic = "visits"

@api.route("/viists",  methods = ['POST'])
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))
def whereabout():
    location = request.get_json()
    # location['creation_time'] created by the database
    #print(location)
    producer.produce(topic, json.dumps(location),callback=acked)
    #producer.poll(1)
    producer.flush()
    return json.dumps({'success, data sent to Kafka':location,})

