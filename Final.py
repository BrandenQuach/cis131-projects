# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Rental Car Management system

import json
import heapq

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
    def __init__(self, car_id, make, model, availability, rental_price, miles, maintenance, vip_discount=0.0):
        super().__init__(car_id, 'Luxury', make, model, availability, rental_price, miles, maintenance)
        self.vip_discount = vip_discount

    def apply_discount(self, rental_price):
        return rental_price - (rental_price * self.vip_discount)

class Electric(Car):
    def __init__(self, car_id, make, model, availability, rental_price, miles, maintenance):
        super().__init__(car_id, 'Electric', make, model, availability, rental_price, miles, maintenance)

class Customer:
    def __init__(self, customer_id, name, contact_info, rental_history=None, vip=False):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = rental_history if rental_history else []
        self.vip = vip

    def add_rental(self, car_id):
        self.rental_history.append(car_id)

    def __str__(self):
        vip_status = "VIP" if self.vip else "Regular"
        return f"{self.name} (ID: {self.customer_id}, Status: {vip_status})"

class VIP(Customer):
    def __init__(self, customer_id, name, contact_info, rental_history=None, vip=True):
        super().__init__(customer_id, name, contact_info, rental_history, vip=vip)

def get_positive_integer_input(prompt):
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                get_positive_integer_input(prompt)
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid positive number.")
            get_positive_integer_input(prompt)

