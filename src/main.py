#!/usr/bin/env python3

import yaml
import subprocess

config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'

def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)

config = read_yaml(config_file)
print(config)
# print(config["HOST"])
# print(config["PORT"])

pgw_host = config["PGW HOST"]
pgw_port = config["PGW PORT"]
job_name = config["JOB NAME"]
label_name = config["LABEL NAME"]
label_value = config["LABEL VALUE"]
kafka = config["KAFKA"]
topic_port = config["TOPIC PORT"]
topic = config["TOPIC"]
key = config["KEY"]
metric_name = config["METRIC NAME"]
metric_value = config["METRIC VALUE"]

# BODY - echo “demo_metric 123”

#curl = subprocess.run(['curl',
#                       'http://{}:{}/metrics/job/{}/{}/{}/event/add'.format(pgw_host, pgw_port, job_name, label_name,
#                                                                            label_value)])
# curl -X POST --header "Content-Type: application/json" --data '{"key1":"value1", "key2":"value2"}' http://8.8.8.8//

curl = ['curl', 'http://{}:{}/metrics/job/{}/{}/{}/event/add'.format(pgw_host, pgw_port, job_name, label_name, label_value)]


print(curl)
