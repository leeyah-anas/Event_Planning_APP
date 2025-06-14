from fastapi import APIRouter, HTTPException
from schemas.registration_schemas import RegistrationCreate, Registration
from service.registrations import registration_service

registration_router = APIRouter()

@registration_router.post("/")
def register_user(reg_in: RegistrationCreate):
    result = registration_service.register_user(reg_in)
    if isinstance(result, str):
        raise HTTPException(status_code=400, detail="Event closed")
    return result

@registration_router.patch("/{reg_id}/attend")
def mark_attendance(reg_id: int):
    reg = registration_service.mark_attendance(reg_id)
    if not reg:
        raise HTTPException(status_code=404, detail="User not registered")
    return reg

@registration_router.get("/user/{user_id}")
def get_registered_user(user_id: int):
    return registration_service.get_registered_user(user_id)


@registration_router.get("/")
def get_all_registrations():
    return registration_service.get_all_registrations()

