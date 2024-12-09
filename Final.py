# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Rental Car Management system.

import queue
import random
import datetime
import json

# Base Car Class
class Car:
    def __init__(self, car_id, model, make, rental_price, available=True):
        self.car_id = car_id
        self.model = model
        self.make = make
        self.rental_price = rental_price
        self.available = available
        self.due_date = None  # When car is due for return

    def rent_car(self, rental_days):
        if self.available:
            self.available = False
            self.due_date = datetime.datetime.now() + datetime.timedelta(days=rental_days)
            return f"Car {self.car_id} rented for {rental_days} days."
        else:
            return "Car not available."

    def return_car(self):
        if not self.available:
            self.available = True
            self.due_date = None
            return f"Car {self.car_id} returned."
        else:
            return "Car already available."

    def __str__(self):
        return f"{self.car_id} - {self.model} - {self.make} - ${self.rental_price} per day"

# LuxuryCar subclass inheriting from Car
class LuxuryCar(Car):
    def __init__(self, car_id, model, make, rental_price, vip_discount=0.1):
        super().__init__(car_id, model, make, rental_price)
        self.vip_discount = vip_discount  # Discount for VIP customers

    def rent_car(self, rental_days, is_vip=False):
        if is_vip:
            self.rental_price *= (1 - self.vip_discount)
        return super().rent_car(rental_days)

# ElectricCar subclass inheriting from Car
class ElectricCar(Car):
    def __init__(self, car_id, model, make, rental_price, battery_life=100):
        super().__init__(car_id, model, make, rental_price)
        self.battery_life = battery_life  # Battery percentage

    def rent_car(self, rental_days):
        if self.battery_life < 20:
            return "Car needs charging before renting."
        return super().rent_car(rental_days)

# Customer Class
class Customer:
    def __init__(self, customer_id, name, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def rent_car(self, car, rental_days):
        if car.available:
            car.rent_car(rental_days)
            self.rental_history.append(car.car_id)
            return f"Customer {self.name} rented car {car.car_id}."
        else:
            return f"Car {car.car_id} is not available."

# Queue to manage available cars
class CarQueue:
    def __init__(self):
        self.available_cars = queue.Queue()

    def add_car(self, car):
        self.available_cars.put(car)

    def rent_car(self):
        if not self.available_cars.empty():
            car = self.available_cars.get()
            car.available = False
            return car
        else:
            return None  # No cars available

    def return_car(self, car):
        car.available = True
        self.available_cars.put(car)

# Stack to manage recently rented cars
class CarStack:
    def __init__(self):
        self.recently_rented = []

    def push(self, car):
        self.recently_rented.append(car)

    def pop(self):
        if self.recently_rented:
            return self.recently_rented.pop()
        return None

# BST for rental due dates
class RentalDueDateBST:
    class Node:
        def __init__(self, car):
            self.car = car
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, car):
        self.root = self._insert(self.root, car)

    def _insert(self, node, car):
        if node is None:
            return self.Node(car)
        if car.due_date < node.car.due_date:
            node.left = self._insert(node.left, car)
        else:
            node.right = self._insert(node.right, car)
        return node

    def find_due_cars(self, due_date):
        return self._find_due_cars(self.root, due_date)

    def _find_due_cars(self, node, due_date):
        if node is None:
            return []
        cars = []
        if node.car.due_date <= due_date:
            cars.append(node.car)
        cars.extend(self._find_due_cars(node.left, due_date))
        cars.extend(self._find_due_cars(node.right, due_date))
        return cars

    def display_due_cars(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is None:
            return []
        return self._inorder_traversal(node.left) + [node.car] + self._inorder_traversal(node.right)

# Sorting Cars by rental price
def quick_sort(cars, key=lambda car: car.rental_price):
    if len(cars) <= 1:
        return cars
    pivot = cars[random.randint(0, len(cars)-1)]
    left = [car for car in cars if key(car) < key(pivot)]
    right = [car for car in cars if key(car) > key(pivot)]
    middle = [car for car in cars if key(car) == key(pivot)]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# File Handling for reading and saving car and customer data
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, default=str)
