from functools import lru_cache
import configparser
import os


@lru_cache(maxsize=None)
def cached_read_config():
    config = configparser.ConfigParser()
    config.read(f'{os.getcwd()}/app/config.ini')
    return config

