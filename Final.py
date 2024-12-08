# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Rental Car Management system.

import queue
import datetime
import json

class Car:
    def __init__(self, car_id, make, model, cost, available=True):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.cost = cost
        self.available = available
        self.due_date = None

    def rent_car(self, rental_days):
        if self.available:
            self.available = False
            self.due_date = datetime.datetime.now() + datetime.timedelta(days=rental_days)
            return f'Car {self.car_id} has been rented for {rental_days} days.'
        else:
            return f'Car not available.'

class Customer:
    def __init__(self, customer_id, name, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []
