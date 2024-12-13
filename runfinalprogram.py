# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Runs Rental Car Program

from Final import RentalSystem

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

    # Sort the cars based on the choice
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

    # Sort the customers based on the choice
    if choice == '1':
        key = lambda customer: customer.customer_id
    elif choice == '2':
        key = lambda customer: customer.name
    elif choice == '3':
        key = lambda customer: customer.contact_info
    elif choice == '4':
        customer_id = int(input("Enter customer ID to view rental history: "))
        rental_system.view_customer_rental_history(customer_id)
        return  # Return early after showing rental history
    else:
        print("Invalid option!")
        return

    sorted_customers = sorted(rental_system.customer_db.values(), key=key)
    for customer in sorted_customers:
        vip_status = "VIP" if getattr(customer, 'vip', False) else "Regular"
        print(f"{customer.name} (ID: {customer.customer_id}), Contact Information: {customer.contact_info}, Status: {vip_status}")
from Final import RentalSystem

