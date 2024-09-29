# Assignment: Telephone Number Word Generator
# Author: Branden Quach
# September 28, 2024
# Converts a telephone number into a word and inputs into a .txt file.

# Library
import itertools

# Main function
def main():
    # Error validation
    try:
        # Prompt for telephone number
        number = (str(input(f'Enter a 7 digit telephone number without 0, 1, and - : ')))
        # Input validation if number is longer than 7 digits or contains 0 or 1
        if len(number) != 7 or any(digit in number for digit in '01'):
            print(f'Input has to be 7 digits and not contain 0 or 1. Please try again.')
            return main()
        # Calls word converter function
        words = wordConverter(number)
        # Prints all word combinations into a .txt file
        with open('telephone_words.txt', mode='w') as telephone_words:
            for word in words:
                print(word, file=telephone_words)
          
    except:
        print(f'Invalid entry. Please try again.')
        return main()
# Number to word converter
def wordConverter(number):
    # Dictionary of numbers that correspond to words
    digitToLetters = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
    }
    # Converts number to letter
    letters = [digitToLetters[digit] for digit in number]
    # Combines all combinations of numbers to letters
    combos = [''.join(word) for word in itertools.product(*letters)]
    return combos
# Calls main function
main()
