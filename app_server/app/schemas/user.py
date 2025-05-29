from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    guid: str
    name: str
    gender: str
    age: int
    birthday: date
    email: EmailStr
    password: str
    passwordConfirm: str

    class Config:
        orm_mode = True