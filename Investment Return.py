# Assignment: Investment Return
# Author: Branden Quach
# September 5, 2024
# Calculates 7% return of $1000 after certain years

def main():
    # Variables
    p = 1000 # Principle Balance
    r = 0.07 # Annual rate of return
    y = [10, 20, 30] # Years to calculate

    a = {n: p * (1 + r) ** n for n in y} # Deposit amount equation

    print(f'7% Investment Return')
    # Repeats for all years listed
    for n, a in a.items():
        print(f"Amount after {n} years: ${a:.2f}")

main()
