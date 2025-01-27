from fastapi import FastAPI
from app.routers.guest_router import router as guest_router
from app.routers.room_router import router as room_router
# from app.exceptions.exceptions import StudentNotFoundException, DuplicateStudentException

app = FastAPI()

# Include routers
app.include_router(guest_router)
app.include_router(room_router)