class RentalSystem:
    def __init__(self):
        self.available_cars = []
        self.recently_rented = []
        self.car_db = {}
        self.customer_db = {}
        self.next_car = 1
        self.next_customer = 1

    def add_car(self, type, make, model, rental_price, miles, maintenance, vip_discount=0.0):
        car_id = self.next_car
        
        while car_id in self.car_db:
            car_id += 1
        
        self.next_car = car_id + 1

        if type == 'Luxury':
            car = Luxury(car_id, make, model, True, rental_price, miles, maintenance, vip_discount)
        elif type == 'Electric':
            car = Electric(car_id, make, model, True, rental_price, miles, maintenance)
        else:
            car = Car(car_id, type, make, model, True, rental_price, miles, maintenance)

        self.car_db[car_id] = car
        self.available_cars.append(car)

        print(f"New car added with ID: {car_id}")

    def add_customer(self, name, contact_info, vip=False):
        customer_id = self.next_customer
        
        while customer_id in self.customer_db:
            print(f"Customer ID {customer_id} already exists. Incrementing ID.")
            customer_id += 1
        
        self.next_customer = customer_id + 1
        
        customer = Customer(customer_id, name, contact_info, vip=vip)
        self.customer_db[customer_id] = customer

        if vip:
            print(f"VIP Customer added with ID: {customer_id}")
        else:
            print(f"Regular Customer added with ID: {customer_id}")

    def view_customer_rental_history(self, customer_id):
        """View the rental history of a customer."""
        customer = self.customer_db.get(customer_id)
        if not customer:
            print(f"Customer with ID {customer_id} not found.")
            return
        
        if not customer.rental_history:
            print(f"{customer.name} has no rental history.")
        else:
            print(f"Rental History for {customer.name} (ID: {customer.customer_id}):")
            for car_id in customer.rental_history:
                car = self.car_db.get(car_id)
                if car:
                    print(f"Car ID: {car.car_id}, Make: {car.make}, Model: {car.model}")
                else:
                    print(f"Car ID: {car_id} not found in the system.")

    def load_data(self):
        try:
            with open('carinfo.json', 'r') as f:
                cars_data = json.load(f)
                for car_data in cars_data:
                    if car_data.get('type') == 'Luxury':
                        car = Luxury(
                        car_data['car_id'],
                        car_data['make'],
                        car_data['model'],
                        car_data['availability'],
                        car_data['rental_price'],
                        car_data['miles'],
                        car_data['maintenance'],
                        car_data.get('vip_discount', 0.0)
                        )
                    elif car_data.get('type') == 'Electric':
                        car = Electric(
                        car_data['car_id'],
                        car_data['make'],
                        car_data['model'],
                        car_data['availability'],
                        car_data['rental_price'],
                        car_data['miles'],
                        car_data['maintenance']
                        )
                    else:
                        car = Car(
                        car_data['car_id'],
                        car_data['type'],
                        car_data['make'],
                        car_data['model'],
                        car_data['availability'],
                        car_data['rental_price'],
                        car_data['miles'],
                        car_data['maintenance']
                    )
                    
                    self.car_db[car.car_id] = car
                    if car.availability:
                        self.available_cars.append(car)
                        
        except FileNotFoundError:
            print(f'Car file not found.')

        try:
            with open('customerinfo.json', 'r') as f:
                customers_data = json.load(f)
                for customer_data in customers_data:
                    if customer_data.get('vip', False):
                        customer = VIP(
                            customer_data['customer_id'],
                            customer_data['name'],
                            customer_data['contact_info'],
                            customer_data.get('rental_history', []),
                            vip = customer_data.get('vip', False)
                        )
                    else:
                        customer = Customer(
                            customer_data['customer_id'],
                            customer_data['name'],
                            customer_data['contact_info'],
                            customer_data.get('rental_history', [])
                        )
                    self.customer_db[customer.customer_id] = customer
        except FileNotFoundError:
            print(f'Customer file not found.')

    def rent_car(self, customer_id, car_id):
        customer = self.customer_db.get(customer_id)
        car = self.car_db.get(car_id)

        if not customer:
            print(f'Customer not found.')
            return
        
        if not car or not car.availability:
            print(f'Car {car_id} is not available.')
            return

        car.rent_car()
        customer.add_rental(car_id)

        self.available_cars.remove(car)
        self.recently_rented.append(car)
        
        print(f'Car {car_id} rented to {customer.name}.')
        
        if isinstance(car, Luxury) and isinstance(customer, VIP):
            discounted_price = car.apply_discount(car.rental_price)
            print(f'VIP discount: {discounted_price}')

    def return_car(self, car_id):
        car = self.car_db.get(car_id)
        if not car:
            print(f'Car {car_id} not found.')
            return

        car.return_car()
        
        self.available_cars.append(car)
        self.recently_rented.remove(car)
        
        print(f"\nCar {car_id} has been returned and is now available for rent.\n")

        update = input("Do you want to update the miles and maintenance for this car? (y/n): ").strip().lower()
        if update == 'y':
            new_miles = get_positive_integer_input("Enter the new miles: ")
            new_maintenance = get_positive_integer_input("Enter the new maintenance threshold: ")
            
            car.miles = new_miles
            car.maintenance = new_maintenance

            if car.miles > car.maintenance:
                print(f"Warning: Car {car_id} has exceeded its maintenance threshold!")
                return
            
            print(f"Car ID {car_id} miles and maintenance updated.")
            return
        else:
            print("No updates made to the car.")
            return

    def save_cars(self):
        cars_data = []
        for car in self.car_db.values():
            car_info = {
                'car_id': car.car_id,
                'type': car.type,
                'make': car.make,
                'model': car.model,
                'availability': car.availability,
                'rental_price': car.rental_price,
                'miles': car.miles,
                'maintenance': car.maintenance,
            }
            if isinstance(car, Luxury):
                car_info['vip_discount'] = car.vip_discount
            cars_data.append(car_info)

        with open('carinfo.json', 'w') as f:
            json.dump(cars_data, f, indent=4)

    def save_customers(self):
        customers_data = []
        for customer in self.customer_db.values():
            customer_info = {
                'customer_id': customer.customer_id,
                'name': customer.name,
                'contact_info': customer.contact_info,
                'rental_history': customer.rental_history,
                'vip': getattr(customer, 'vip', False)
            }
            customers_data.append(customer_info)

        with open('customerinfo.json', 'w') as f:
            json.dump(customers_data, f, indent=4)

    def report(self):
        for car in self.car_db.values():
            status = "Rented" if car in self.recently_rented else "Available"
            print(f"Car ID: {car.car_id}, Type: {car.type}, Make: {car.make}, Model: {car.model}, Status: {status}")
