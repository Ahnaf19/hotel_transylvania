from fastapi import FastAPI
from app.routers.guest_router import router as guest_router
from app.routers.room_router import router as room_router

app = FastAPI()

# Include routers
app.include_router(guest_router)
app.include_router(room_router)


if __name__ == "__main__":
    print('main.py running explicitly')