# Assignment: Final
# Author: Branden Quach
# December 7, 2024
# Tester

runfile('Final.py')

if __name__ == "__main__":
    program = RentalSystem() # Assign function to variable program

    program.load_data() # Initializes all files

    program.rent_car(customer_id=1, car_id=2) # Rents car ID 2 for customer ID 1
    
    program.report() # Prints report to show car has been rented properly
