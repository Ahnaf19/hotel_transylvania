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
    
class UpdateRoom(BaseModel):
    room_id: Optional[int] = None
    room_type: Optional[str] = None
    room_price: Optional[float] = None
    room_is_available: Optional[bool] = None
    current_guest_id: Optional[str] = None    