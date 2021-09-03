from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(10):
    print ('producing message ' + str(e))
    producer.send('visits', {'number': e, 'time': datetime.now().strftime("%H:%M:%S")})
    #data = {'number' : e, 'name' : 'John Doe'}
    #producer.send('visits', value=data)
    sleep(5)