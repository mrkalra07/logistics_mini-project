import random
from models.shipment_model import create_shipment_model
from repositories import shipment_repository

def generate_tracking():
    return "TRK" + str(random.randint(10000, 99999))


def create_shipment(data):
    tracking_number = generate_tracking()

    shipment = create_shipment_model(data, tracking_number)

    return shipment_repository.insert_shipment(shipment)


def track_shipment(tracking_number):
    return shipment_repository.get_shipment(tracking_number)