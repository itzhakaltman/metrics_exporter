#!/usr/bin/env python3
import json
from kafka import KafkaConsumer
import requests
from config import API_ENDPOINT
from config import METRIC_NAME

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('m-exp',
                         group_id='my-group',
                         bootstrap_servers=['10.210.110.20:9092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    # print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                      message.offset, message.key,
    #                                      message.value))
    message_value_string = message.value.decode("utf-8")
    message_value_dict = json.loads(message_value_string)
    message_value_value = message_value_dict[METRIC_NAME]
    # print(METRIC_NAME)
    # print(message_value_value)

    data = str(METRIC_NAME) + ' ' + str(message_value_value) + '\n'
    print(data)


    # data = 'demo 321\n'

    request = requests.post(url=API_ENDPOINT, data=data)


# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# consume msgpack
KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)

# Subscribe to a regex topic pattern
consumer = KafkaConsumer()
consumer.subscribe(pattern='^awesome.*')

# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
consumer1 = KafkaConsumer('numtest',
                          group_id='my-group',
                          bootstrap_servers='10.210.110.20:9092')
consumer2 = KafkaConsumer('numtest',
                          group_id='my-group',
                          bootstrap_servers='10.210.110.20:9092')



