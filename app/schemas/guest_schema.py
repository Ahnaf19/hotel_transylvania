from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr

class GuestHistory(BaseModel):
    guest_arrival: date
    guest_room_id: str
    guest_departure: Optional[date | None]

class GuestBase(BaseModel):
    guest_id: Optional[str] = None
    guest_name: str
    guest_email: EmailStr
    guest_contact: str #  TODO: Add regex for contact number --> regex=r'^(\+8801|01)[0-9]\d{9}$'
    guest_history: Optional[list[GuestHistory] | None]

class GuestData:
    guest: list[GuestBase]