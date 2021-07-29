from confluent_kafka import Producer
import socket

#https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html#initialization
#https://www.tutorialsbuddy.com/confluent-kafka-python-consumer-example

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

# initialization
conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)

#producer.produce(topic, key="key", value="value")

# send data to kafka
for e in range(10):

    print(e)
    producer.produce("c99", key="mykey", value="have a nice day",callback=acked)
    producer.poll(1)