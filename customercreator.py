import json

customer_info = [ # Creates list of customers for testing
    {
        "customer_id": 1,
        "name": "John Doe",
        "contact_info": "johndoe@gmail.com",
        "vip": True
    },
    {
        "customer_id": 2,
        "name": "Jane Smith",
        "contact_info": "janesmith@yahoo.com",
        "vip": False
    },
    {
        "customer_id": 3,
        "name": "Joey Doe",
        "contact_info": "john@hotmail.com",
        "vip": False
    },
    {
        "customer_id": 4,
        "name": "Jeff Doe",
        "contact_info": "jeff@gmail.com",
        "vip": True
    }
]

json_object = json.dumps(customer_info, indent=4) # Converts customer list into json format

with open('customerinfo.json', 'w') as f: # Writes converted customer list into json file
    f.write(json_object)
