# Assignment: Miles Per Gallon
# Author: Branden Quach
# September 14, 2024
# A game where you guess the number with the fewest tries

import random

def main():
    while True:
      tries = 0
      randomNumber = random.randint(1, 1000)

      while True:
          try:
              guess = int(input(f'Guess my number between 1 and 1000 with the fewest guesses: '))
              tries += 1

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
      if tries <= 10:
          print(f'Either you know the secret or you got lucky!')
      else:
          print(f'You should be able to do better!')
      replay = input(f'Do you want to play again? (yes/no): ')
      if replay.lower() != 'yes':
          break
main()
