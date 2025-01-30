from app.schemas.guest_schema import *
# from app.exceptions.guest_exceptions import GuestNotFoundException
from loguru import logger

class GuestService:
    def __init__(self, dummy_guest_data: GuestData):
        self.dummy_guest_data = dummy_guest_data
        logger.debug("GuestService initialized")

    def create_guest(self, guest: GuestBase):
        self.guests.append(guest)
        return guest

    def get_guests(self):
        return self.guests

    def get_guest(self, guest_id: str):
        for guest in self.guests:
            if guest.guest_id == guest_id:
                return guest
        return None
