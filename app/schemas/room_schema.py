from typing import Optional, Dict, List
from pydantic import BaseModel


class RoomBase(BaseModel):
    """
    A class to represent a room in the hotel.
    
    This schema uses Pydantic for data validation and serialization.
    """
    room_id: int
    room_type: str
    room_price: float
    room_is_available: bool
    current_guest_id: Optional[str] = None

    def update(self, **kwargs) -> None:
        """
        Update the attributes of the room with the given keyword arguments.
        
        :param kwargs: Dictionary of attributes to update.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


class RoomData(BaseModel):
    """
    A class to manage multiple rooms in the hotel.
    
    This schema uses Pydantic for data validation and serialization.
    """
    rooms: Dict[int, RoomBase] = {}

    def create_dummy_rooms(self, **dummy_room_data) -> None:
        """
        Create dummy rooms with the provided data.
        
        :param dummy_room_data: Dictionary containing lists of room attributes.
        """
        room_ids = dummy_room_data.get("room_ids", [])
        room_types = dummy_room_data.get("room_types", [])
        room_prices = dummy_room_data.get("room_prices", [])
        room_is_available = dummy_room_data.get("room_is_available", [])

        for i in range(len(room_ids)):
            room = {
                'room_id': int(room_ids[i]),
                'room_type': str(room_types[i]),
                'room_price': float(room_prices[i]),
                'room_is_available': bool(room_is_available[i]),
                'current_guest_id': None
            }
            self.add_dummy_room(room)
            # Hardcoded for testing purposes
            self.rooms[101].current_guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
            self.rooms[101].room_is_available = False

    def add_dummy_room(self, room) -> RoomBase:
        """
        Add a dummy room to the rooms dictionary.
        
        :param room: Dictionary containing room attributes.
        :return: The newly created RoomBase object.
        """
        new_room = RoomBase(**room)
        self.rooms[new_room.room_id] = new_room
        return new_room


class UpdateRoom(BaseModel):
    """
    A class to represent the data required to update a room.
    
    This schema uses Pydantic for data validation and serialization.
    """
    room_id: Optional[int] = None
    room_type: Optional[str] = None
    room_price: Optional[float] = None
    room_is_available: Optional[bool] = None
    current_guest_id: Optional[str] = None