from fastapi import APIRouter, HTTPException
from app.schemas import guest_schema
from app.data.guest_data import dummy_guest_data
# from app.services.guest_service import create_guest, get_guest

router = APIRouter(prefix="/guests", tags=["guests"])

# @router.post("/", response_model=GuestResponse)
# def create_new_guest(guest: GuestCreate):
#     return create_guest(guest)

@router.get("/guests")
async def read_guests():
    return dummy_guest_data
