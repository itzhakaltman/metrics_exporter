#!/usr/bin/env python3

# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

import yaml
import os

#config_file = '/Users/itzhak/Documents/GitHub/metrics_exporter/config/config.yaml'

dir_path = os.path.join(os.path.dirname( __file__ ), '..' )
config_path = os.path.join(dir_path, "config", "config.yaml")
print(config_path)

#def read_yaml():
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    companies_path = os.path.join(dir_path, "config", "config.yaml")
#    with open(config_file, "r") as f:
#        return yaml.safe_load(f)





#print(read_yaml(config_file))
#if __name__ == "__main__":
#    read_yaml(config_file)

