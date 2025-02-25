import sys

from fastapi import File, HTTPException, UploadFile
from loguru import logger

from app.exceptions.room_exceptions import (
    InvalidImageFileException,
    RoomAlreadyExistsException,
    RoomNotFoundException,
)
from app.schemas.room_schema import RoomBase, RoomData, UpdateRoom, UploadImageResponse


class RoomService:
    """
    Service class to handle room operations!
    """

    def __init__(self, dummy_room_data: RoomData) -> None:
        """
        Initialize the RoomService with dummy room data.

        :param dummy_room_data: RoomData object containing dummy room data.
        """
        self.dummy_room_data = dummy_room_data
        logger.debug("RoomService initialized")

    def get_room_by_id(self, room_id: int) -> RoomBase:
        """
        Retrieve a room by its ID.

        :param room_id: ID of the room to retrieve.
        :return: RoomBase object representing the room.
        :raises RoomNotFoundException: If the room with the given ID is not found.
        """
        response_room = self.dummy_room_data.rooms.get(room_id, None)
        if response_room is None:
            logger.error(f"Room with id {room_id} not found")
            raise RoomNotFoundException(room_id)
        logger.debug(f"Room with id {room_id} found: {response_room.model_dump()}")
        return response_room

    def add_room(self, room: RoomBase) -> RoomBase:
        """
        Add a new room.

        :param room: RoomBase object representing the room to add.
        :return: RoomBase object representing the added room.
        :raises RoomAlreadyExistsException: If a room with the same ID already exists.
        """
        logger.debug(f"Received room: {room}")
        if self.dummy_room_data.rooms.get(room.room_id, None):
            logger.error(f"Room with id {room.room_id} already exists")
            raise RoomAlreadyExistsException(room.room_id)
        self.dummy_room_data.rooms[room.room_id] = room
        logger.debug(f"Room with id {room.room_id} added: {room.model_dump()}")
        return room

    def delete_room_by_id(self, room_id: int) -> RoomBase:
        """
        Delete a room by its ID.

        :param room_id: ID of the room to delete.
        :return: RoomBase object representing the deleted room.
        :raises RoomNotFoundException: If the room with the given ID is not found.
        """
        deleted_room = self.dummy_room_data.rooms.pop(room_id, None)
        if deleted_room is None:
            logger.error(f"Room with id {room_id} not found")
            raise RoomNotFoundException(room_id)
        logger.debug(f"Room with id {room_id} deleted: {deleted_room.model_dump()}")
        return deleted_room

    def update_room_by_id(self, room_id: int, update_room: UpdateRoom) -> RoomBase:
        """
        Update a room by its ID.

        :param room_id: ID of the room to update.
        :param update_room: UpdateRoom object containing the updated room data.
        :return: RoomBase object representing the updated room.
        :raises RoomNotFoundException: If the room with the given ID is not found.
        """
        response_room = self.get_room_by_id(room_id)
        update_data = update_room.model_dump(
            exclude_unset=True
        )  # Exclude data that is not set/updated
        response_room.update(**update_data)  # Update the room data
        logger.debug(f"Room with id {room_id} updated: {response_room.model_dump()}")
        return response_room

    async def upload_image(self, file: UploadFile = File(...)):
        """
        Uploads an image file.
        Args:
            file (UploadFile): The image file to be uploaded. Must be of type 'image/*'.
        Raises:
            InvalidImageFileException: If the uploaded file is not an image.
            HTTPException: If an error occurs during the upload process.
        Returns:
            UploadImageResponse: A response object containing the file name and file size.
        """
        if file.content_type is None or not file.content_type.startswith("image/"):
            raise InvalidImageFileException

        try:
            response_dict = {
                "file_name": file.filename,
                "file_size": file.size,
            }

            return UploadImageResponse(**response_dict)

        except Exception as error:
            logger.exception(error)
            e = sys.exc_info()[1]
            raise HTTPException(status_code=500, detail=str(e))
