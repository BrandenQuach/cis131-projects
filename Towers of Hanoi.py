# Lab: Towers of Hanoi
# Author: Branden Quach
# October 31, 2024
# Solves the Tower of Hanoi problem by moving 3 disks from peg 1 to peg 3.

# Towers of Hanoi function
def towers_of_hanoi(n, starting_peg, destination_peg, temporary_peg):
    # Checks if only one disk is left
    if n == 1:
        # Moves final disk to destination peg
        print(f'{starting_peg} to {destination_peg}')
        return
    # Moves disk from starting peg to temporary peg
    towers_of_hanoi(n - 1, starting_peg, temporary_peg, destination_peg)
    # Moves disk from starting peg to destination peg
    print(f'{starting_peg} to {destination_peg}')
    # Moves disk from temporary peg to destination peg
    towers_of_hanoi(n - 1, temporary_peg, destination_peg, starting_peg)

# Sets amount of disk for the problem
disks = 3
# Calls function using amount of disks, starting peg as position 1, destination peg as position 3, and temporary peg as position 2
towers_of_hanoi(disks, 1, 3, 2)
