# Assignment: Account Class with Read-Only Properties
# Author: Branden Quach
# October 5, 2024
# Tests account program and modified read-only account program

# Import libraries and original account.py
from decimal import Decimal
from account import Account

# Sets values for account
account1 = Account('Branden', Decimal('100.00'))

# Tests for name changing
try:
    account1.name = 'Jeff'
    print(account1.name) # Prints name if no error occurs
except:
    print(f'Name could not be edited') # Prints if error occurs
  
# Tests for balance changing
try:
    account1.balance = '50.00'
    print(account1.balance) # Prints balance if no error occurs
except:
    print(f'Balance could not be edited') # Prints if error occurs

# Imports modified account in read only
from Account_Read_Only import Account

# Sets values for account
account1 = Account('Branden', Decimal('100.00'))

# Tests for name changing
try:
    account1.name = 'Jeff'
    print(account1.name) # Prints name if no error occurs
except:
    print(f'Name could not be edited') # Prints if error occurs

# Tests for balance changing
try:
    account1.balance = '50.00'
    print(account1.balance) # Prints balance if no error occurs
except:
    print(f'Balance could not be edited') # Prints if error occurs
