from app.data.room_data import RoomData
from app.schemas.room_schema import *
from app.exceptions.room_exceptions import *
from loguru import logger

class RoomService:
    def __init__(self, dummy_room_data: RoomData) -> None:
        self.dummy_room_data = dummy_room_data
        logger.info("RoomService initialized")
    
    def get_room_by_id(self, room_id: int) -> RoomBase:
        response_room = self.dummy_room_data.rooms.get(room_id, None)
        if response_room is None:
            logger.error(f"Room with id {room_id} not found")
            raise RoomNotFoundException(room_id)
        logger.info(f"Room with id {room_id} found: {response_room.model_dump()}")
        return response_room

    def add_room(self, room: RoomBase) -> RoomBase:
        logger.info(f"Received room: {room}")
        if self.dummy_room_data.rooms.get(room.room_id, None):
            logger.error(f"Room with id {room.room_id} already exists")
            raise RoomAlreadyExistsException(room.room_id)
        self.dummy_room_data.rooms[room.room_id] = room
        logger.info(f"Room with id {room.room_id} added: {room.model_dump()}")
        return room 

    def delete_room_by_id(self, room_id: int) -> RoomBase:
        deleted_room = self.dummy_room_data.rooms.pop(room_id, None)
        if deleted_room is None:
            logger.error(f"Room with id {room_id} not found")
            raise RoomNotFoundException(room_id)
        logger.info(f"Room with id {room_id} deleted: {deleted_room.model_dump()}")
        return deleted_room

    def update_room_by_id(self, room_id: int, update_room: UpdateRoom) -> RoomBase:
        response_room = self.get_room_by_id(room_id)
        update_data = update_room.model_dump(exclude_unset=True) # exclude_unset will exclude the data that is not set/updated
        response_room.update(**update_data) # update the data
        logger.info(f"Room with id {room_id} updated: {response_room.model_dump()}")
        return response_room
