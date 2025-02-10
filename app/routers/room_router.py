from fastapi import APIRouter

from app.data.room_data import dummy_room_data
from app.schemas.room_schema import *
from app.services.room_service import RoomService

# Initialize the router
router = APIRouter(prefix="/rooms", tags=["rooms"])

# Initiate the RoomService with dummy data
room_service = RoomService(dummy_room_data)


# Define the routes
@router.get("/", response_model=RoomData)
async def read_rooms() -> RoomData:
    """
    Retrieve all rooms.

    Returns:
        RoomData: A list of all rooms.
    """
    return room_service.dummy_room_data


@router.get("/{room_id}", response_model=RoomBase)
async def read_room(room_id: int) -> RoomBase:
    """
    Retrieve a room by its ID.

    Args:
        room_id (int): The ID of the room to retrieve.

    Returns:
        RoomBase: The room data.
    """
    return room_service.get_room_by_id(room_id)


@router.post("/add-room", response_model=RoomBase)
async def add_room(room: RoomBase) -> RoomBase:
    """
    Add a new room.

    Args:
        room (RoomBase): The room data to add.

    Returns:
        RoomBase: The added room data.
    """
    return room_service.add_room(room)


@router.delete(
    "/{room_id}",
    response_model=RoomBase,
    responses={
        200: {"description": "Room deleted"},
        404: {"description": "Room not found"},
    },
)
async def remove_room(room_id: int) -> RoomBase:
    """
    Remove a room by its ID.

    Args:
        room_id (int): The ID of the room to remove.

    Returns:
        RoomBase: The removed room data.
    """
    return room_service.delete_room_by_id(room_id)


@router.put("/{room_id}", response_model=RoomBase)
async def modify_room(room_id: int, updated_room: UpdateRoom) -> RoomBase:
    """
    Modify a room by its ID.

    Args:
        room_id (int): The ID of the room to modify.
        updated_room (UpdateRoom): The updated room data.

    Returns:
        RoomBase: The modified room data.
    """
    return room_service.update_room_by_id(room_id, updated_room)
