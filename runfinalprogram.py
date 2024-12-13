# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Runs Rental Car Program

from Final import RentalSystem

def main(): # Main function
    rental_system = RentalSystem() # Links class to variable

    # Load the data
    rental_system.load_data() # Initializes information

    recursive_menu(rental_system) # Calls recursive menu

def display_menu(): # Menu function that prints all options
    print("\n-- Rental Car Management System --\n")
    print("1. Rent a Car")
    print("2. Return a Car")
    print("3. View Available Cars")
    print("4. View Rented Cars")
    print("5. View Customers")
    print("6. Sort and View Car Data")
    print("7. Sort and View Customer Data")
    print("8. Add Car")
    print("9. Remove Car")
    print("10. Add Customer")
    print("11. Remove Customer")
    print("12. Report")
    print("13. Exit")
    print("14. Exit Without Saving\n")

def recursive_menu(rental_system): # Recursive menu function
    display_menu() # Calls display menu function

    choice = input("Choose an option: ") # User input for menu

    if choice == '1':
        rent_car_interface(rental_system)
    elif choice == '2':
        return_car_interface(rental_system)
    elif choice == '3':
        view_available_cars(rental_system)
    elif choice == '4':
        view_rented_cars(rental_system)
    elif choice == '5':
        view_customers(rental_system)
    elif choice == '6':
        sort_and_display_cars(rental_system)
    elif choice == '7':
        sort_and_display_customers(rental_system)
    elif choice == '8':
        add_car(rental_system)
    elif choice == '9':
        remove_car(rental_system)
    elif choice == '10':
        add_customer(rental_system)
    elif choice == '11':
        remove_customer(rental_system)
    elif choice == '12':
        report_interface(rental_system)
    elif choice == '13':
        save_car_data(rental_system) # Saves car data
        save_customer_data(rental_system) # Saves customer data
        print("\nSaving and quitting.")
        return  # Ends recursion
    elif choice == '14':
        print("Quitting without saving.")
        return  # Ends recursion
    else:
        print("Invalid option. Please try again.") # Input validation

    recursive_menu(rental_system) # Recursive menu calling

def rent_car_interface(rental_system): # Car rental interface
    print("\n--- Rent a Car ---")
    view_customers(rental_system) # Prints all customers to select
    customer_id = get_positive_integer_input("Enter customer ID: ") # User input for customer ID with input validation
    view_available_cars(rental_system) # Prints all available cars to select
    car_id = get_positive_integer_input("Enter car ID: ") # User input for car ID with input validation
    rental_system.rent_car(customer_id, car_id) # Returns user inputs into rental function

def return_car_interface(rental_system): # Car return interface
    print("\n-- Return a Car --\n")
    car_id = get_positive_integer_input("Enter car ID to return: ") # User input for car ID with input validation
    rental_system.return_car(car_id) # Returns car ID to return function
    print()

def view_available_cars(rental_system): # Displays available cars
    print("\n-- Available Cars --\n")
    available_cars = [car for car in rental_system.available_cars] # Selects all available cars
    if not available_cars: # Checks for no cars available
        print("No cars available.")
    else:
        for car in available_cars: # Prints available cars
            print(car)
    print()

def view_rented_cars(rental_system): # Displays rented cars
    print("\n-- Rented Cars --\n")
    rented_cars = rental_system.recently_rented # Selects all rented cars
    if not rented_cars: # Checks for no rented cars
        print("No cars rented.")
    else:
        for car in rented_cars: # Prints all rented cars
            print(car)
    print()

def view_customers(rental_system): # Displays all customers
    print("\n-- Customers --\n")
    for customer in rental_system.customer_db.values(): # Selects all customers
        vip_status = "VIP" if customer.vip else "Regular" # Checks for vip status of customers
        print(f'{customer.name} (ID: {customer.customer_id}, Status: {vip_status})') # Prints all customer's info
    print()

def sort_and_display_cars(rental_system): # Sorting cars menu
    print("\n-- Sorting Cars by --")
    print("1. Car ID")
    print("2. Type")
    print("3. Make")
    print("4. Model")
    print("5. Rental Price")
    print("6. Miles")
    print("7. Maintenance\n")
    choice = input("Choose an option: ") # User input for above choices

    if choice == '1':
        key = lambda car: car.car_id
    elif choice == '2':
        key = lambda car: car.type
    elif choice == '3':
        key = lambda car: car.make
    elif choice == '4':
        key = lambda car: car.model
    elif choice == '5':
        key = lambda car: car.rental_price
    elif choice == '6':
        key = lambda car: car.miles
    elif choice == '7':
        key = lambda car: car.maintenance
    else:
        print("Invalid option. Please try again.") # Input validation
        return

    sorted_cars = sorted(rental_system.car_db.values(), key=key) # Sorts cars based off choice
    for car in sorted_cars: # Prints all cars in sorted order
        print(f"Car ID: {car.car_id}, Type: {car.type}, Make: {car.make}, Model: {car.model}, "
              f"Rental Price: {car.rental_price}, Miles: {car.miles}, Maintenance: {car.maintenance}")

