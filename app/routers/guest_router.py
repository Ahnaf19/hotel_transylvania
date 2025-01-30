from fastapi import APIRouter, HTTPException
from typing import List
from app.data.guest_data import dummy_guest_data
from ..schemas.guest_schema import GuestBase, GuestHistory

router = APIRouter(prefix="/guests", tags=["guests"])

@router.post("/", response_model=GuestBase)
def create_guest(guest: GuestBase):
    guests.append(guest)
    return guest

@router.get("/", response_model=List[GuestBase])
def get_guests():
    return guests

@router.get("/{guest_id}", response_model=GuestBase)
def get_guest(guest_id: str):
    for guest in guests:
        if guest.guest_id == guest_id:
            return guest
    raise HTTPException(status_code=404, detail="Guest not found")
