#!/usr/bin/env python3

import yaml

config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'


def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


config = read_yaml(config_file)
print(config)
print(config["HOST"])
print(config["PORT"])
