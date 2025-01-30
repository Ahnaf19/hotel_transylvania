from ..schemas.guest_schema import GuestBase

class GuestService:
    def __init__(self):
        self.guests = []

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
