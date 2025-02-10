from fastapi.testclient import TestClient
from loguru import logger

from app.data.room_data import dummy_room_data
from app.main import app
from app.schemas.room_schema import RoomBase, UpdateRoom


class TestRoomRouter:
    client: TestClient
    new_room_dict: dict
    update_data: dict

    @classmethod
    def setup_class(cls) -> None:
        """
        Setup the test client and initial data for the tests.
        """
        cls.client = TestClient(app)
        cls.new_room_dict = {
            "room_id": 106,
            "room_type": "King",
            "room_price": 3500.0,
            "room_is_available": True,
        }
        cls.update_data = {"room_type": "Updated Type", "room_price": 2600.0}

    def test_read_rooms(self) -> None:
        """
        Test reading all rooms.
        """
        response = self.client.get("/rooms/")
        # Convert the dummy_room_data to a dictionary to match with FastAPI JSON response
        dummy_room_data_converted = {
            "rooms": {str(k): v.model_dump() for k, v in dummy_room_data.rooms.items()}
        }
        assert response.status_code == 200
        logger.debug(response.json())
        logger.debug(dummy_room_data_converted)
        assert response.json() == dummy_room_data_converted

    def test_read_room(self) -> None:
        """
        Test reading a specific room by ID.
        """
        for test_room_id in [101, 102]:
            response = self.client.get(f"/rooms/{test_room_id}")
            assert response.status_code == 200
            assert response.json()["room_id"] == test_room_id
            if test_room_id == 102:  # * testing harcoded portion
                assert (
                    response.json()["current_guest_id"]
                    == "23159162-dd67-4a2a-8054-d6be6c0379ca"
                )
                assert response.json()["room_is_available"] == False

    def test_read_room_not_found(self) -> None:
        """
        Test reading a room that does not exist.
        """
        room_id = 999
        response = self.client.get(f"/rooms/{room_id}")
        assert response.status_code == 404
        assert (
            response.json()["detail"]["error_message"]
            == f"Room with id {room_id} not found"
        )

    def test_add_room(self) -> None:
        """
        Test adding a new room.
        """
        new_room = RoomBase(**self.new_room_dict)
        response = self.client.post("/rooms/add-room", json=new_room.model_dump())
        assert response.status_code == 200
        assert response.json()["room_id"] == new_room.room_id

    def test_add_room_already_exists(self) -> None:
        """
        Test adding a room that already exists.
        """
        room_id = 101
        response = self.client.get(f"/rooms/{room_id}")
        assert response.status_code == 200
        existing_room = RoomBase(**response.json())
        response = self.client.post("/rooms/add-room", json=existing_room.model_dump())
        assert response.status_code == 409
        assert (
            response.json()["detail"]["error_message"]
            == f"Room with id {existing_room.room_id} already exists"
        )

    def test_remove_room(self) -> None:
        """
        Test removing a room.
        """
        room_id = 105
        response = self.client.delete(f"/rooms/{room_id}")
        assert response.status_code == 200
        assert response.json()["room_id"] == room_id

    def test_remove_room_not_found(self) -> None:
        """
        Test removing a room that does not exist.
        """
        room_id = 999
        response = self.client.delete(f"/rooms/{room_id}")
        assert response.status_code == 404
        assert (
            response.json()["detail"]["error_message"]
            == f"Room with id {room_id} not found"
        )

    def test_modify_room(self) -> None:
        """
        Test modifying an existing room.
        """
        room_id = 104
        updated_room = UpdateRoom(**self.update_data)
        response = self.client.put(f"/rooms/{room_id}", json=updated_room.model_dump())
        assert response.status_code == 200
        assert response.json()["room_type"] == updated_room.room_type
        assert response.json()["room_price"] == updated_room.room_price

    def test_modify_room_not_found(self) -> None:
        """
        Test modifying a room that does not exist.
        """
        room_id = 999
        updated_room = UpdateRoom(**self.update_data)
        response = self.client.put(f"/rooms/{room_id}", json=updated_room.model_dump())
        assert response.status_code == 404
        assert (
            response.json()["detail"]["error_message"]
            == f"Room with id {room_id} not found"
        )
