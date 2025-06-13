from schemas.user_schemas import UserCreate, User
from db import users

class UserService:
    @staticmethod
    def get_users():
        return list(users.values())
    
    @staticmethod
    def get_user_by_id(user_id: int):
        user = users.get(user_id)
        if not user:
            return None
        return user

    @staticmethod
    def create_user(user_in: UserCreate):
        user_id = len(users) + 1
        user = User(id=user_id, **user_in.dict())
        users[user_id] = user
        return user
    
    @staticmethod
    def update_user(user_id: int, user_in: UserCreate):
        if user_id not in users:
            return None
        existing_user = users[user_id]
        updated_user = User(id=user_id, full_name=user_in.full_name, email=user_in.email, is_active=existing_user.is_active)
        users[user_id] = updated_user
        return updated_user
    
    @staticmethod
    def delete_user(user_id: int):
        return users.pop(user_id, None)
    
    @staticmethod
    def deactivate_user(user_id: int):
        user = users.get(user_id)
        if user:
            user.is_active = False
            return user
        return None
   
        

User_service = UserService()