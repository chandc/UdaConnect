from flask import Flask
from flask import request
from confluent_kafka import Producer
import socket
import json
from datetime import datetime


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


app = Flask(__name__)

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}
producer = Producer(conf)
topic = "visits"
       

@app.route("/",  methods = ['POST'])
def whereabout():

    location = request.get_json()
    # location['creation_time'] created by the database
    #print(location)
    producer.produce(topic, json.dumps(location),callback=acked)
    #producer.poll(1)
    producer.flush()
    return json.dumps({'success, data sent':location,})


if __name__ == "__main__":
    app.run()
