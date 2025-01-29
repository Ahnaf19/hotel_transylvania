from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.guest_router import router as guest_router
from app.routers.room_router import router as room_router
# from app.exceptions.custom_exceptions import RoomNotFoundException

app = FastAPI()

# # Custom exception handler
# @app.exception_handler(RoomNotFoundException)
# async def room_not_found_exception_handler(request, exc: RoomNotFoundException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail},
#     )

# Include routers
app.include_router(guest_router)
app.include_router(room_router)


if __name__ == "__main__":
    print('main.py running explicitly')