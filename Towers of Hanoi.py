# Lab: Towers of Hanoi
# Author: Branden Quach
# October 31, 2024
# Solves the Tower of Hanoi problem by moving 3 disks from peg 1 to peg 3.

def towers_of_hanoi(n, starting_peg, destination_peg, temporary_peg):
    if n == 1:
        print(f'{starting_peg} to {destination_peg}')
        return
    towers_of_hanoi(n - 1, starting_peg, temporary_peg, destination_peg)
    print(f'{starting_peg} to {destination_peg}')
    towers_of_hanoi(n - 1, temporary_peg, target_peg, source_peg)

disks = 3
towers_of_hanoi(disks, 1, 3, 2)
