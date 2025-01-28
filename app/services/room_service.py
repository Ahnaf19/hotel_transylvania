from app.data.room_data import dummy_room_data, RoomData

class RoomService:
    @staticmethod
    def get_room_by_id(room_id: int):
        assert isinstance(dummy_room_data, RoomData)  # ? how to resolve dtype issue without this assertion?
        response = dummy_room_data.rooms.get(room_id, None) #TODO implement custom exception if room_id not found
        return response

    @staticmethod
    def add_room(room):
        assert isinstance(dummy_room_data, RoomData)
        dummy_room_data.rooms[room["room_id"]] = room
        return room

    # @staticmethod
    # def delete_room_by_id(room_id: int):
    #     dummy_room_data = [room for room in dummy_room_data if room["id"] != room_id]
    #     return {"message": f"Room with id {room_id} deleted"}

    # @staticmethod
    # def update_room_by_id(room_id: int, updated_room: dict):
    #     for index, room in enumerate(dummy_room_data):
    #         if room["id"] == room_id:
    #             dummy_room_data[index].update(updated_room)
    #             return dummy_room_data[index]
    #     return None
