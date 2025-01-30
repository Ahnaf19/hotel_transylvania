from fastapi import APIRouter
from app.data.room_data import RoomData, dummy_room_data
from app.services.room_service import RoomService
from app.schemas.room_schema import *

# Initialize the router
router = APIRouter(prefix="/rooms", tags=["rooms"])

# initiate the RoomService
room_service = RoomService(dummy_room_data)

# define the routes
@router.get("/")
async def read_rooms() -> RoomData:
    return room_service.dummy_room_data

@router.get("/{room_id}", response_model=RoomBase)
async def read_room(room_id: int) -> RoomBase:
    return room_service.get_room_by_id(room_id)

@router.post("/add-room", response_model=RoomBase)
async def add_room(room: RoomBase) -> RoomBase:
    return room_service.add_room(room)

@router.delete("/{room_id}", response_model=RoomBase, responses={200: {"description": "Room deleted"}, 404: {"description": "Room not found"}})
async def remove_room(room_id: int) -> RoomBase:
    return room_service.delete_room_by_id(room_id)

@router.put("/{room_id}")
async def modify_room(room_id: int, updated_room: UpdateRoom) -> RoomBase:
    return room_service.update_room_by_id(room_id, updated_room)
