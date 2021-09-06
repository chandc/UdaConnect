from concurrent import futures
import grpc

from person_pb2 import (
    Person,
    Empty
)
import person_pb2_grpc, person_pb2
import logging
import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-api")


PERSON_SERVICE_ENDPOINT = "http://person-api:5000/"

ListofPersons = requests.get(PERSON_SERVICE_ENDPOINT + "api/persons").json()

logger.info(f"No of Persons: {len(ListofPersons)}")
logger.info(ListofPersons)

class PersonServer(person_pb2_grpc.PersonRequestServicer):
    def PersonLookup(self, request, context):
        for person in ListofPersons:
            response = person_pb2.Person(id=person['id'], first_name=person['first_name'], 
                                         last_name=person['last_name'], 
                                         company_name=person['company_name'])

            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    person_pb2_grpc.add_PersonRequestServicer_to_server(
        PersonServer(), server
    )

    server.add_insecure_port('[::]:50051')
    #server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()       



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
