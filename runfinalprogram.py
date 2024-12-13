# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Runs Rental Car Program

from Final import RentalSystem

def main():
    rental_system = RentalSystem()

    # Load the data
    rental_system.load_data()

    recursive_menu(rental_system)

def display_menu():
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

def recursive_menu(rental_system):
    # Display the menu
    display_menu()

    # Get user input for the menu option
    choice = input("Choose an option: ")

    # Handle user choices recursively
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
        save_car_data(rental_system)
        save_customer_data(rental_system)
        print("\nSaving and quitting.")
        return  # End the program (exit recursion)
    elif choice == '14':
        print("Quitting without saving.")
        return  # End the program (exit recursion)
    else:
        print("Invalid option. Please try again.")

    # Recursively call the menu again to repeat the process
    recursive_menu(rental_system)

def rent_car_interface(rental_system):
    print("\n--- Rent a Car ---")
    view_customers(rental_system)
    customer_id = get_positive_integer_input("Enter customer ID: ")
    view_available_cars(rental_system)
    car_id = get_positive_integer_input("Enter car ID: ")
    rental_system.rent_car(customer_id, car_id)

def return_car_interface(rental_system):
    print("\n-- Return a Car --\n")
    car_id = get_positive_integer_input("Enter car ID to return: ")
    rental_system.return_car(car_id)
    print()

def view_available_cars(rental_system):
    print("\n-- Available Cars --\n")
    available_cars = [car for car in rental_system.available_cars]
    if not available_cars:
        print("No cars available.")
    else:
        for car in available_cars:
            print(car)
    print()

def view_rented_cars(rental_system):
    print("\n-- Rented Cars --\n")
    rented_cars = rental_system.recently_rented
    if not rented_cars:
        print("No cars rented.")
    else:
        for car in rented_cars:
            print(car)
    print()

def view_customers(rental_system):
    print("\n-- Customers --\n")
    for customer in rental_system.customer_db.values():
        vip_status = "VIP" if customer.vip else "Regular"
        print(f'{customer.name} (ID: {customer.customer_id}, Status: {vip_status})')
    print()

def sort_and_display_cars(rental_system):
    print("\n-- Sorting Cars by --")
    print("1. Car ID")
    print("2. Type")
    print("3. Make")
    print("4. Model")
    print("5. Rental Price")
    print("6. Miles")
    print("7. Maintenance\n")
    choice = input("Choose an option: ")

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
        print("Invalid option!")
        return

    sorted_cars = sorted(rental_system.car_db.values(), key=key)
    for car in sorted_cars:
        print(f"Car ID: {car.car_id}, Type: {car.type}, Make: {car.make}, Model: {car.model}, "
              f"Rental Price: {car.rental_price}, Miles: {car.miles}, Maintenance: {car.maintenance}")

def sort_and_display_customers(rental_system):
    print("\n-- Sort and Search --")
    print("1. Customer ID")
    print("2. Name")
    print("3. Contact Info")
    print("4. Rental History")
    choice = input("Choose an option: ")

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

    sorted_customers = sorted(rental_system.customer_db.values(), key=key)
    for customer in sorted_customers:
        vip_status = "VIP" if getattr(customer, 'vip', False) else "Regular"
        print(f"{customer.name} (ID: {customer.customer_id}), Contact Information: {customer.contact_info}, Status: {vip_status}")

def add_car(rental_system):
    print("\n-- Add a New Car --\n")
    car_type = input("Enter car type (Luxury, Electric, Regular): ").capitalize()
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    rental_price = float(input("Enter rental price: "))
    miles = int(input("Enter miles driven: "))
    maintenance = int(input("Enter maintenance threshold: "))

    vip_discount = 0.0
    if car_type == 'Luxury':
        vip_discount = float(input("Enter VIP discount for Luxury car: "))

    rental_system.add_car(car_type, make, model, rental_price, miles, maintenance, vip_discount)

def remove_car(rental_system):
    print("\n-- Remove a Car --\n")
    car_id = int(input("Enter car ID to remove: "))
    if car_id in rental_system.car_db:
        confirmation = input(f"Are you sure you want to delete car with ID {car_id}? (y/n): ")
        if confirmation.lower() == 'y':
            car = rental_system.car_db.pop(car_id)
            if car in rental_system.available_cars:
                rental_system.available_cars.remove(car)
            if car in rental_system.recently_rented:
                rental_system.recently_rented.remove(car)
            print(f"Car with ID {car_id} removed successfully.")
        else:
            print("Car removal canceled.")
    else:
        print("Car not found.")

def add_customer(rental_system):
    print("\n-- Add a New Customer --\n")
    name = input("Enter customer's name: ")
    contact_info = input("Enter customer's contact info: ")
    vip_status_input = input("Is the customer a VIP? (y/n): ").strip().lower()

    vip_status = vip_status_input == 'y'

    rental_system.add_customer(name, contact_info, vip_status)

def remove_customer(rental_system):
    print("\n-- Remove a Customer --\n")
    customer_id = int(input("Enter customer ID to remove: "))
    if customer_id in rental_system.customer_db:
        confirmation = input(f"Are you sure you want to delete customer with ID {customer_id}? (y/n): ")
        if confirmation.lower() == 'y':
            rental_system.customer_db.pop(customer_id)
            print(f"Customer with ID {customer_id} removed successfully.")
        else:
            print("Customer removal canceled.")
    else:
        print("Customer not found.")

def save_car_data(rental_system):
    print("\n-- Saving Car Data --")
    rental_system.save_cars()
    print("Car data saved to 'carinfo.json'.")

def save_customer_data(rental_system):
    print("\n-- Saving Customer Data --")
    rental_system.save_customers()
    print("Customer data saved to 'customerinfo.json'.")

def report_interface(rental_system):
    print("\n-- Report --\n")
    rental_system.report()

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
