from fastapi import APIRouter, HTTPException
from schemas.event_schemas import EventCreate, Event
from service.events import Event_service

event_router = APIRouter()

@event_router.get("/")
def get_all_events():
    return Event_service.get_all_events()

@event_router.get("/{event_id}")
def get_event_by_id(event_id: int):
    event = Event_service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@event_router.post("/")
def create_event(event_in: EventCreate):
    return Event_service.create_event(event_in)

@event_router.put("/")
def update_event(event_id: int, event_in: EventCreate):
    updated = Event_service.update_event(event_id, event_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated

@event_router.delete("/{event_id}")
def delete_user(event_id: int):
    deleted = Event_service.delete_event(event_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message":f"User Deleted successfully"}

@event_router.patch("/{event_id}/close")
def close_event(event_id: int):
    event = Event_service.close_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event




