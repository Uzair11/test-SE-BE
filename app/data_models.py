from pydantic import BaseModel, ValidationError, validator
from datetime import datetime
from typing import Optional
from app.lib.config_handler import cached_read_config


config = cached_read_config()

event_types = [key for key in config['EVENT_TYPES']]


class Event(BaseModel):
    user_id: str
    device_id: str
    event_type: str
    time_stamp: datetime
    training_program_title: Optional[str] = None
    training_program_id: str

    @validator('event_type')
    def event_type_must_be_valid(cls, v):
        if v not in event_types:
            raise ValidationError('event_type must be a valid event type')
        return v
