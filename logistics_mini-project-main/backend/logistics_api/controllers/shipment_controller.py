from fastapi import APIRouter
from services import shipment_service

router = APIRouter()

@router.post("/shipments")
def create(data: dict):
    return shipment_service.create_shipment(data)


@router.get("/shipments/{tracking_number}")
def track(tracking_number: str):
    shipment = shipment_service.track_shipment(tracking_number)

    if shipment:
        return shipment
    return {"error": "Shipment not found"}