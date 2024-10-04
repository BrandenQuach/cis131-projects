# Assignment: Modifying The Internal Data Representation of a Class
# Author: Branden Quach
# October 3, 2024
# Class modification to store time as total seconds since midnight.

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.second = second # 0-59
