# Assignment: Miles Per Gallon
# Author: Branden Quach
# September 14, 2024
# Calculates the miles per gallon with user input

def main():
    # Variables
    totalGallons = 0
    totalMiles = 0
    # Calls prompt for gallons
    getGallons = getValidGallons()
    # While function for sentinel
    while getGallons != -1:
        # Calls prompt for miles
        getMiles = getValidMiles()
        # Calculates MPG
        total = getMiles / getGallons
        # Gathers total gallons
        totalGallons += getGallons
        # Gathers total miles
        totalMiles += getMiles
        # Prints MPG results
        print(f'The miles/gallon for this tank was {total:.6f}')
        # Calls prompt for gallons or sentinel
        getGallons = getValidGallons()
    # Else for sentinel value entry
    else:
        # Calculates total average of miles and gallons
        average = totalMiles / totalGallons
        print(f'The overall average miles/gallon was {average:.6f}')
def getValidGallons():
    try:
        getGallons = (float(input(f'Enter the gallons used (-1 to end): ')))
        if getGallons != -1 and getGallons < 0:
            print(f'Please enter a valid number.')
            return getValidGallons()
        else:
            return getGallons
    except:
        print(f'Invalid entry. Please try again.')
        return getValidGallons()
def getValidMiles():
    try:
        getMiles = (float(input(f'Enter the miles driven: ')))
        if getMiles < 0:
            print(f'Please enter a valid number.')
            return getValidMiles()
        else:
            return getMiles
    except:
        print(f'Invalid entry. Please try again.')
        return getValidMiles()
main()
