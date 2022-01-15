#!/usr/bin/env python3

import yaml

config_file = '/config.yaml'


# config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'

def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


config = read_yaml(config_file)

PGW_HOST = config["PGW HOST"]
PGW_PORT = config["PGW PORT"]
PGW_JOB_NAME = config["JOB NAME"]
PGW_LABEL_NAME = config["LABEL NAME"]
PGW_LABEL_VALUE = config["LABEL VALUE"]
BOOTSTRAP_SERVER = config["BOOTSTRAP SERVER"]
KAFKA_TOPIC = config["TOPIC"]
GROUP_ID = config["GROUP ID"]
KAFKA_KEY = config["KEY"]
METRIC_NAME = config["METRIC NAME"]

API_ENDPOINT = 'http://{}:{}/metrics/job/{}/{}/{}'.format(PGW_HOST, PGW_PORT, PGW_JOB_NAME, PGW_LABEL_NAME,
                                                          PGW_LABEL_VALUE)
