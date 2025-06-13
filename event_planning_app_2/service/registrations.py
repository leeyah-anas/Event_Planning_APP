from schemas.registration_schemas import RegistrationCreate, Registration
from db import events, users, registrations
from datetime import datetime

class RegistrationService:
    @staticmethod
    def register_user(reg_in:RegistrationCreate):
        if reg_in.user_id not in users or not users[reg_in.user_id].is_active:
            return "User not found or inactive"
        if reg_in.event_id not in events or not events[reg_in.event_id].is_open:
            return "Event not found or not open"
    
        for reg in registrations.values():
            if reg.user_id == reg_in.user_id and reg.event_id == reg_in.event_id:
                return "User already registered for this event"
        
        reg_id = len(registrations) + 1
        new_reg = Registration(id=reg_id, user_id=reg_in.user_id, event_id=reg_in.event_id, registration_date=datetime.now()
                           )
        registrations[reg_id] = new_reg
        return new_reg
    @staticmethod
    def mark_attendance(reg_id: int):
        reg = registrations.get(reg_id)
        if reg:
            reg.attended = True
            return reg
        return None
    
    @staticmethod
    def get_registered_user(user_id: int):
        return [r for r in registrations.values() if r.user_id == user_id]
    
    @staticmethod
    def get_all_registrations():
        return registrations

    


registration_service = RegistrationService()