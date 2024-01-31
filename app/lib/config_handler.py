from functools import lru_cache
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')


@lru_cache(maxsize=None, ttl=6*60*60)
def cached_read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config