def sort_and_display_customers(rental_system): # Sorting customers menu
    print("\n-- Sort and Search --")
    print("1. Customer ID")
    print("2. Name")
    print("3. Contact Info")
    print("4. Rental History")
    choice = input("Choose an option: ") # User input for above choices

    if choice == '1':
        key = lambda customer: customer.customer_id
    elif choice == '2':
        key = lambda customer: customer.name
    elif choice == '3':
        key = lambda customer: customer.contact_info
    elif choice == '4':
        customer_id = int(input("Enter customer ID to view rental history: "))
        rental_system.view_customer_rental_history(customer_id)
        return
    else:
        print("Invalid option!")
        return

    sorted_customers = sorted(rental_system.customer_db.values(), key=key) # Sorts customers based off choice
    for customer in sorted_customers: # Prints all customers
        vip_status = "VIP" if getattr(customer, 'vip', False) else "Regular"
        print(f"{customer.name} (ID: {customer.customer_id}), Contact Information: {customer.contact_info}, Status: {vip_status}")

def add_car(rental_system): # Add car function
    print("\n-- Add a New Car --\n")
    car_type = input("Enter car type (Luxury, Electric, Regular): ").capitalize() # User input for car type
    make = input("Enter car make: ") # User input for make
    model = input("Enter car model: ") # User input for model
    rental_price = float(input("Enter rental price: ")) # User input for rental cost
    miles = int(input("Enter miles driven: ")) # User input for mileage
    maintenance = int(input("Enter maintenance miles schedule: ")) # User input for maintenance schedule

    vip_discount = 0.0 # Sets VIP discount to 0
    if car_type == 'Luxury': # User input for VIP discount if applicable
        vip_discount = float(input("Enter VIP discount for Luxury car: "))

    rental_system.add_car(car_type, make, model, rental_price, miles, maintenance, vip_discount) # Adds final car entry into list

def remove_car(rental_system): # Remove car function
    print("\n-- Remove a Car --\n")
    car_id = int(input("Enter car ID to remove: ")) # User prompt for car ID to delete
    if car_id in rental_system.car_db: # Checks for correct ID
        confirmation = input(f"Are you sure you want to delete car with ID {car_id}? (y/n): ") # Confirmation before deletion
        if confirmation.lower() == 'y':
            car = rental_system.car_db.pop(car_id) # Removes car from car database
            if car in rental_system.available_cars:
                rental_system.available_cars.remove(car) # Removes car from available list
            if car in rental_system.recently_rented:
                rental_system.recently_rented.remove(car) # Removes car from recently rented list
            print(f"Car with ID {car_id} removed successfully.") # Confirmation
        else:
            print("Car removal canceled.") # Cancellation
    else:
        print("Car not found.") # Input validation

def add_customer(rental_system): # Add customer function
    print("\n-- Add a New Customer --\n")
    name = input("Enter customer's name: ") # User input for customer name
    contact_info = input("Enter customer's contact info (Email): ") # User input for email
    vip_status_input = input("Is the customer a VIP? (y/n): ").strip().lower() # User input for VIP

    vip_status = vip_status_input == 'y' # Changes VIP status if applicable

    rental_system.add_customer(name, contact_info, vip_status) # Returns info to list

def remove_customer(rental_system): # Remove customer function
    print("\n-- Remove a Customer --\n")
    customer_id = int(input("Enter customer ID to remove: ")) # User input for customer ID
    if customer_id in rental_system.customer_db: # Checks for correct ID
        confirmation = input(f"Are you sure you want to delete customer with ID {customer_id}? (y/n): ") # Confirmation to delete
        if confirmation.lower() == 'y':
            rental_system.customer_db.pop(customer_id) # Removes customer from customer database
            print(f"Customer with ID {customer_id} removed successfully.") # Confirmation
        else:
            print("Customer removal canceled.") # Cancellation
    else:
        print("Customer not found.") # Input validation

def save_car_data(rental_system): # Save car data function
    print("\n-- Saving Car Data --")
    rental_system.save_cars() # Saves cars
    print("Car data saved to 'carinfo.json'.") # Confirmation

def save_customer_data(rental_system): # Save customer data function
    print("\n-- Saving Customer Data --")
    rental_system.save_customers() # Saves customers
    print("Customer data saved to 'customerinfo.json'.") # Confirmation

def report_interface(rental_system): # Rental report function
    print("\n-- Report --\n")
    rental_system.report() # Calls report function

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

if __name__ == "__main__":
