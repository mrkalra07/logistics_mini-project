from fastapi import APIRouter
from services import tracking_service

router = APIRouter()

# Agent adds update
@router.post("/tracking/{tracking_number}")
def add_tracking(tracking_number: str, data: dict):
    location = data.get("location")
    status = data.get("status")

    return tracking_service.add_update(tracking_number, location, status)


# Get tracking history
@router.get("/tracking/{tracking_number}")
def get_tracking(tracking_number: str):
    return tracking_service.get_updates(tracking_number)