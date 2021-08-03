from confluent_kafka import Consumer
from time import sleep

class UdaConsumer:

    def __init__(self, broker="localhost:9092", topic="test-topic", group_id="consumer-1"):
         self.broker = broker
         self.topic = topic
         self.group_id = group_id

    def start_listener(self):
        consumer_config = {
            'bootstrap.servers': self.broker,
            'group.id': self.group_id,
            'auto.offset.reset': 'largest',
            'enable.auto.commit': 'false',
            'max.poll.interval.ms': '86400000'}

        consumer = Consumer(consumer_config)
        consumer.subscribe([self.topic])

        try:
            while True:
                print("Listening")
                # read single message at a time
                msg = consumer.poll(0)

                if msg is None:
                    sleep(5)
                    continue
                if msg.error():
                    print("Error reading message : {}".format(msg.error()))
                    continue
                # You can parse message and save to data base here
                input_data = msg.value().decode('utf-8')
                #json.load(message.value.decode())
                print(input_data)
                consumer.commit()

        except Exception as ex:
            print("Kafka Exception : {}", ex)

        finally:
            print("closing consumer")
            consumer.close()

#RUNNING CONSUMER FOR READING MESSAGE FROM THE KAFKA TOPIC
my_consumer = UdaConsumer(topic="visits")
my_consumer.start_listener()