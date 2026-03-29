from fastapi import APIRouter
from controllers import shipment_controller
from controllers import shipment_controller, tracking_controller



router = APIRouter()

router.include_router(shipment_controller.router)
router.include_router(shipment_controller.router)
router.include_router(tracking_controller.router)