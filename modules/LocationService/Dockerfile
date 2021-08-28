FROM python:3.7-alpine

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev librdkafka-dev

WORKDIR .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python", "confluent_kafka_Consumer.py"]
