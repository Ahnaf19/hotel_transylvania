from app.data.room_data import dummy_room_data #, RoomData
from app.schemas.room_schema import UpdateRoom
from app.exceptions.room_exceptions import *

class RoomService:
    @staticmethod
    def get_room_by_id(room_id: int):
        # assert isinstance(dummy_room_data, RoomData)  # ? how to resolve dtype issue without this assertion?
        response = dummy_room_data.rooms.get(room_id, None) #TODO implement custom exception if room_id not found
        if response is None:
            raise RoomNotFoundException(room_id)
        return response

    @staticmethod
    def add_room(room):
        # assert isinstance(dummy_room_data, RoomData)
        if dummy_room_data.rooms.get(room["room_id"], None):
            raise RoomAlreadyExistsException(room["room_id"])
        dummy_room_data.rooms[room["room_id"]] = room
        print(f"Room with id {room['room_id']} added")
        return room

    @staticmethod
    def delete_room_by_id(room_id: int):
        response = dummy_room_data.rooms.pop(room_id, None)
        if response is None:
            raise RoomNotFoundException(room_id)
        print(f"Room with id {room_id} deleted")
        return response

    @staticmethod
    def update_room_by_id(room_id: int, update_room: UpdateRoom):
        response_room = RoomService.get_room_by_id(room_id)
        update_data = update_room.model_dump(exclude_unset=True) # exclude_unset will exclude the data that is not set/updated
        response_room.update(**update_data) # update the data
        return response_room