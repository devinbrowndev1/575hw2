from DialogFrameSimple import DialogFrameSimple

class Database:
    customers = {"1234567890": {"pizza_type": "hawaiian",
                      "pizza_size": "small",
                      "pizza_crust": "deep-dish",
                      "pizza_cost": 0,
                      "order_name": "Jessica",
                      "order_phone": "1234567890",
                      "order_address": "",
                      "order_delivery": "pick-up",
                      "order_wait": 20,
                      "confirmed": False},
                 "0987654321": {"pizza_type": "vegan",
                      "pizza_size": "medium",
                      "pizza_crust": "regular",
                      "pizza_cost": 0,
                      "order_name": "Devin",
                      "order_phone": "0987654321",
                      "order_address": "195 Stevens Way",
                      "order_delivery": "delivery",
                      "order_wait": 20,
                      "confirmed": False}}