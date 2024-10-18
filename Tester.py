# Lab: Software Engineering with Abstract Classes and Abstract Methods
# Author: Branden Quach
# October 17, 2024
# Tests an Abstract Base Class for Employees

# Imports Employee, SalariedEmployee, and HourlyEmployee classes from Abstract.py
from Abstract import Employee, SalariedEmployee, HourlyEmployee

# Try except to test for employee object creation
try:
    employee = Employee('Jeff', 'Jefferson', '987-65-4321')
# Prints TypeError if employee creation isn't allowed
except TypeError as e:
    print(f'{e}\n')

# Assigns employee objects to variables
salaried_employee = SalariedEmployee('Joe', 'Smith', '123-45-6789', 2000)
hourly_employee = HourlyEmployee('Sarah', 'Johnson', '135-79-2468', 40, 30)

# Prints objects of salaried employee
print(salaried_employee)
print(f'Salaried Employee Earnings: ${salaried_employee.earnings():.2f}\n')

# Prints objects of hourly employee
print(hourly_employee)
print(f'Hourly Employee Earnings: ${hourly_employee.earnings():.2f}')


# Creates list and prints all employee's objects
employees = [salaried_employee, hourly_employee]
for employee in employees:
    print()
    print(employee)
    print(f'Earnings: ${employee.earnings():.2f}')
