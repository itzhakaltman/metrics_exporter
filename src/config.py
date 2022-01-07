#!/usr/bin/env python3

import yaml

config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'


def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


config = read_yaml(config_file)
# print(config)

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

API_ENDPOINT = 'http://{}:{}/metrics/job/{}/{}/{}'.format(PGW_HOST, PGW_PORT, JOB_NAME, LABEL_NAME, LABEL_VALUE)
# print(API_ENDPOINT)
# print(request.text)
