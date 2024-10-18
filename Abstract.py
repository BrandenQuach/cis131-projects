# Lab: Software Engineering with Abstract Classes and Abstract Methods
# Author: Branden Quach
# October 17, 2024
# Creates an Abstract Base Class for Employees

# Imports Abstract Base Class and abstract method
from abc import ABC, abstractmethod

# Main Employee class
class Employee(ABC):
    # Initializes all data attributes for employee in read only mode
    def __init__(self, first_name: str, last_name: str, ssn: str):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
    # Property decorator for first name
    @property
    def first_name(self):
        return self._first_name
    # Property decorator for last name
    @property
    def last_name(self):
        return self._last_name
    # Property decorator for ssn
    @property
    def ssn(self):
        return self._ssn
    # Abstractmethod decorator that raises NotImplementedError
    @abstractmethod
    def earnings(self):
        raise NotImplementedError
    # Returns printable data of employee
    def __repr__(self):
        return f'{self.first_name} {self.last_name}, SSN: {self.ssn}'

# Salaried Employee class
class SalariedEmployee(Employee):
    # Initializes all data attributes for salaried employee
    def __init__(self, first_name: str, last_name: str, ssn: str, weekly_salary: float):
        # Calls temporary base class Employee
        super().__init__(first_name, last_name, ssn)
        # Sets weekly salary in read-write mode
        self.weekly_salary = weekly_salary
    # Property decorator for weekly salary
    @property
    def weekly_salary(self):
        return self._weekly_salary
    # Setter for weekly salary
    @weekly_salary.setter
    def weekly_salary(self, value: float):
        # Checks for negative numbers
        if value < 0:
            raise ValueError(f'Weekly salary cannot be negative.')
        self._weekly_salary = value
    # Earnings abstract method
    def earnings(self):
        return self.weekly_salary
    # Returns a string of all salaried employee information
    def __repr__(self):
        return f'Salaried Employee: {super().__repr__()}, Weekly Salary: ${self.weekly_salary:.2f}'

# Hourly Employee class
class HourlyEmployee(Employee):
    # Initializes all data attributes for hourly employee
    def __init__(self, first_name: str, last_name: str, ssn: str, hours_worked: float, hourly_rate: float):
        # Calls temporary base class Employee
        super().__init__(first_name, last_name, ssn)
        # Sets hours worked and hourly rate in read-write mode
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    # Property decorator for hours worked
    @property
    def hours_worked(self):
        return self._hours_worked
    # Setter for hours worked
    @hours_worked.setter
    def hours_worked(self, value: float):
        # Checks for values 0 to 168
        if not (0 <= value <= 168):
            raise ValueError(f'Hours worked must be between 0 and 168.')
        self._hours_worked = value
    # Property decorator for hours worked
    @property
    def hourly_rate(self):
        return self._hourly_rate
    # Setter for hourly rate
    @hourly_rate.setter
    def hourly_rate(self, value: float):
        # Checks for negative numbers
        if value < 0:
            raise ValueError(f'Hourly rate cannot be negative.')
        self._hourly_rate = value
    # Earnings abstract method
    def earnings(self):
        return self.hours_worked * self.hourly_rate
    # Returns a string of all hourly employee information
    def __repr__(self):
        return(f'Hourly Employee: {super().__repr__()}, Hours Worked: {self.hours_worked}, Hourly Rate: ${self.hourly_rate:.2f}')
