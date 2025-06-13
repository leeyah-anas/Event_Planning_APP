from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr

class User(UserCreate):
    id: int
    is_active: bool = True 
  