from repositories import tracking_repository
from models.tracking_model import create_tracking_model
from repositories import shipment_repository

def add_update(shipment_id, location, status):
    tracking = create_tracking_model(shipment_id, location, status)
    
    tracking_repository.add_tracking_update(tracking)
    
    shipment_repository.update_status(shipment_id, status)

    return {"message": "Tracking updated"}


def get_updates(shipment_id):
    return tracking_repository.get_tracking_updates(shipment_id)