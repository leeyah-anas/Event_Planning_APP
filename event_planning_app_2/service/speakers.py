from schemas.speaker_schemas import Speaker
from db import speakers

class SpeakerService:

    @staticmethod
    def get_all_speakers():
        return [Speaker(**s) for s in speakers.values()]
    
    @staticmethod
    def get_speaker_by_id(speaker_id: int):
        speaker = speakers.get(speaker_id)
        if not speaker:
            return None
        return Speaker(**speaker)
    
    
speaker_service = SpeakerService()