# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Rental Car Management system

import json # File management
import heapq # Priority queue

class Car: # Car class
    def __init__(self, car_id, type, make, model, availability, rental_price, miles, maintenance): # Initiates all car attributes
        self.car_id = car_id
        self.type = type
        self.make = make
        self.model = model
        self.availability = availability
        self.rental_price = rental_price
        self.miles = miles
        self.maintenance = maintenance

    def rent_car(self): # Changes car availability
        self.availability = False

    def return_car(self): # Changes car availability
        self.availability = True

    def __str__(self): # String representation of object
        return f'Car ID: {self.car_id}, Type: {self.type}, Make: {self.make}, Model: {self.model}, Availability: {self.availability}, Rental Price: {self.rental_price}, Miles: {self.miles}, Maintenance: {self.maintenance}' # Car info string

class Luxury(Car): # Luxury car class
    def __init__(self, car_id, make, model, availability, rental_price, miles, maintenance, vip_discount=0.0): # Initiates car class
        super().__init__(car_id, 'Luxury', make, model, availability, rental_price, miles, maintenance) # Super class reference
        self.vip_discount = vip_discount # Sets VIP discount

    def apply_discount(self, rental_price): # Apply discount function
        return rental_price - (rental_price * self.vip_discount) # Expression to subtract VIP discount percentage from original price

class Electric(Car): # Electric car class
    def __init__(self, car_id, make, model, availability, rental_price, miles, maintenance): # Initiates car class
        super().__init__(car_id, 'Electric', make, model, availability, rental_price, miles, maintenance) # Super class reference

class Customer: # Customer class
    def __init__(self, customer_id, name, contact_info, rental_history=None, vip=False): # Initiates all customer attributes
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = rental_history if rental_history else [] # Sets rental history list to empty if not applicable
        self.vip = vip

    def add_rental(self, car_id): # Function to add car to customer rental history
        self.rental_history.append(car_id) # Appends to history list

    def __str__(self): # String representation of object
        vip_status = "VIP" if self.vip else "Regular" # Sets status of customer
        return f"{self.name} (ID: {self.customer_id}, Status: {vip_status})" # Prints customers info

class VIP(Customer): # VIP customer class
    def __init__(self, customer_id, name, contact_info, rental_history=None, vip=True): # Initiates all customer attributes
        super().__init__(customer_id, name, contact_info, rental_history, vip=vip) # Super class reference

def get_positive_integer_input(prompt): # Integer input validation function
        try:
            value = int(input(prompt)) # Checks for proper integer input
            if value < 0: # Checks for negative numbers
                print("Please enter a positive number.")
                get_positive_integer_input(prompt) # Returns prompt
            else:
                return value # Returns proper integer
        except ValueError: # Checks for nonnumbers
            print("Invalid input! Please enter a valid positive number.")
            get_positive_integer_input(prompt) # Returns prompt

