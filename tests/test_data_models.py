import unittest
from datetime import datetime
from pydantic import ValidationError
from app.data_models import Event


class TestDataModels(unittest.TestCase):
    def test_event_valid(self):
        event_data = {
            "user_id": "foo1",
            "device_id": "bar1",
            "event_type": "training_program_started",
            "training_program_id": "2352",
            "training_program_title": "7 Minutes of HIIT Training",
            "time_stamp": datetime.now(),
        }
        event = Event(**event_data)
        self.assertEqual(event.user_id, "foo1")
        self.assertEqual(event.device_id, "bar1")
        self.assertEqual(event.event_type, "training_program_started")
        self.assertEqual(event.training_program_id, "2352")
        self.assertEqual(event.training_program_title, "7 Minutes of HIIT Training")
        self.assertIsInstance(event.time_stamp, datetime)

    def test_event_invalid_type(self):
        event_data = {
            "user_id": "foo1",
            "device_id": "bar1",
            "event_type": "invalid_type",
            "training_program_id": "2352",
            "training_program_title": "7 Minutes of HIIT Training",
            "time_stamp": datetime.now(),
        }
        with self.assertRaises(ValidationError):
            Event(**event_data)


if __name__ == '__main__':
    unittest.main()