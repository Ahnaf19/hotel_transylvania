from app.schemas import room_schema

room_data_local = {
    "room_ids": [101, 102, 103, 104, 105],
    "room_types": ["Single", "Double", "Triple", "Quad", "Queen"],
    "room_prices": [1000.0, 1500.0, 2000.0, 2500.0, 3000.0],
    "room_is_available": [True, True, True, True, True],
}

# initialize the dummy guest data
dummy_room_data = room_schema.RoomData()
dummy_room_data.create_dummy_rooms(**room_data_local)

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
