from fastapi import APIRouter, HTTPException
from schemas.user_schemas import UserCreate, User
from service.users import User_service


user_router =  APIRouter()

@user_router.get("/")
def get_users():
    return User_service.get_users()

@user_router.get("/{user_id}")
def get_user_by_id(user_id: int):
    user = User_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user 
    

@user_router.post("/")
def create_user(user_in: UserCreate):
    return User_service.create_user(user_in)
    
@user_router.put('/{user_id}')
def update_user(user_id: int, user_in: UserCreate):
    updated = User_service.update_user(user_id, user_in)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@user_router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted = User_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message":f"User Deleted"}

@user_router.patch("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    user = User_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
