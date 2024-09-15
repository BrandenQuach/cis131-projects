# Assignment: Guess The Number
# Author: Branden Quach
# September 14, 2024
# A game where you guess the number with the fewest tries

# Libraries
import random
# Main function
def main():
    # While loop for game replay
    while True:
        # Variable
        tries = 0
        # Creates random number
        randomNumber = random.randint(1, 1000)
        # While loop for replay until win
        while True:
            # Try except to check for invalid input
            try:
                # Prompt
                guess = int(input(f'Guess my number between 1 and 1000 with the fewest guesses: '))
                tries += 1
                # Message based off input
                if guess > randomNumber:
                    print(f'Too high. Try again.')
                elif guess < randomNumber:
                    print(f'Too low. Try again.')
                else:
                    print(f'Congratulations. You guessed the number!')
                    break
            except:
                print(f'Invalid entry. Please try again.')
                return main()
        # Checks for amount of attempts
        if tries <= 10:
            print(f'Either you know the secret or you got lucky!')
        else:
            print(f'You should be able to do better!')
        # Prompt for replay
        replay = input(f'Do you want to play again? (yes/no): ')
        if replay.lower() != 'yes':
            break
main()
