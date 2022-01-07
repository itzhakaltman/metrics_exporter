#!/usr/bin/env python3

from time import sleep
from json import dumps
from kafka import KafkaProducer
from config import TOPIC
from config import KAFKA
from config import TOPIC_PORT

bootstrap_server = '\'' + str(KAFKA) + ':' + str(TOPIC_PORT) + '\''
topic = '\'' + str(TOPIC) + '\''

print(bootstrap_server)

producer = KafkaProducer(bootstrap_servers=['10.210.110.20:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number': e}
    producer.send('m-exp', value=data)
    print(data)
    sleep(5)
