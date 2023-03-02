from pydantic import BaseModel, Field, EmailStr
from datetime import date


class ContactModel(BaseModel):
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    email: EmailStr
    phone_number: str
    birthday: date


class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True
