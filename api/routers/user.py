from fastapi import APIRouter,FastAPI
from api.controller import user as controller

# Define Route for the all user request

router = APIRouter(tags=["Users"])

# Apply the middleware to the router
# router.middleware(response_handler)


@router.get("/users")
async def get_users():
    return controller.get_users()

