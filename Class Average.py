# Assignment: Class Average
# Author: Branden Quach
# September 26, 2024
# Stores grades in a .txt file

with open('grades.txt', mode='w') as grades:

    total = 0
    grade_counter = 0

    grade = int(input('Enter grade, -1 to end: '))

    while grade != -1:
        total += grade
        grade_counter += 1
        grade = int(input('Enter grade, -1 to end: '))
        print(f'{grade} {total} {grade_counter}', file=grades)

    if grade_counter != 0:
        average = total / grade_counter
        print(f'Class average is {average:.2f}', file=grades)
    else:
        print('No grades were entered')
