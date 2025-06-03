# training_data_inventory.py

TRAINING_DATA = [
    (
        "Move productX to gap3",
        {
            "entities": [(5, 13, "PRODUCT"), (17, 22, "LOCATION_TO")],
            "cats": {
                "move_product": 1.0,
                "check_product": 0.0,
                "add_product": 0.0,
                "delete_product": 0.0,
                "update_stock": 0.0
            }
        }
    ),
    (
        "Make a report of the productX",
        {
            "entities": [(21, 29, "PRODUCT")],
            "cats": {
                "move_product": 0.0,
                "check_product": 1.0,
                "add_product": 0.0,
                "delete_product": 0.0,
                "update_stock": 0.0
            }
        }
    ),
    (
        "Add productX to inventory",
        {
            "entities": [(4, 12, "PRODUCT"), (16, 25, "LOCATION_TO")],
            "cats": {
                "move_product": 0.0,
                "check_product": 0.0,
                "add_product": 1.0,
                "delete_product": 0.0,
                "update_stock": 0.0
            }
        }
    ),
    (
        "Add 15 units to productX",
        {
            "entities": [(4, 13, "STOCK"), (17, 25, "PRODUCT")],
            "cats": {
                "move_product": 0.0,
                "check_product": 0.0,
                "add_product": 0.0,
                "delete_product": 0.0,
                "update_stock": 1.0
            }
        }
    ),
    (
        "Delete productX from inventory",
        {
            "entities": [(7, 15, "PRODUCT"), (21, 30, "LOCATION_FROM")],
            "cats": {
                "move_product": 0.0,
                "check_product": 0.0,
                "add_product": 0.0,
                "delete_product": 1.0,
                "update_stock": 0.0
            }
        }
    )
]
