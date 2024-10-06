# Assignment: Account Class with Read-Only Properties
# Author: Branden Quach
# October 5, 2024
# Class modification to provide read-only properties for name and balance.

# Modified 10.2.2 Account Class
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self._name = name
        self._balance = balance
    # Sets name to read-only
    @property
    def name(self):
        return self._name
    # Sets balance to read-only  
    @property
    def balance(self):
        return self._balance

    
    def deposit(self, amount):
         """Deposit money to the account."""

         # if amount is less than 0.00, raise an exception
         if amount < Decimal('0.00'):
             raise ValueError('amount must be positive.')

         self._balance += amount
