# Lab: Software Engineering with Abstract Classes and Abstract Methods
# Author: Branden Quach
# October 16, 2024
# Creates an Abstract Base Class for Employees

from abc import ABC
from abc import abstractmethod

class Employee(ABC):
    def __init__(self, first_name: str, last_name: str, ssn: str):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @abstractmethod
    def earnings(self):
        raise NotImplementedError

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, SSN: {self.ssn}'

class SalariedEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, ssn: str, weekly_salary: float):
        super().__init__(first_name, last_name, ssn)
        self.weekly_salary = weekly_salary

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, value: float):
        if value < 0:
            raise ValueError(f'Weekly salary cannot be negative.')
        self._weekly_salary = value

    def earnings(self):
        return self.weekly_salary

    def __repr__(self):
        return f'Salaried Employee: {super().__repr__()}, Weekly Salary: ${self.weekly_salary:.2f}'

class HourlyEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, ssn: str, hours_worked: float, hourly_rate: float):
        super().__init__(first_name, last_name, ssn)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value: float):
        if not (0 <= value <= 168):
            raise ValueError("Hours worked must be between 0 and 168.")
        self._hours_worked = value
        
    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value: float):
        if value < 0:
            raise ValueError(f'Hourly rate cannot be negative.')
        self._hourly_rate = value

    def earnings(self):
        return self.hours_worked * self.hourly_rate

    def __repr__(self):
        return(f'Hourly Employee: {super().__repr__()}, Hours Worked: {self.hours_worked}, Hourly Rate: ${self.hourly_rate:.2f}')

    
