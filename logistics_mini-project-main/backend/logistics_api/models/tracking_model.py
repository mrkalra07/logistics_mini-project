from datetime import datetime

def create_tracking_model(shipment_id, location, status):
    return {
        "shipment_id": shipment_id,
        "location": location,
        "status": status,
        "updated_at": datetime.now()
    }