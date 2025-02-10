from fastapi.testclient import TestClient
from loguru import logger

from app.data.guest_data import dummy_guest_data
from app.main import app
from app.schemas.guest_schema import GuestBase, UpdateGuest


class TestGuestRouter:
    client: TestClient
    new_guest_dict: dict
    update_data: dict
    guest_id: str
    dummy_guest_data_converted: dict

    @classmethod
    def setup_class(cls) -> None:
        """
        Setup the test client and initial data for the tests.
        """
        cls.client = TestClient(app)
        cls.new_guest_dict = {
            "guest_name": "Jane Doe",
            "guest_email": "jane@cloudly.io",
            "guest_contact": "01700000001",
            "guest_history": [],
        }
        cls.update_data = {"guest_name": "Jane Smith", "guest_contact": "01700000002"}
        cls.guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
        cls.dummy_guest_data_converted = {
            "guests": {
                k: {
                    **v.model_dump(),
                    "guest_history": [
                        {
                            "guest_arrival": str(history.guest_arrival),
                            "guest_room_id": history.guest_room_id,
                            "guest_departure": (
                                str(history.guest_departure)
                                if history.guest_departure
                                else None
                            ),
                        }
                        for history in v.guest_history
                    ],
                }
                for k, v in dummy_guest_data.guests.items()
            }
        }

    def test_read_guests(self) -> None:
        """
        Test reading all guests.
        """
        response = self.client.get("/guests/")
        assert response.status_code == 200
        logger.debug(response.json())
        logger.debug(self.dummy_guest_data_converted)
        assert response.json() == self.dummy_guest_data_converted

    def test_read_guest(self) -> None:
        """
        Test reading a specific guest by ID.
        """
        response = self.client.get(f"/guests/{self.guest_id}")
        assert response.status_code == 200
        assert (
            response.json() == self.dummy_guest_data_converted["guests"][self.guest_id]
        )

    def test_read_guest_not_found(self) -> None:
        """
        Test reading a guest that does not exist.
        """
        guest_id = "nonexistent-id"
        response = self.client.get(f"/guests/{guest_id}")
        assert response.status_code == 404
        assert (
            response.json()["detail"]["error_message"]
            == f"Guest with id {guest_id} not found"
        )

    def test_add_guest(self) -> None:
        """
        Test adding a new guest.
        """
        new_guest = GuestBase(**self.new_guest_dict)
        response = self.client.post("/guests/add-guest", json=new_guest.model_dump())
        assert response.status_code == 200
        assert response.json()["guest_name"] == new_guest.guest_name

    def test_add_guest_already_exists(self) -> None:
        """
        Test adding a guest that already exists.
        """
        existing_guest = self.dummy_guest_data_converted["guests"][self.guest_id]
        response = self.client.post("/guests/add-guest", json=existing_guest)
        assert response.status_code == 409
        assert (
            response.json()["detail"]["error_message"]
            == f"Guest with id {existing_guest['guest_id']} already exists"
        )

    def test_modify_guest(self) -> None:
        """
        Test modifying an existing guest.
        """
        updated_guest = UpdateGuest(
            guest_name=self.update_data["guest_name"],
            guest_contact=self.update_data["guest_contact"],
        )
        response = self.client.put(
            f"/guests/{self.guest_id}", json=updated_guest.model_dump()
        )
        assert response.status_code == 200
        assert response.json()["guest_name"] == updated_guest.guest_name
        assert response.json()["guest_contact"] == updated_guest.guest_contact

    def test_modify_guest_not_found(self) -> None:
        """
        Test modifying a guest that does not exist.
        """
        guest_id = "nonexistent-id"
        updated_guest = UpdateGuest(
            guest_name=self.update_data["guest_name"],
            guest_contact=self.update_data["guest_contact"],
        )
        response = self.client.put(
            f"/guests/{guest_id}", json=updated_guest.model_dump()
        )
        assert response.status_code == 404
        assert (
            response.json()["detail"]["error_message"]
            == f"Guest with id {guest_id} not found"
        )

    def test_remove_guest(self) -> None:
        """
        Test removing a guest.
        """
        response = self.client.delete(f"/guests/{self.guest_id}")
        assert response.status_code == 200
        assert response.json()["guest_id"] == self.guest_id

    def test_remove_guest_not_found(self) -> None:
        """
        Test removing a guest that does not exist.
        """
        guest_id = "nonexistent-id"
        response = self.client.delete(f"/guests/{guest_id}")
        assert response.status_code == 404
        assert (
            response.json()["detail"]["error_message"]
            == f"Guest with id {guest_id} not found"
        )
