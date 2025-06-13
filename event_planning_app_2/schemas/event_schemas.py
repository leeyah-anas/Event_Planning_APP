from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from schemas.speaker_schemas import Speaker


class EventCreate(BaseModel):
    title: str
    location: str
    datetime: datetime
    speaker_id: Optional[int]

class Event(BaseModel):
    id: int
    title: str
    location: str
    datetime: datetime
    is_open: bool = True
    speaker_id: Optional[int]

class EventWithSpeaker(Event):
    speaker: Optional[Speaker]