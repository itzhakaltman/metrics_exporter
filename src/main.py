#!/usr/bin/env python3

import yaml
import requests

config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'

def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)

config = read_yaml(config_file)
print(config)

PGW_HOST = config["PGW HOST"]
PGW_PORT = config["PGW PORT"]
JOB_NAME = config["JOB NAME"]
LABEL_NAME = config["LABEL NAME"]
LABEL_VALUE = config["LABEL VALUE"]
KAFKA = config["KAFKA"]
TOPIC_PORT = config["TOPIC PORT"]
TOPIC = config["TOPIC"]
KEY = config["KEY"]
METRIC_NAME = config["METRIC NAME"]
METRIC_VALUE = config["METRIC VALUE"]

API_ENDPOINT = 'http://{}:{}/metrics/job/{}/{}/{}'.format(PGW_HOST, PGW_PORT, JOB_NAME, LABEL_NAME,
                                                                    LABEL_VALUE)
#data = '{} {}'.format(METRIC_NAME, METRIC_VALUE)
data = 'demo 321'
request = requests.post(url=API_ENDPOINT, data=data)

print(API_ENDPOINT)
print(data)
print(request.text)

# echo "demo_metric 123" | curl --data-binary @- http://localhost:9091/metrics/job/demo_pg_job/instance/demo_instance/event/add


# BODY - echo “demo_metric 123”

# curl = subprocess.run(['curl',
#                       'http://{}:{}/metrics/job/{}/{}/{}/event/add'.format(pgw_host, pgw_port, job_name, label_name,
#                                                                            label_value)])
# curl -X POST --header "Content-Type: application/json" --data '{"key1":"value1", "key2":"value2"}' http://8.8.8.8//

# curl = ['curl', 'http://{}:{}/metrics/job/{}/{}/{}/event/add'.format(pgw_host, pgw_port, job_name, label_name, label_value)]


# print(curl)
