# Assignment: Modifying The Internal Data Representation of a Class
# Author: Branden Quach
# October 6, 2024
# Class modification to store time as total seconds since midnight.

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.total_seconds = self.to_total_seconds(hour, minute, second)

    def to_total_seconds(self, hour, minute, second):
        return hour * 3600 + minute * 60 + second
        
    # Returns hours
    @property
    def hour(self):
        return self._total_seconds // 3600
        
    # Sets hours
    @hour.setter
    def hour(self, value):
        if not (0 <= value < 24):
            raise ValueError(f'Hour must be between 0 and 23.')
        self._total_seconds = (value * 3600) + (self.minute * 60) + self.second
        
    # Returns minutes
    @property
    def minute(self):
        return (self._total_seconds % 3600) // 60
        
    # Sets minutes
    @minute.setter
    def minute(self, value):
        if not (0 <= value < 60):
            raise ValueError(f'Minute must be between 0 and 59.')
        self._total_seconds = (self.hour * 3600) + (value * 60) + self.second
        
    # Returns seconds
    @property
    def second(self):
        return self._total_seconds % 60
        
    # Sets seconds
    @second.setter
    def second(self, value):
        if not (0 <= value < 60):
            raise ValueError(f'Second must be between 0 and 59.')
        self._total_seconds = (self.hour * 3600) + (self.minute * 60) + value
        
    # Returns total seconds
    @property
    def total_seconds(self):
        return self._total_seconds
        
    # Sets total seconds
    @total_seconds.setter
    def total_seconds(self, value):
        if not (0 <= value < 86400):
            raise ValueError(f'Total seconds must be between 0 and 86399.')
        self._total_seconds = value

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second
        
    # Returns time string for repr()
    def __repr__(self):
        return (f'Time(hour={self.hour}, minute={self.minute}, second={self.second}, total_seconds={self.total_seconds})')
