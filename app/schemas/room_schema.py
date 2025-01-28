from typing import Optional
from pydantic import BaseModel

class RoomBase(BaseModel):
    room_id: int
    room_type: str
    room_price: float
    room_is_available: bool
    current_guest_id: Optional[str] = None