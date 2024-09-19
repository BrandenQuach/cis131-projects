# Assignment: Telephone Number Word Generator
# Author: Branden Quach
# September 18, 2024
# Converts a telephone number into a word for easy memorization

# Library
import itertools

# Main function
def main():
    # Check for errors
    try:
        # Prompt for telephone number
        number = (str(input(f'Enter a 7 digit telephone number without 0, 1, and - : ')))
        # Input validation
        if len(number) != 7 or any(digit in number for digit in '01'):
            print(f'Input has to be 7 digits and not contain 0 or 1. Please try again.')
            return main()
        # Calls word converter function
        words = wordConverter(number)
        # Prints all combinations
        for word in words:
          print(word)
          
    except:
        print(f'Invalid entry. Please try again.')
        return main()
# Number to word converter
def wordConverter(number):
    # Dictionary of numbers to words
    digitToLetters = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
    }
    # Converts number to letter
    letters = [digitToLetters[digit] for digit in number]
    # Combines all combinations of numbers to letters
    combos = [''.join(word) for word in itertools.product(*letters)]
    return combos
  
main()
