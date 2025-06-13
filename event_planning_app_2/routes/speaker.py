from fastapi import APIRouter, HTTPException
from schemas.speaker_schemas import Speaker, SpeakerCreate
from service.speakers import SpeakerService

speaker_router = APIRouter()

@speaker_router.get("/")
def get_all_speakers():
    return SpeakerService.get_all_speakers()

@speaker_router.get("/{speaker_id}")
def get_speaker_by_id(speaker_id: int):
    speaker = SpeakerService.get_speaker_by_id(speaker_id)
    if not speaker:
        raise HTTPException(status_code=404, detail="speaker not found")
    return speaker
