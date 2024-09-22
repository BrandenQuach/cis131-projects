# Assignment: Guess The Number
# Author: Branden Quach
# September 19, 2024
# Simulates 1 million games of craps to analyze the win and loss percentages

# Libraries
import random
# Roll two dice and return as tuple
def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)
# Game
def play_craps():
    # Sums two dice rolls together
    die_values = roll_dice()
    sum_of_dice = sum(die_values)
    # Checks for win or loss on first roll
    if sum_of_dice in (7, 11):
        return 1  # Win on the first roll
    elif sum_of_dice in (2, 3, 12):
        return -1  # Lose on the first roll
    # Continues game
    my_point = sum_of_dice
    rolls = 1
    # Loops until win or loss
    while True:
        die_values = roll_dice()
        sum_of_dice = sum(die_values)
        rolls += 1
        
        if sum_of_dice == my_point:
            return rolls  # Win as positive number
        elif sum_of_dice == 7:
            return -rolls  # Lose as negative number
# Main function
def main():
    # Dictionaries
    wins = {}
    losses = {}
    # Variables
    total_wins = 0
    total_losses = 0
    games = 1000000
    # Simulates specified games
    for _ in range(games):
        result = play_craps()
        # Checks for positive number dice rolls
        if result > 0:
            total_wins += 1
            # Adds to existing dictionary
            if result in wins:
                wins[result] += 1
            # Creates dictionary of roll number
            else:
                wins[result] = 1
        else:
            total_losses += 1
            # Converts negative rolls number to positive
            abs_result = -result
            # Adds to existing dictionary
            if abs_result in losses:
                losses[abs_result] += 1
            # Creates dictionary of roll number
            else:
                losses[abs_result] = 1
    # Displays final results when complete
    display_results(wins, losses, total_wins, total_losses, games)
# Displays results
def display_results(wins, losses, total_wins, total_losses, games):
    # Calculates win percentage
    percentage_wins = (total_wins / games) * 100
    # Calculates loss percentage
    percentage_losses = (total_losses / games) * 100
    
    print(f'Percentage of wins: {percentage_wins:.2f}%')
    print(f'Percentage of losses: {percentage_losses:.2f}%\n')
    print(f'Percentage of wins/losses based on total number of rolls')
    print(f'            % Resolved      Cumulative %')
    print(f'Rolls      on this roll     of games resolved')
    # Variables
    cumulative_wins = 0
    cumulative_losses = 0
    # Loops results
    for roll in range(1, 32):
        # Collects wins, loss, and total amount for each roll
        win_count = wins.get(roll, 0)
        loss_count = losses.get(roll, 0)
        total_count = win_count + loss_count
        # Calculates percentage of games won in that roll
        percentage_on_roll = (total_count / games) * 100
        # Collects win counts for cumulative total
        cumulative_wins += win_count
        # Collects loss counts for cumulative total
        cumulative_losses += loss_count
        # Calculates cumulative total and percentage for the roll and previous
        cumulative_total = cumulative_wins + cumulative_losses
        cumulative_percentage = (cumulative_total / games) * 100
        # Prints results
        print(f'{roll:<9} {percentage_on_roll:>11.2f}% {cumulative_percentage:>16.2f}%')

main()
