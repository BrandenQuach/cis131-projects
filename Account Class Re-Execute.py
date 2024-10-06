# Assignment: Account Class with Read-Only Properties
# Author: Branden Quach
# October 5, 2024
# Class modification to provide read-only properties for name and balance.

# Original 10.2.2 Account class
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance

    @property
    def name(self):
        return self._name
      
    @property
    def balance(self):
        return self._balance


    def deposit(self, amount):
         """Deposit money to the account."""

         # if amount is less than 0.00, raise an exception
         if amount < Decimal('0.00'):
             raise ValueError('amount must be positive.')

         self.balance += amount

account1 = Account('Branden', Decimal('100.00'))

account1.deposit(Decimal('50.00'))
print(account1.name)
print(account1.balance)

# Modified 10.2.2 Account class
