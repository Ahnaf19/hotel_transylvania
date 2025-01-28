from app.schemas import room_schema

    
class RoomData:
    def __init__(self):
        self.rooms: dict[int, room_schema.RoomBase] = {}
        self.create_rooms()
        
        # add dummy_guest to room 101
        # ! Hardcoded for testing purposes
        self.rooms[101].current_guest_id = "23159162-dd67-4a2a-8054-d6be6c0379ca"
        self.rooms[101].room_is_available = False
    
    def create_rooms(self):
        room_ids = [101, 102, 103, 104, 105]
        room_types = ["Single", "Double", "Triple", "Quad", "Queen"]
        room_prices = [1000.0, 1500.0, 2000.0, 2500.0, 3000.0]
        room_is_available = [True, True, True, True, True]
        
        for i in range(len(room_ids)):
            room = {
                'room_id': room_ids[i],
                'room_type': room_types[i],
                'room_price': room_prices[i],
                'room_is_available': room_is_available[i],
                'current_guest_id': None
            }
            self.add_dummy_room(room)

    def add_dummy_room(self, room):
        new_room = room_schema.RoomBase(**room) # * pydantic isn't designed to work with positional arguments
        self.rooms[new_room.room_id] = new_room
        return new_room

# initialize the dummy guest data
dummy_room_data = RoomData()

if __name__ == "__main__":
    room = dummy_room_data.rooms[101]
    print(f"Room ID: {room.room_id}")
    print(f"Room Type: {room.room_type}")
    print(f"Room Price: {room.room_price}")
    print(f"Room Availability: {room.room_is_available}")
    print(f"Current Guest ID: {room.current_guest_id}")
    print("\n")
    print(type(dummy_room_data))
    print(type(dummy_room_data.rooms))
    print(type(dummy_room_data.rooms[101]))
