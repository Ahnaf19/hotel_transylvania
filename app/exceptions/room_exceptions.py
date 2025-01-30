from fastapi import HTTPException

class RoomNotFoundException(HTTPException):
    """
    Exception raised when a room with the specified ID is not found.

    Attributes:
        room_id (int): ID of the room that was not found.
    """
    def __init__(self, room_id: int):
        """
        Initialize the RoomNotFoundException with the given room ID.

        Args:
            room_id (int): ID of the room that was not found.
        """
        detail = {
            "error_message": f"Room with id {room_id} not found",
            "room_id": room_id
        }
        # Call the parent constructor with a 404 status code and the detail message
        super().__init__(status_code=404, detail=detail)
        
class RoomAlreadyExistsException(HTTPException):
    """
    Exception raised when a room with the specified ID already exists.

    Attributes:
        room_id (int): ID of the room that already exists.
    """
    def __init__(self, room_id: int):
        """
        Initialize the RoomAlreadyExistsException with the given room ID.

        Args:
            room_id (int): ID of the room that already exists.
        """
        detail = {
            "error_message": f"Room with id {room_id} already exists",
            "room_id": room_id
        }
        # Call the parent constructor with a 409 status code and the detail message
        super().__init__(status_code=409, detail=detail)