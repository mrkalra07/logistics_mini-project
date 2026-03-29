from core.database import shipments_collection
from bson import ObjectId

def insert_shipment(shipment):
    result = shipments_collection.insert_one(shipment)
    shipment["_id"] = str(result.inserted_id)
    return shipment


def get_shipment(tracking_number):
    shipment = shipments_collection.find_one(
        {"tracking_number": tracking_number},
        {"_id": 0}
    )
    return shipment

def update_status(tracking_number, status):
    shipments_collection.update_one(
        {"tracking_number": tracking_number},
        {"$set": {"status": status}}
    )