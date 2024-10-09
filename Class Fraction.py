# Assignment: Lab: Class Fraction
# Author: Branden Quach
# October 8, 2024
# Demonstrate how to use the class Fractions

# Library
from fractions import Fraction

# Fractions class demonstration
print(f'Fraction class demonstration:')

# Fractions assigned to variables
fraction1 = Fraction(2, 5)
fraction2 = Fraction(1, 8)

# Addition of fractions
add_fractions = fraction1 + fraction2
print(f'\n{fraction1} + {fraction2} = {add_fractions}.')

# Subraction of fractions
subtract_fractions = fraction1 - fraction2
print(f'{fraction1} - {fraction2} = {subtract_fractions}.')

# Multiplying of fractions
multiply_fractions = fraction1 * fraction2
print(f'{fraction1} times {fraction2} = {multiply_fractions}.')

# Dividing of fractions
divide_fractions = fraction1 / fraction2
print(f'{fraction1} divided by {fraction2} = {divide_fractions}.')

# Fractions printed in a/b format
print(f'Fraction 1 is {fraction1.numerator}/{fraction1.denominator}.')
print(f'Fraction 2 is {fraction2.numerator}/{fraction2.denominator}.')

# Fractions converted to float numbers
fraction1_float = float(fraction1)
fraction2_float = float(fraction2)
print(f'{fraction1} as a floating point number is {fraction1_float}.')
print(f'{fraction2} as a floating point number is {fraction2_float}.')

# Complex numbers demonstration
print(f'\nComplex numbers built-in type demonstration:')

# Complex numbers assigned to variables
complex1 = complex(5, 3)
complex2 = complex(3, 2)

# Addition of complex numbers
add_complex = complex1 + complex2
print(f'\n{complex1} + {complex2} = {add_complex}.')

# Subtraction of complex numbers
subtract_complex = complex1 + complex2
print(f'{complex1} - {complex2} = {subtract_complex}.')

# Printing complex numbers
print(f'Complex number 1 is {complex1}.')
print(f'Complex number 2 is {complex2}.')

# Seperating complex numbers into real and imaginary numbers
real_complex1 = complex1.real
imaginary_complex1 = complex1.imag
real_complex2 = complex2.real
imaginary_complex2 = complex2.imag

# Prints real and imaginary numbers of given complex numbers
print(f'The real part of {complex1} is {real_complex1} and the imaginary part is {imaginary_complex1}.')
print(f'The real part of {complex2} is {real_complex2} and the imaginary part is {imaginary_complex2}.')
