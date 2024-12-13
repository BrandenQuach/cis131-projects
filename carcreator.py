import json

car_info = [ # Creates list of cars for testing
    {
        "car_id": 1,
        "type": "Luxury",
        "make": "Tesla",
        "model": "Model S",
        "availability": True,
        "rental_price": 100,
        "miles": 4500,
        "maintenance": 8000,
        "vip_discount": 0.1
    },
    {
        "car_id": 2,
        "type": "Electric",
        "make": "Nissan",
        "model": "Leaf",
        "availability": True,
        "rental_price": 50,
        "miles": 55000,
        "maintenance": 60000
    },
    {
        "car_id": 3,
        "type": "Regular",
        "make": "Ford",
        "model": "Mustang",
        "availability": True,
        "rental_price": 150,
        "miles": 12000,
        "maintenance": 15000
    },
    {
        "car_id": 4,
        "type": "Regular",
        "make": "Toyota",
        "model": "Camry",
        "availability": True,
        "rental_price": 100,
        "miles": 22000,
        "maintenance": 25000
    }
]

json_object = json.dumps(car_info, indent=4) # Converts car list into json format

with open('carinfo.json', 'w') as f: # Writes converted car list into json file
    f.write(json_object)
