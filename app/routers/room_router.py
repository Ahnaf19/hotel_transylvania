from fastapi import APIRouter, HTTPException
from app.data.room_data import dummy_room_data
from app.services.room_service import RoomService
from app.schemas.room_schema import RoomBase

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/")
async def read_rooms():
    return dummy_room_data

@router.get("/{room_id}")
async def read_room(room_id: int):
    return RoomService.get_room_by_id(room_id)

@router.post("/add-room", response_model=RoomBase)
async def add_room(room: RoomBase):
    return RoomService.add_room(room.model_dump())

# @router.delete("/{room_id}")
# async def remove_room(room_id: int):
#     result = RoomService.delete_room_by_id(room_id)
#     if result is None:
#         raise HTTPException(status_code=404, detail="Room not found")
#     return result

# @router.put("/{room_id}")
# async def modify_room(room_id: int, updated_room: dict):
#     room = RoomService.update_room_by_id(room_id, updated_room)
#     if room is None:
#         raise HTTPException(status_code=404, detail="Room not found")
#     return room
