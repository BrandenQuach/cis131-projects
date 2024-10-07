# Assignment: Modifying The Internal Data Representation of a Class
# Author: Branden Quach
# October 6, 2024
# Class modification to store time as total seconds since midnight.

# Imports original 10.4.2 timewithproperties file
from timewithproperties import Time
# Sets time
wake_up = Time(8, 45, 50)
print(wake_up)
# Changes hour to 10
wake_up.hour = 10
print(wake_up)
# Changes minute to 30
wake_up.minute = 30
print(wake_up)
# Changes seconds to 30
wake_up.second = 30
print(wake_up, '\n')

# Imports modified 10.4.2 to include total seconds
from timewithtotalseconds import Time
# Sets time
wake_up = Time(8, 45, 50)
print(wake_up)
# Changes hour to 10
wake_up.hour = 10
print(wake_up)
# Changes minute to 30
wake_up.minute = 30
print(wake_up)
# Changes seconds to 30
wake_up.second = 30
print(wake_up)
