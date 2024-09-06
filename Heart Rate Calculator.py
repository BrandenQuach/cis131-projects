# Assignment: Target Heart-Rate Calculator
# Author: Branden Quach
# September 6, 2024
# Calculates range and maximum heart rate from user's given age

def main():
    # Calls to prompt user for age
    age = getValidAge()
    # Calculates the maximum bpm
    maximum = 220 - age
    # Calculates the minimum bpm range
    target_low = maximum * 0.50
    # Calculates the maximum bpm range
    target_high = maximum * 0.85
    # Prints results
    print(f'Your maximum heart rate is {maximum} beats per minute.')
    print(f'Your target heart rate range is {target_low} to {target_high} beats per minute.')
# Checks for valid inputs
def getValidAge():
    try:
        # Prompt
        age = (float(input(f'Enter your age: ')))
        # Checks if age is greater than 0
        if age <= 0:
            print(f'{getAge} is not a valid age. Please try again.')
            return getValidAge()
        else:
            return age
    except:
        print(f'Invalid age. Please try again.')
        return getValidAge()

main()
