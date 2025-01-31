from datetime import date
from typing import Optional, Dict, List
from loguru import logger
from pydantic import BaseModel, EmailStr
import uuid


class GuestHistory(BaseModel):
    """
    Represents the history of a guest's stay.
    """
    guest_arrival: date
    guest_room_id: str
    guest_departure: Optional[date | None]


class GuestBase(BaseModel):
    """
    Represents the basic information of a guest.
    """
    guest_id: str = str(uuid.uuid4())
    guest_name: str
    guest_email: EmailStr
    guest_contact: str  # TODO: Add regex for contact number --> regex=r'^(\+8801|01)[0-9]\d{9}$'
    guest_history: List[GuestHistory]

    def update(self, **kwargs: dict) -> None:
        """
        Update the attributes of the guest with the given keyword arguments.

        :param kwargs: Dictionary of attributes to update.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

class GuestData(BaseModel):
    """
    Represents a collection of guests.
    """
    guests: Dict[str, GuestBase] = {}

    def add_dummy_guest(self, dummy_guest_data: dict) -> None:
        """
        Add a dummy guest to the collection.

        :param dummy_guest_data: Dictionary containing dummy guest data.
        """
        new_guest = GuestBase(**dummy_guest_data)
        self.guests[new_guest.guest_id] = new_guest

        # Hardcoded for testing purposes
        self.guests["23159162-dd67-4a2a-8054-d6be6c0379ca"] = new_guest.model_copy()
        self.guests["23159162-dd67-4a2a-8054-d6be6c0379ca"].guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
        del self.guests[new_guest.guest_id]

class UpdateGuest(BaseModel):
    """
    Represents the fields that can be updated for a guest.
    """
    guest_name: Optional[str] = None
    guest_email: Optional[EmailStr] = None
    guest_contact: Optional[str] = None
    guest_history: Optional[List[GuestHistory]] = None
