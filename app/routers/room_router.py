from fastapi import APIRouter
from app.data.room_data import dummy_room_data
from app.services.room_service import RoomService
from app.schemas.room_schema import *
from app.exceptions.room_exceptions import RoomNotFoundException

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/")
async def read_rooms():
    return dummy_room_data

@router.get("/{room_id}", response_model=RoomBase)
async def read_room(room_id: int):
    return RoomService.get_room_by_id(room_id)

@router.post("/add-room", response_model=RoomBase)
async def add_room(room: RoomBase):
    return RoomService.add_room(room.model_dump())

@router.delete("/{room_id}", response_model=RoomBase, responses={200: {"description": "Room deleted"}, 404: {"description": "Room not found"}})
async def remove_room(room_id: int):
    return RoomService.delete_room_by_id(room_id)

@router.put("/{room_id}")
async def modify_room(room_id: int, updated_room: UpdateRoom):
    return RoomService.update_room_by_id(room_id, updated_room)
