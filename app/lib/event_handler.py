from app.data_models import Event
from .config_handler import cached_read_config


class EventHandler:
    def __init__(self, event_obj: Event):
        self.event = event_obj
        self.config = cached_read_config()

    def process_event(self):
        match self.event.type:
            case 'app_launch':
                self.process_app_launch()
            case 'training_program_started':
                self.process_training_program_started()
            case 'training_program_finished':
                self.process_training_program_completed()
            case 'training_program_cancelled':
                self.process_training_program_cancelled()
            case _:
                raise ValueError('Invalid event type')

    def process_app_launch(self):
        # TODO: Extend this method to process app_launch event.
        # Make a call to /v1/notify
        pass

    def process_training_program_started(self):
        # TODO: Extend this method to process training_program_started event.
        # Make a call to /v1/notify
        pass

    def process_training_program_finished(self):
        # TODO: Extend this method to process training_program_finished event.
        # Make a call to /v1/notify
        pass

    def process_training_program_cancelled(self):
        # TODO: Extend this method to process training_program_cancelled event.
        # Make a call to /v1/notify
        pass
