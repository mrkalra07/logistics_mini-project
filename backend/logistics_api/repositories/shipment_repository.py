from core.database import shipments_collection

def insert_shipment(shipment):
    shipments_collection.insert_one(shipment)
    return shipment


def get_shipment(tracking_number):
    return shipments_collection.find_one(
        {"tracking_number": tracking_number},
        {"_id": 0}
    )