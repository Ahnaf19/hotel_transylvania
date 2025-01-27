from fastapi import APIRouter
from app.data.room_data import dummy_room_data

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/")
async def read_rooms():
    return dummy_room_data
