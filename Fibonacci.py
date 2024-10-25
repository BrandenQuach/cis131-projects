# Lab: Recursive Fibonacci Modification
# Author: Branden Quach
# October 24, 2024
# Modification of Section 11.4 recursive fibonacci function to keep track of total number of function calls.

# Global variable
call_amount = 0

# Fibonacci function
def fibonacci(n):
    # Calls global variable
    global call_amount
    # Increments calls
    call_amount += 1
    # Fibonacci sequence
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Fibonacci calculator function
def fibonacci_calculator(n):
    # Calls global variable
    global call_amount
    # Sets call amount equal to zero
    call_amount = 0
    # Calls fibonacci function
    result = fibonacci(n)
    return result, call_amount

# Prompts for fibonacci calls of 10, 20, and 30
for num in [10, 20, 30]:
    # Calls fibonacci calculator function
    result, calls = fibonacci_calculator(num)
    # Prints results
    print(f'Fibonacci({num}) = {result}, Number of calls = {calls}')
