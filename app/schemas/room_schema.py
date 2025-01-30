from typing import Optional
from pydantic import BaseModel


class RoomBase(BaseModel):
    room_id: int
    room_type: str
    room_price: float
    room_is_available: bool
    current_guest_id: Optional[str] = None
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

class RoomData(BaseModel):
    rooms: dict[int, RoomBase] = {}
    
    def create_dummy_rooms(self, **dummy_room_data: dict): # ? can we control the constructor to call this method?
        room_ids = dummy_room_data.get("room_ids", [])
        room_types = dummy_room_data.get("room_types", [])
        room_prices = dummy_room_data.get("room_prices", [])
        room_is_available = dummy_room_data.get("room_is_available", [])
        
        for i in range(len(room_ids)):
            room = {
                'room_id': room_ids[i],
                'room_type': room_types[i],
                'room_price': room_prices[i],
                'room_is_available': room_is_available[i],
                'current_guest_id': None
            }
            self.add_dummy_room(room)
            # ! Hardcoded for testing purposes
            self.rooms[101].current_guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
            self.rooms[101].room_is_available = False
    
    def add_dummy_room(self, room: dict):
        new_room = RoomBase(**room) # * pydantic isn't designed to work with positional arguments
        self.rooms[new_room.room_id] = new_room
        return new_room
            
class UpdateRoom(BaseModel):
    room_id: Optional[int] = None
    room_type: Optional[str] = None
    room_price: Optional[float] = None
    room_is_available: Optional[bool] = None
    current_guest_id: Optional[str] = None    