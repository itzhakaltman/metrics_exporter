#!/usr/bin/env python3

# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

import yaml
import json

config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'


def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)



print(read_yaml(config_file))
#if __name__ == "__main__":
#    read_yaml(config_file)

