#!/usr/bin/env python3

# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

import yaml

# import os

config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'


# dir_path = os.path.join(os.path.dirname(__file__), '..')
# config_path = os.path.join(dir_path, "config", "config.yaml")
# print(config_path)

def read_yaml(config_file):
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    companies_path = os.path.join(dir_path, "config", "config.yaml")
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


print(read_yaml(config_file))

#ENVIRONMENT = : dev
#  DEBUG: True #False

#PUSHGATEWAY:
#  HOST: 192.168.192.2
#  PORT: 8080
#
#DATABASE:
#  USERNAME: user
#  PASSWORD: password
#  HOST: 192.168.192.3
#  PORT: 5432
#  DB: metrics_exporter




# if __name__ == "__main__":
#    read_yaml(config_file)
