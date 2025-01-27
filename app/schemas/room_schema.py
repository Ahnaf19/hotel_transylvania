from uuid import UUID
from pydantic import BaseModel

class RoomSchema(BaseModel):
    room_id: UUID
    room_type: str
    room_price: float
    room_is_available: bool