class RentalSystem: # Main rental system class
    def __init__(self): # Initiates all rental attributes
        self.available_cars = []
        self.recently_rented = []
        self.car_db = {}
        self.customer_db = {}
        self.next_car = 1
        self.next_customer = 1

    def add_car(self, type, make, model, rental_price, miles, maintenance, vip_discount=0.0): # Add car function
        car_id = self.next_car
        
        while car_id in self.car_db: # Checks for last used car ID
            car_id += 1
        
        self.next_car = car_id + 1 # Last used car ID plus 1

        if type == 'Luxury': # Checks for Luxury car type
            car = Luxury(car_id, make, model, True, rental_price, miles, maintenance, vip_discount)
        elif type == 'Electric': # Checks for Electric car type
            car = Electric(car_id, make, model, True, rental_price, miles, maintenance)
        else: # All other entries
            car = Car(car_id, type, make, model, True, rental_price, miles, maintenance)

        self.car_db[car_id] = car # Adds to car database
        self.available_cars.append(car) # Adds to available cars

        print(f"New car added with ID: {car_id}") # String confirmation

    def add_customer(self, name, contact_info, vip=False): # Add customer function
        customer_id = self.next_customer
        
        while customer_id in self.customer_db: # Checks for last used customer ID
            customer_id += 1
        
        self.next_customer = customer_id + 1 # Last used customer ID plus 1
        
        customer = Customer(customer_id, name, contact_info, vip=vip) # Checks for user input
        self.customer_db[customer_id] = customer # Adds to customer database

        if vip: # Checks for VIP
            print(f"VIP Customer added with ID: {customer_id}")
        else: # All other customers
            print(f"Regular Customer added with ID: {customer_id}")

    def view_customer_rental_history(self, customer_id): # Customer history function
        customer = self.customer_db.get(customer_id) # Gets customer ID
        if not customer: # Input validation
            print(f"Customer with ID {customer_id} not found.")
            return
        
        if not customer.rental_history: # Checks for no rental history
            print(f"{customer.name} has no rental history.")
        else:
            print(f"Rental History for {customer.name} (ID: {customer.customer_id}):")
            for car_id in customer.rental_history: # Repeats for all cars in rental history
                car = self.car_db.get(car_id) # Sets ID to car
                if car: # Prints for every entry
                    print(f"Car ID: {car.car_id}, Make: {car.make}, Model: {car.model}")
                else: # Validates car ID
                    print(f"Car ID: {car_id} not found in the system.")

    def load_data(self): # Loads data
        try:
            with open('carinfo.json', 'r') as f: # Opens car file
                cars_data = json.load(f) # Converts json string to python string
                for car_data in cars_data: # Checks for all cars available
                    if car_data.get('type') == 'Luxury': # Checks for Luxury car type
                        car = Luxury( # Assigns all information
                        car_data['car_id'],
                        car_data['make'],
                        car_data['model'],
                        car_data['availability'],
                        car_data['rental_price'],
                        car_data['miles'],
                        car_data['maintenance'],
                        car_data.get('vip_discount', 0.0)
                        )
                    elif car_data.get('type') == 'Electric': # Checks for Electric car type
                        car = Electric( # Assigns all information
                        car_data['car_id'],
                        car_data['make'],
                        car_data['model'],
                        car_data['availability'],
                        car_data['rental_price'],
                        car_data['miles'],
                        car_data['maintenance']
                        )
                    else: # All other car types
                        car = Car( # Assigns all information
                        car_data['car_id'],
                        car_data['type'],
                        car_data['make'],
                        car_data['model'],
                        car_data['availability'],
                        car_data['rental_price'],
                        car_data['miles'],
                        car_data['maintenance']
                    )
                    
                    self.car_db[car.car_id] = car # Adds to car database
                    if car.availability: # Checks for car availability
                        self.available_cars.append(car) # Adds to available cars list
                        
        except FileNotFoundError: # Checks for car file
            print(f'Car file not found.')

        try:
            with open('customerinfo.json', 'r') as f: # Opens customer file
                customers_data = json.load(f) # Converts json string to python string
                for customer_data in customers_data: # Checks for all customers available
                    if customer_data.get('vip', False): # Checks for VIP customer
                        customer = VIP( # Assigns all information
                            customer_data['customer_id'],
                            customer_data['name'],
                            customer_data['contact_info'],
                            customer_data.get('rental_history', []),
                            vip = customer_data.get('vip', False)
                        )
                    else: # All other customers
                        customer = Customer( # Assigns all information
                            customer_data['customer_id'],
                            customer_data['name'],
                            customer_data['contact_info'],
                            customer_data.get('rental_history', [])
                        )
                    self.customer_db[customer.customer_id] = customer # Adds to customer database
        except FileNotFoundError: # Checks for customer file
            print(f'Customer file not found.')

    def rent_car(self, customer_id, car_id): # Rent car function
        customer = self.customer_db.get(customer_id) # Get customer from database using ID
        car = self.car_db.get(car_id) # Gets car from database using ID

        if not customer: # Input validation
            print(f'Customer not found.')
            return
        
        if not car or not car.availability: # Input validation
            print(f'Car {car_id} is not available.')
            return

        car.rent_car() # Calls rent car function again
        customer.add_rental(car_id) # Adds rental car to customer rental history

        self.available_cars.remove(car) # Removes car from available car list
        self.recently_rented.append(car) # Adds car to rented car list
        
        print(f'Car {car_id} rented to {customer.name}.') # Confirmation string
        
        if isinstance(car, Luxury) and isinstance(customer, VIP): # Checks for VIP customer and Luxury car
            discounted_price = car.apply_discount(car.rental_price) # Applies VIP discount
            print(f'VIP discount: {discounted_price}') # Prints discounted price

    def return_car(self, car_id): # Return car function
        car = self.car_db.get(car_id) # Gets car from database using ID
        if not car: # Input validation
            print(f'Car {car_id} not found.')
            return

        car.return_car() # Calls return car function
        
        self.available_cars.append(car) # Adds car to available car list
        self.recently_rented.remove(car) # Removes car from rented car list
        
        print(f"\nCar {car_id} has been returned and is now available for rent.\n") # Confirmation string

        update = input("Do you want to update the miles and maintenance for this car? (y/n): ").strip().lower() # Prompts editing mileage and maintenance schedule
        if update == 'y': # Checks for user input
            new_miles = get_positive_integer_input("Enter the new miles: ") # Prompts user for new mileage
            new_maintenance = get_positive_integer_input("Enter the new maintenance schedule: ") # Prompts user for new maintenance mile schedule amount
            
            car.miles = int(new_miles) # Applies changes to car miles
            car.maintenance = new_maintenance # Applies changes to car maintenance

            if car.miles > car.maintenance: # Checks for mileage greater than car maintenance schedule
                print(f"Warning: Car {car_id} has exceeded its maintenance mile schedule amount.") # Prints maintenance warning
                return
            
            print(f"Car ID {car_id} miles and maintenance updated.") # Confirmation of updated info
            return
        else:
            print("No updates made to the car.") # No further updates made
            return

    def save_cars(self): # Save cars function
        cars_data = [] # Empty car list
        for car in self.car_db.values(): # Checks for all cars in database
            car_info = { # Applies car information in preparation for list
                'car_id': car.car_id,
                'type': car.type,
                'make': car.make,
                'model': car.model,
                'availability': car.availability,
                'rental_price': car.rental_price,
                'miles': car.miles,
                'maintenance': car.maintenance,
            }
            if isinstance(car, Luxury): # Checks for Luxury car type
                car_info['vip_discount'] = car.vip_discount # Applies VIP discount
            cars_data.append(car_info) # Adds car info to list

        with open('carinfo.json', 'w') as f: # Writes list into car json file
            json.dump(cars_data, f, indent=4)

    def save_customers(self): # Saves customers function
        customers_data = [] # Empty customers list
        for customer in self.customer_db.values(): # Checks for all customers in database
            customer_info = { # Applies customer information in preparation for list
                'customer_id': customer.customer_id,
                'name': customer.name,
                'contact_info': customer.contact_info,
                'rental_history': customer.rental_history,
                'vip': getattr(customer, 'vip', False) # Checks for VIP status
            }
            customers_data.append(customer_info) # Adds customer info to list

        with open('customerinfo.json', 'w') as f: # Writes list into customer json file
            json.dump(customers_data, f, indent=4)

    def report(self): # Report function
        for car in self.car_db.values(): # Repeats for all cars in database
            status = "Rented" if car in self.recently_rented else "Available" # Sets status of cars based on recently rented list
            print(f"Car ID: {car.car_id}, Type: {car.type}, Make: {car.make}, Model: {car.model}, Status: {status}") # Prints all cars with rented status
