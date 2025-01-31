from app.schemas import guest_schema
from loguru import logger


# Dummy guest data for testing purposes
dummy_guest_local = {
    "guest_name": "John Doe",
    "guest_email": "john@cloudly.io",
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

class GuestData1:
    """
    Class to manage guest data.
    """

    def __init__(self):
        """
        Initialize the GuestData1 class with an empty dictionary of guests.
        """
        self.guests: dict[str, guest_schema.GuestBase] = {}
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
        self.add_dummy_guest(dummy_guest)

    def add_dummy_guest(self, dummy_guest: dict) -> None:
        """
        Add a dummy guest to the guests dictionary.

        Args:
            dummy_guest (dict): The dummy guest data.
        """
        new_guest, new_guest_id = self.add_guest(dummy_guest)

        # Hardcoded for testing purposes
        self.guests["23159162-dd67-4a2a-8054-d6be6c0379ca"] = new_guest
        self.guests["23159162-dd67-4a2a-8054-d6be6c0379ca"].guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
        del self.guests[new_guest_id]

    def add_guest(self, guest: dict) -> tuple[guest_schema.GuestBase, str]:
        """
        Add a guest to the guests dictionary.

        Args:
            guest (dict): The guest data.

        Returns:
            tuple: A tuple containing the new guest object and the guest ID.
        """
        new_guest = guest_schema.GuestBase(**guest)  # pydantic isn't designed to work with positional arguments
        self.guests[new_guest.guest_id] = new_guest
        return new_guest, new_guest.guest_id

# Initialize the dummy guest data
dummy_guest_data = guest_schema.GuestData()
dummy_guest_data.add_dummy_guest(dummy_guest_local)

if __name__ == "__main__":
    dummy_guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
    guest = dummy_guest_data.guests[dummy_guest_id]
    print(type(dummy_guest_data))
    print(type(dummy_guest_data.guests))
    print(type(guest), end="\n\n")
    print(dummy_guest_data.guests)
    print(guest.guest_id)
    print(guest.guest_name)
    print(guest.guest_email)
    print(guest.guest_contact)
    print(guest.guest_history)
    print(guest.guest_history[0].guest_arrival)
    print(guest.guest_history[0].guest_room_id)
    print(guest.guest_history[0].guest_departure)
    print(guest.guest_history[1].guest_arrival)
    print(guest.guest_history[1].guest_room_id)
    print(guest.guest_history[1].guest_departure)