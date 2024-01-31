import unittest
from unittest.mock import patch
from app.data_models import Event
from app.lib.event_handler import EventHandler


class TestEventHandler(unittest.TestCase):
    def setUp(self):
        mock_data = {
                "user_id": "foo1",
                "device_id": "bar1",
                "event_type": "training_program_started",
                "training_program_id": "2352",
                "training_program_title": "7 Minutes of HIIT Training",
                "time_stamp": "2021-02-28 16:23:25",
            }
        self.event = Event(**mock_data)
        self.handler = EventHandler(self.event)

    def test_process_event_app_launch(self):
        with patch('app.lib.event_handler.cached_read_config') as mock_read_config:
            self.handler.process_event()
            mock_read_config.assert_called_once()

    def test_process_event_training_program_started(self):
        with patch('app.lib.event_handler.cached_read_config') as mock_read_config:
            self.event.event_type = 'training_program_started'
            self.handler.process_event()
            mock_read_config.assert_called_once()

    def test_process_event_training_program_finished(self):
        with patch('app.lib.event_handler.cached_read_config') as mock_read_config:
            self.event.event_type = 'training_program_finished'
            self.handler.process_event()
            mock_read_config.assert_called_once()

    def test_process_event_training_program_cancelled(self):
        with patch('app.lib.event_handler.cached_read_config') as mock_read_config:
            self.event.event_type = 'training_program_cancelled'
            self.handler.process_event()
            mock_read_config.assert_called_once()

    def test_process_event_invalid_type(self):
        self.event.event_type = 'invalid_type'
        with self.assertRaises(ValueError):
            self.handler.process_event()


if __name__ == '__main__':
    unittest.main()
