from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime


class ContactModel(BaseModel):
    first_name: str = Field(min_length=2, max_length=20)
    last_name: str = Field(min_length=2, max_length=20)
    email: EmailStr
    phone_number: str = Field(min_length=5, max_length=12)
    birthday: date


class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str = Field(min_length=2, max_length=20)
    email: EmailStr
    password: str = Field(min_length=7, max_length=200)


class UserDb(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
