# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Rental Car Management system.

import json

class Car:
    def __init__(self, car_id, type, make, model, availability, rental_price, miles, maintenance):
        self.car_id = car_id
        self.type = type
        self.make = make
        self.model = model
        self.availability = availability
        self.rental_price = rental_price
        self.miles = miles
        self.maintenance = maintenance

    def rent_car(self):
        self.availability = False

    def return_car(self):
        self.availability = True

    def maintenance_due(self, mileage):
        return mileage >= self.maintenance

    def __str__(self):
        return f'Car ID: {self.car_id}, Type: {self.type}, Make: {self.make}, Model: {self.model}, Availability: {self.availability}, Rental Price: {self.rental_price}, Miles: {self.miles}, Maintenance: {self.maintenance}'

class Luxury(Car):
    def __init__(self, car_id, make, model, availability, rental_price, maintenance, vip_discount):
        super().__init__(car_id, make, model, availability, rental_price, maintenance)
        self.vip_discount = vip_discount

    def apply_discount(self, rental_price):
        return rental_price - (rental_price * self.vip_discount)

class
