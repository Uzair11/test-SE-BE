import unittest
from unittest.mock import patch
from app.routes import process_event
from app.data_models import Event
from app.lib.event_handler import EventHandler
from app import create_app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_process_event_valid(self):
        with self.app.test_request_context('/v1/api/event', method='POST', json={
            "user_id": "foo1",
            "device_id": "bar1",
            "event_type": "training_program_started",
            "training_program_id": "2352",
            "training_program_title": "7 Minutes of HIIT Training",
            "time_stamp": "2022-01-01T00:00:00"
        }):
            with patch.object(Event, 'is_valid', return_value=True):
                with patch.object(EventHandler, 'process_event') as mock_process_event:
                    response = process_event()
                    self.assertEqual(response[1], 200)
                    mock_process_event.assert_called_once()

    def test_process_event_invalid(self):
        with self.app.test_request_context('/v1/api/event', method='POST', json={
            "user_id": "foo1",
            "device_id": "bar1",
            "event_type": "invalid_type",
            "training_program_id": "2352",
            "training_program_title": "7 Minutes of HIIT Training",
            "time_stamp": "2022-01-01T00:00:00"
        }):
            with patch.object(Event, 'is_valid', return_value=False):
                response = process_event()
                self.assertEqual(response[1], 400)



if __name__ == '__main__':
    unittest.main()