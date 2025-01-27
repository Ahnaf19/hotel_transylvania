from fastapi import FastAPI
from app.routers.guest_router import router as guest_router
# from app.exceptions.exceptions import StudentNotFoundException, DuplicateStudentException
# from fastapi.responses import JSONResponse

app = FastAPI()

# Include routers
app.include_router(guest_router)