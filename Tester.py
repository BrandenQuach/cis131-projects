# Lab: Software Engineering with Abstract Classes and Abstract Methods
# Author: Branden Quach
# October 17, 2024
# Tests an Abstract Base Class for Employees

from Abstract import Employee, SalariedEmployee, HourlyEmployee

try:
    employee = Employee('Jeff', 'Jefferson', '987-65-4321')
except TypeError as e:
    print(f'{e}')

salaried_employee = SalariedEmployee('Joe', 'Smith', '123-45-6789', 2000)
hourly_employee = HourlyEmployee('Sarah', 'Johnson', '135-79-2468', 40, 30)

print(salaried_employee)
print(f'Salaried Employee Earnings: ${salaried_employee.earnings():.2f}')

print(hourly_employee)
print(f'Hourly Employee Earnings: ${hourly_employee.earnings():.2f}')

employees = [salaried_employees, hourly_employees]
for employee in employees:
    print()
    print(employee)
    print(f'Earnings: ${employee.earnings():.2f}')
