#!/usr/bin/env python3

import yaml
import requests


def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


config = read_yaml(config_file)
print(config)

data = 'demo 321\n'

request = requests.post(url=API_ENDPOINT, data=data)

# print(API_ENDPOINT)
# print(request.text)
