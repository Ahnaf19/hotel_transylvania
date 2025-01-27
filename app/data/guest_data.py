from app.schemas import guest_schema
# import uuid

class Guest(guest_schema.GuestBase):
    def __init__(self, guest_name, guest_email, guest_contact, guest_history=None):
        super().__init__(
            guest_name=guest_name,
            guest_email=guest_email,
            guest_contact=guest_contact,
            guest_history=guest_history
        )
        # self.guest_id = str(uuid.uuid4())
        # ! Hardcoded for testing purposes
        self.guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca" 

    def __str__(self):
        return f"Guest ID: {self.guest_id}\nGuest Name: {self.guest_name}\nGuest Email: {self.guest_email}\nGuest Contact: {self.guest_contact}\nGuest History: {self.guest_history}"
    
    
class GuestData(guest_schema.GuestData):
    def __init__(self):
        self.guests = []
        dummy_guest = {
            "guest_name": "John Doe",
            "guest_email": "ahnaf@cloudly.io",
            "guest_contact": "01700000000",
            "guest_history": [
                {
                    "guest_arrival": "2021-10-01",
                    "guest_room_id": "101",
                    "guest_departure": "2021-10-03"
                },
                {
                    "guest_arrival": "2021-10-05",
                    "guest_room_id": "102",
                    "guest_departure": None
                }
                    ]
        }
        self.add_dummy_guest(**dummy_guest)

    def add_dummy_guest(self, guest_name, guest_email, guest_contact, guest_history=None):
        new_guest = Guest(guest_name, guest_email, guest_contact, guest_history)
        self.guests.append(new_guest)
        return new_guest

# initialize the dummy guest data
dummy_guest_data = GuestData()

if __name__ == "__main__":
    print(dummy_guest_data.guests, end="\n\n")
    print(str(dummy_guest_data.guests[0]), end="\n\n")
    print(dummy_guest_data.guests[0].guest_id)
    print(dummy_guest_data.guests[0].guest_name)
    print(dummy_guest_data.guests[0].guest_email)
    print(dummy_guest_data.guests[0].guest_contact)
    print(dummy_guest_data.guests[0].guest_history)
    print(dummy_guest_data.guests[0].guest_history[0].guest_arrival)
    print(dummy_guest_data.guests[0].guest_history[0].guest_room_id)
    print(dummy_guest_data.guests[0].guest_history[0].guest_departure)
    print(dummy_guest_data.guests[0].guest_history[1].guest_arrival)
    print(dummy_guest_data.guests[0].guest_history[1].guest_room_id)
    print(dummy_guest_data.guests[0].guest_history[1].guest_departure)