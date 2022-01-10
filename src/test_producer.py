#!/usr/bin/env python3

from time import sleep
from json import dumps
from kafka import KafkaProducer
from config import KAFKA_TOPIC
from config import KAFKA_IP
from config import KAFKA_PORT
from config import METRIC_NAME

bootstrap_server = '\'' + str(KAFKA_IP) + ':' + str(KAFKA_PORT) + '\''
topic = '\'' + str(KAFKA_TOPIC) + '\''

print(bootstrap_server)

producer = KafkaProducer(bootstrap_servers=['10.210.110.20:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {METRIC_NAME: e}
    producer.send(KAFKA_TOPIC, value=data)
    print(data)
    sleep(1)
