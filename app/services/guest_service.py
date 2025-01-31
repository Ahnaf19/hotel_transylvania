from app.schemas.guest_schema import GuestData, GuestBase, UpdateGuest
from app.exceptions.guest_exceptions import GuestNotFoundException, GuestAlreadyExistsException
from loguru import logger


class GuestService:
    """
    Service class to handle guest operations.
    """

    def __init__(self, dummy_guest_data: GuestData) -> None:
        """
        Initialize the GuestService with dummy guest data.

        :param dummy_guest_data: GuestData object containing dummy guest data.
        """
        self.dummy_guest_data = dummy_guest_data
        logger.debug("GuestService initialized")
    
    def get_guest_by_id(self, guest_id: str) -> GuestBase:
        """
        Retrieve a guest by their ID.

        :param guest_id: ID of the guest to retrieve.
        :return: GuestBase object representing the guest.
        :raises GuestNotFoundException: If the guest with the given ID is not found.
        """
        # Attempt to retrieve the guest from the dummy data
        response_guest = self.dummy_guest_data.guests.get(guest_id, None)
        if response_guest is None:
            # Log an error and raise an exception if the guest is not found
            logger.error(f"Guest with id {guest_id} not found")
            raise GuestNotFoundException(guest_id)
        # Log the found guest and return it
        logger.debug(f"Guest with id {guest_id} found: {response_guest.model_dump()}")
        return response_guest

    def add_guest(self, guest: GuestBase) -> GuestBase:
        """
        Add a new guest.

        :param guest: GuestBase object representing the guest to add.
        :return: GuestBase object representing the added guest.
        :raises GuestAlreadyExistsException: If a guest with the same ID already exists.
        """
        logger.debug(f"Received guest: {guest}")
        # Check if a guest with the same ID already exists
        if self.dummy_guest_data.guests.get(guest.guest_id, None):
            # Log an error and raise an exception if the guest already exists
            logger.error(f"Guest with id {guest.guest_id} already exists")
            raise GuestAlreadyExistsException(guest.guest_id)
        # Add the new guest to the dummy data
        self.dummy_guest_data.guests[guest.guest_id] = guest
        logger.debug(f"Guest with id {guest.guest_id} added: {guest.model_dump()}")
        return guest 

    def delete_guest_by_id(self, guest_id: str) -> GuestBase:
        """
        Delete a guest by their ID.

        :param guest_id: ID of the guest to delete.
        :return: GuestBase object representing the deleted guest.
        :raises GuestNotFoundException: If the guest with the given ID is not found.
        """
        # Attempt to delete the guest from the dummy data
        deleted_guest = self.dummy_guest_data.guests.pop(guest_id, None)
        if deleted_guest is None:
            # Log an error and raise an exception if the guest is not found
            logger.error(f"Guest with id {guest_id} not found")
            raise GuestNotFoundException(guest_id)
        # Log the deleted guest and return it
        logger.debug(f"Guest with id {guest_id} deleted: {deleted_guest.model_dump()}")
        return deleted_guest

    def update_guest_by_id(self, guest_id: str, update_guest: UpdateGuest) -> GuestBase:
        """
        Update a guest by their ID.

        :param guest_id: ID of the guest to update.
        :param update_guest: UpdateGuest object containing the updated guest data.
        :return: GuestBase object representing the updated guest.
        :raises GuestNotFoundException: If the guest with the given ID is not found.
        """
        # Retrieve the existing guest
        response_guest = self.get_guest_by_id(guest_id)
        # Extract the update data, excluding unset fields
        update_data = update_guest.model_dump(exclude_unset=True)
        # Update the guest data with the new values
        response_guest.update(**update_data)
        logger.debug(f"Guest with id {guest_id} updated: {response_guest.model_dump()}")
        return response_guest
