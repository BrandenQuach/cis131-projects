# Assignment: Guess The Number
# Author: Branden Quach
# September 19, 2024
# Simulates 1 million games of craps to analyze the win and loss percentages

import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)

def play_craps():
    """Simulate a game of craps and return the number of rolls taken."""
    die_values = roll_dice()
    sum_of_dice = sum(die_values)
    
    if sum_of_dice in (7, 11):
        return 1  # Win on the first roll
    elif sum_of_dice in (2, 3, 12):
        return 1  # Lose on the first roll

    my_point = sum_of_dice
    rolls = 1
    
    while True:
        die_values = roll_dice()
        sum_of_dice = sum(die_values)
        rolls += 1
        
        if sum_of_dice == my_point:
            return rolls  # Win by making point
        elif sum_of_dice == 7:
            return -rolls  # Lose by rolling 7

def simulate_games(num_games):
    wins = {}
    losses = {}
    total_wins = 0
    total_losses = 0

    for _ in range(num_games):
        result = play_craps()
        
        if result > 0:
            total_wins += 1
            if result in wins:
                wins[result] += 1
            else:
                wins[result] = 1
        else:
            total_losses += 1
            abs_result = -result
            if abs_result in losses:
                losses[abs_result] += 1
            else:
                losses[abs_result] = 1

    return wins, losses, total_wins, total_losses

def display_results(wins, losses, total_wins, total_losses):
    total_games = total_wins + total_losses
    percentage_wins = (total_wins / total_games) * 100
    percentage_losses = (total_losses / total_games) * 100

    print(f'Percentage of wins: {percentage_wins:.2f}%')
    print(f'Percentage of losses: {percentage_losses:.2f}%')
    print()
    print(f'Percentage of wins/losses based on total number of rolls')
    print(f'% Resolved        Cumulative %')
    
    cumulative_wins = 0
    cumulative_losses = 0
    max_rolls = max(len(wins), len(losses))

    for roll in range(1, max_rolls + 1):
        win_count = wins.get(roll, 0)
        loss_count = losses.get(roll, 0)
        total_count = win_count + loss_count
        
        if total_count > 0:
            percentage_on_roll = (total_count / total_games) * 100
            cumulative_wins += win_count
            cumulative_losses += loss_count
            
            cumulative_total = cumulative_wins + cumulative_losses
            cumulative_percentage = (cumulative_total / total_games) * 100
            
            print(f'{roll:<9} {percentage_on_roll:>11.2f}% {cumulative_percentage:>16.2f}%')

# Simulate 1,000,000 games
num_games = 1_000_000
wins, losses, total_wins, total_losses = simulate_games(num_games)

# Display the results
display_results(wins, losses, total_wins, total_losses)
