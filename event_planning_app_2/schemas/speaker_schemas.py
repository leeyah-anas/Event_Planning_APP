from pydantic import BaseModel

class SpeakerCreate(BaseModel):
     name: str
     topic: str 

class Speaker(SpeakerCreate):
    id: int

    