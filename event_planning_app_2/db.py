from schemas.event_schemas import Event
from schemas.user_schemas import UserCreate
from schemas.registration_schemas import Registration
from schemas.speaker_schemas import Speaker

users: dict[str, UserCreate] = {}
events: dict[str, Event] = {}
registrations: dict[str, Registration] = {}
speakers: dict[str, Speaker] = {
    1: {"id": 1, "name": "Adejumo Progress", "topic": "Cook or be cooked"},
    2: {"id": 2, "name": "Ameerah Anas", "topic": "Life of Pi"},
    3: {"id": 3, "name": "Steve Harvey", "topic": " Think like a Man"}
}