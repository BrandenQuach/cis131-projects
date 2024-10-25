# Lab: Recursive Power Function
# Author: Branden Quach
# October 24, 2024
# A recursive power function from user inputted base and exponent.

# Power function
def power(base, exponent):
    # Checks for terminating condition
    if exponent == 1:
        return base
    # Returns base times power through recursive function
    else:
        return base * power(base, exponent - 1)

# Prompts base and exponent from user
base = float(input(f'Enter the base: '))
exponent = int(input(f'Enter an exponent equal or greater than 1: '))

# Validation for exponent less than 1
if exponent < 1:
    print(f'Exponent must be equal or greater than 1: ')
  
else:
    # Gathers result by calling power function
    result = power(base, exponent)
    # Prints results
    print(f'{base}^{exponent} = {result}')
