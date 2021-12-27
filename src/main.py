#!/usr/bin/env python3

# https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3

import yaml
import pytest

config_file = '/config/config.yaml'


def read_yaml(config_file):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


def test_validation_yaml(config_file):
    with pytest.raises(FileNotFoundError):
        read_yaml(config_file)

    with pytest.raises(yaml.scanner.ScannerError):
        # only show the first error
        read_yaml(config_file)

    with pytest.raises(yaml.parser.ParserError):
        # only show the first error
        read_yaml(config_file)


if __name__ == "__main__":
    config = read_yaml(config_file)
    test = test_validation_yaml(config_file)
    print(config)
    print(test)
    sys.exit(0)
