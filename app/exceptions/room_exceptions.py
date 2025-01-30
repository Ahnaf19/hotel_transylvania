from fastapi import HTTPException

class RoomNotFoundException(HTTPException):
    def __init__(self, room_id: int):
        detail = {
            "error_message": f"Room with id {room_id} not found",
            "room_id": room_id
        }
        super().__init__(status_code=404, detail=detail)
        
class RoomAlreadyExistsException(HTTPException):
    def __init__(self, room_id: int):
        detail = {
            "error_message": f"Room with id {room_id} already exists",
            "room_id": room_id
        }
        super().__init__(status_code=409, detail=detail)