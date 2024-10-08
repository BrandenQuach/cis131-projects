# Assignment: Manipulating Dates and Times With Module: DATETIME
# Author: Branden Quach
# October 8, 2024
# Researching and performing tasks related to datetime's capabilities.

from datetime import datetime

x = datetime.now()
y = datetime.now()

print(f'Datetime object x is:', x)
print(f'Datetime object y is:', y)

print(f'\nDatetime object x attributes:')
print(f'Year:', x.year)
print(f'Month:', x.month)
print(f'Day:', x.day)
print(f'Hour:', x.hour)
print(f'Second:', x.second)
print(f'Microsecond:', x.microsecond)

print(f'\nDatetime object y attributes:')
print(f'Year:', y.year)
print(f'Month:', y.month)
print(f'Day:', y.day)
print(f'Hour:', y.hour)
print(f'Second:', y.second)
print(f'Microsecond:', y.microsecond)

print(f'\nComparisons between x and y:')
print(f'Is x equal to y:', x == y)
print(f'Is x less than y:', x < y)
print(f'Is x greater than y:', x > y)

difference = y - x
print(f'\nDifference between y and x:')
print(difference)
