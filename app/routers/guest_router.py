from fastapi import APIRouter

from app.data.guest_data import dummy_guest_data
from app.schemas.guest_schema import GuestBase, GuestData, UpdateGuest
from app.services.guest_service import GuestService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/guests", tags=["guests"])

# Initiate the GuestService with dummy data
guest_service = GuestService(dummy_guest_data)


# Define the routes
@router.get("/", response_model=GuestData)
async def read_guests() -> GuestData:
    """
    Retrieve all guests.

    Returns:
        GuestData: A list of all guests.
    """
    return guest_service.dummy_guest_data


@router.get("/{guest_id}", response_model=GuestBase)
async def read_guest(guest_id: str) -> GuestBase:
    """
    Retrieve a guest by their ID.

    Args:
        guest_id (str): The ID of the guest to retrieve.

    Returns:
        GuestBase: The guest data.
    """
    return guest_service.get_guest_by_id(guest_id)


@router.post("/add-guest", response_model=GuestBase)
async def add_guest(guest: GuestBase) -> GuestBase:
    """
    Add a new guest.

    Args:
        guest (GuestBase): The guest data to add.

    Returns:
        GuestBase: The added guest data.
    """
    return guest_service.add_guest(guest)


@router.delete(
    "/{guest_id}",
    response_model=GuestBase,
    responses={
        200: {"description": "Guest deleted"},
        404: {"description": "Guest not found"},
    },
)
async def remove_guest(guest_id: str) -> GuestBase:
    """
    Remove a guest by their ID.

    Args:
        guest_id (str): The ID of the guest to remove.

    Returns:
        GuestBase: The removed guest data.
    """
    return guest_service.delete_guest_by_id(guest_id)


@router.put("/{guest_id}", response_model=GuestBase)
async def modify_guest(guest_id: str, updated_guest: UpdateGuest) -> GuestBase:
    """
    Modify a guest by their ID.

    Args:
        guest_id (str): The ID of the guest to modify.
        updated_guest (UpdateGuest): The updated guest data.

    Returns:
        GuestBase: The modified guest data.
    """
    return guest_service.update_guest_by_id(guest_id, updated_guest)
