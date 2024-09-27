# Assignment: Class Average
# Author: Branden Quach
# September 26, 2024
# Stores grades in a .txt file

# Opens grade file in write mode
with open('grades.txt', mode='w') as grades:
    # Variables
    total = 0
    grade_counter = 0
    # Prints header of table
    print(f'Grade Total Counter', file=grades)
    # While loop until sentinel value is entered
    while True:
        # Prompts for grade input
        grade = int(input('Enter grade, -1 to end: '))
        # Checks for sentinel value input
        if grade == -1:
            # Calculates average
            average = total / grade_counter
            # Prints results to user and into file
            print(f'Class average is {average:.2f}', file=grades)
            print(f'Class average is {average:.2f}')
            break
        # Adds grade to total if sentinel not detected
        total += grade
        # Adds one to grade counter
        grade_counter += 1
        # Prints results in file
        print(f'{grade}     {total}     {grade_counter}', file=grades)
