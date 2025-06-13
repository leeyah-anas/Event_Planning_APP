from schemas.event_schemas import EventCreate, Event, EventWithSpeaker
from db import events, speakers

class EventService:
    @staticmethod
    def get_all_events():
        event_list =[]
        for event in events.values():
           speaker = speakers.get(event.speaker_id)
           event_dict = event.dict()
           event_dict["speaker"] = speaker
           event_with_speaker = EventWithSpeaker(**event_dict)
           event_list.append(event_with_speaker)
        return event_list  
    

    @staticmethod
    def get_event_by_id(event_id: int):
        event = events.get(event_id)
        if not event:
            return None
        return event
    
    @staticmethod
    def create_event(event_in: EventCreate) -> Event:
        event_id = len(events) + 1
        new_event = Event(id=event_id, **event_in.dict())
        events[event_id] = new_event
        return new_event
    
    
    
    @staticmethod
    def update_event(event_id: int, event_in: EventCreate):
        if event_id not in events:
            return None
        existing_event = events[event_id]
        updated_event = Event(id=event_id, title=event_in.title, location=event_in.location, datetime=event_in.datetime, is_open=existing_event.is_open, speaker_id=event_in.speaker_id )
        events = Event[event_id]
        return updated_event
    
    @staticmethod
    def delete_event(event_id: int):
        return events.pop(event_id, None)
    
    
    @staticmethod
    def close_event( event_id: int):
        event = events.get(event_id)
        if event:
            closed_event = Event(id=event.id, title=event.title, location=event.location, date=event.date, is_open=False, speaker_id=event.speaker_id)
            events[event_id]= closed_event
            return closed_event
        return None



    
    
Event_service = EventService() 