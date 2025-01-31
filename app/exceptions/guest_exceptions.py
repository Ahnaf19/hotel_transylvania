from fastapi import HTTPException


class GuestNotFoundException(HTTPException):
    """
    Exception raised when a guest with the specified ID is not found.

    Attributes:
        guest_id (str): ID of the guest that was not found.
    """
    def __init__(self, guest_id: str):
        """
        Initialize the GuestNotFoundException with the given guest ID.

        Args:
            guest_id (str): ID of the guest that was not found.
        """
        detail = {
            "error_message": f"Guest with id {guest_id} not found",
            "guest_id": guest_id
        }
        # Call the parent constructor with a 404 status code and the detail message
        super().__init__(status_code=404, detail=detail)
        
class GuestAlreadyExistsException(HTTPException):
    """
    Exception raised when a guest with the specified ID already exists.

    Attributes:
        guest_id (str): ID of the guest that already exists.
    """
    def __init__(self, guest_id: str):
        """
        Initialize the GuestAlreadyExistsException with the given guest ID.

        Args:
            guest_id (str): ID of the guest that already exists.
        """
        detail = {
            "error_message": f"Guest with id {guest_id} already exists",
            "guest_id": guest_id
        }
        # Call the parent constructor with a 409 status code and the detail message
        super().__init__(status_code=409, detail=detail)
