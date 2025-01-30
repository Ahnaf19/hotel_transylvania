from fastapi import FastAPI
from app.routers.guest_router import router as guest_router
from app.routers.room_router import router as room_router

# Create an instance of the FastAPI application
app = FastAPI()

# Include routers for guest and room endpoints
app.include_router(guest_router)
app.include_router(room_router)

def main() -> None:
    """
    Entry point for the application when run explicitly.
    """
    print('main.py running explicitly')

if __name__ == "__main__":
    main()