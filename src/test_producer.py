#!/usr/bin/env python3

from time import sleep
from json import dumps
from kafka import KafkaProducer
from config import KAFKA_TOPIC
from config import BOOTSTRAP_SERVER
from config import METRIC_NAME

producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {METRIC_NAME: e}
    producer.send(KAFKA_TOPIC, value=data)
    print(data)
    sleep(1)