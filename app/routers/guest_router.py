from fastapi import APIRouter
from app.data.guest_data import dummy_guest_data

router = APIRouter(prefix="/guests", tags=["guests"])

# @router.post("/", response_model=GuestResponse)
# def create_new_guest(guest: GuestCreate):
#     return create_guest(guest)

@router.get("/")
async def read_guests():
    return dummy_guest_data
