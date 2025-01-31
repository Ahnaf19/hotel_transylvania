from datetime import date
from typing import Optional
from loguru import logger
from pydantic import BaseModel, EmailStr
import uuid


class GuestHistory(BaseModel):
    guest_arrival: date
    guest_room_id: str
    guest_departure: Optional[date | None]

class GuestBase(BaseModel):
    guest_id: str = str(uuid.uuid4())
    guest_name: str
    guest_email: EmailStr
    guest_contact: str #  TODO: Add regex for contact number --> regex=r'^(\+8801|01)[0-9]\d{9}$'
    guest_history: list[GuestHistory]
    
    def update(self, **kwargs) -> None:
        """
        Update the attributes of the room with the given keyword arguments.
        
        :param kwargs: Dictionary of attributes to update.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

class GuestData(BaseModel):
    guests: dict[str, GuestBase] = {}
    
    def add_dummy_guest(self, dummy_guest_data) -> None:
        new_guest = GuestBase(**dummy_guest_data)
        self.guests[new_guest.guest_id] = new_guest
        
        # ! Hardcoded for testing purposes
        self.guests["23159162-dd67-4a2a-8054-d6be6c0379ca"] = new_guest.model_copy()
        self.guests["23159162-dd67-4a2a-8054-d6be6c0379ca"].guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
        del self.guests[new_guest.guest_id]

class UpdateGuest(BaseModel):
    guest_name: Optional[str]
    guest_email: Optional[EmailStr]
    guest_contact: Optional[str]
    guest_history: Optional[list[GuestHistory]]

