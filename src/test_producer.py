#!/usr/bin/env python3

from time import sleep
import random
from json import dumps
from kafka import KafkaProducer
from config import KAFKA_TOPIC
from config import KAFKA_KEY
from config import BOOTSTRAP_SERVER
from config import METRIC_NAME

producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

kafka_key = bytes(KAFKA_KEY, 'utf-8')

for e in range(2620269952):
    random_number = random.randint(1, 24)
    data = {METRIC_NAME: random_number}
    producer.send(KAFKA_TOPIC, value=data, key=kafka_key)
    print(data)
    sleep(15)