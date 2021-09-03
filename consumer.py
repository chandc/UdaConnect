from kafka import KafkaConsumer
from json import loads
from datetime import datetime

# https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

consumer = KafkaConsumer(
    'visits',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group99',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print(datetime.now().strftime("%H:%M:%S"))
    print('{} read'.format(message)     )