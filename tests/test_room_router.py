import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.data.room_data import dummy_room_data
from app.schemas.room_schema import RoomBase, UpdateRoom
from loguru import logger

class TestRoomRouter:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        cls.new_room_dict = {
            "room_id": 106,
            "room_type": "King",
            "room_price": 3500.0,
            "room_is_available": True
        }
        cls.update_data = {
            "room_type": "Updated Type",
            "room_price": 2600.0
        }

    def test_read_rooms(self):
        response = self.client.get("/rooms/")
        dummy_room_data_serialized = dummy_room_data.model_dump_json()
        assert response.status_code == 200
        logger.info(response.json())
        logger.info(dummy_room_data_serialized)
        assert response.json() == dummy_room_data_serialized

    def test_read_room(self):
        test_room_id = 101
        response = self.client.get(f"/rooms/{test_room_id}")
        assert response.status_code == 200
        assert response.json()["room_id"] == test_room_id

    def test_read_room_not_found(self):
        room_id = 999
        response = self.client.get(f"/rooms/{room_id}")
        assert response.status_code == 404
        assert response.json()["detail"]["error_message"] == f"Room with id {room_id} not found"

    def test_add_room(self):
        new_room = RoomBase(**self.new_room_dict)
        response = self.client.post("/rooms/add-room", json=new_room.model_dump())
        assert response.status_code == 200
        assert response.json()["room_id"] == new_room.room_id

    def test_add_room_already_exists(self):
        room_id = 101
        response = self.client.get(f"/rooms/{room_id}")
        assert response.status_code == 200
        existing_room = RoomBase(**response.json())
        response = self.client.post("/rooms/add-room", json=existing_room.model_dump())
        assert response.status_code == 409
        assert response.json()["detail"]["error_message"] == f"Room with id {existing_room.room_id} already exists"

    def test_remove_room(self):
        room_id = 105
        response = self.client.delete(f"/rooms/{room_id}")
        assert response.status_code == 200
        assert response.json()["room_id"] == room_id

    def test_remove_room_not_found(self):
        room_id = 999
        response = self.client.delete(f"/rooms/{room_id}")
        assert response.status_code == 404
        assert response.json()["detail"]["error_message"] == f"Room with id {room_id} not found"

    def test_modify_room(self):
        room_id = 104
        updated_room = UpdateRoom(**self.update_data)
        response = self.client.put(f"/rooms/{room_id}", json=updated_room.model_dump())
        assert response.status_code == 200
        assert response.json()["room_type"] == updated_room.room_type
        assert response.json()["room_price"] == updated_room.room_price

    def test_modify_room_not_found(self):
        room_id = 999
        updated_room = UpdateRoom(**self.update_data)
        response = self.client.put(f"/rooms/{room_id}", json=updated_room.model_dump())
        assert response.status_code == 404
        assert response.json()["detail"]["error_message"] == f"Room with id {room_id} not found"
