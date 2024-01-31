import unittest
from app.lib.config_handler import cached_read_config


class TestConfigHandler(unittest.TestCase):
    def setup(self):
        pass

    def test_cached_read_config(self):
        config = cached_read_config()
        self.assertEqual(config['Event_TYPES']['app_launch'], '"app_launch"')
