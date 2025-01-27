from uuid import UUID
from pydantic import BaseModel

class RoomBase(BaseModel):
    room_id: int
    room_type: str
    room_price: float
    room_is_available: bool
    current_guest_id: str | None = None
    
class RoomData:
    guest: list[RoomBase]