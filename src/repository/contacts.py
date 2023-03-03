from typing import List
from datetime import date, timedelta

from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(db: Session):
    return db.query(Contact).all()


async def get_contact(contact_id: int, db: Session):
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session):
    contact = Contact(first_name=body.first_name, last_name=body.last_name, email=body.email,
                      phone_number=body.phone_number, birthday=body.birthday)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.email = body.email
        db.commit()
    return contact


async def find_contact_by_info(find_info, db: Session):
    return db.query(Contact).filter(
        or_(Contact.first_name == find_info, Contact.last_name == find_info, Contact.email == find_info)).all()


async def birthday(db: Session):
    last_birthday_point = date.today() + timedelta(days=7)
    return db.query(Contact).filter(and_(Contact.birthday.between(date.today(), last_birthday_point))).all()