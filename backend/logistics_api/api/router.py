from fastapi import APIRouter
from controllers import shipment_controller

router = APIRouter()

router.include_router(shipment_controller.router)