import json
from kafka import KafkaConsumer
import requests
from config import API_ENDPOINT
from config import METRIC_NAME
from config import BOOTSTRAP_SERVER
from config import KAFKA_TOPIC
from config import GROUP_ID

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(KAFKA_TOPIC,
                         group_id=GROUP_ID,
                         bootstrap_servers=[BOOTSTRAP_SERVER])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
    message_value_string = message.value.decode("utf-8")
    message_value_dict = json.loads(message_value_string)
    message_value_value = message_value_dict[METRIC_NAME]

    data = str(METRIC_NAME) + ' ' + str(message_value_value) + '\n'
    print(data)
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