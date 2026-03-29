def create_shipment_model(data, tracking_number):
    return {
        "tracking_number": tracking_number,
        "customer_name": data.get("customer_name"),
        "source": data.get("source"),
        "destination": data.get("destination"),
        "status": "created"
    }