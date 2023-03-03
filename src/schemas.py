from pydantic import BaseModel, Field, EmailStr
from datetime import date


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
