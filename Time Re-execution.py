# Assignment: Modifying The Internal Data Representation of a Class
# Author: Branden Quach
# October 6, 2024
# Class modification to store time as total seconds since midnight.

from timewithproperties import Time

wake_up = Time(8, 45, 50)
print(wake_up)

wake_up.hour = 10
print(wake_up)

wake_up.minute = 30
print(wake_up)

wake_up.second = 30
print(wake_up)

from timewithtotalseconds import Time

wake_up = Time(8, 45, 50)
print(wake_up)
print(wake_up.total_seconds)

wake_up.hour = 10
print(wake_up)
print(wake_up.total_seconds)

wake_up.minute = 30
print(wake_up)
print(wake_up.total_seconds)

wake_up.second = 30
print(wake_up)
print(wake_up.total_seconds)
