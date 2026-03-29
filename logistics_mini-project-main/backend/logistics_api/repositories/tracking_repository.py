from core.database import db

tracking_collection = db["tracking"]

def add_tracking_update(data):
    tracking_collection.insert_one(data)
    return data


def get_tracking_updates(shipment_id):
    updates = tracking_collection.find(
        {"shipment_id": shipment_id},
        {"_id": 0}
    )

    return list(updates)