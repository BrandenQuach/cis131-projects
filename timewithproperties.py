# Assignment: Modifying The Internal Data Representation of a Class
# Author: Branden Quach
# October 6, 2024
# Class modification to store time as total seconds since midnight.

# Original 10.4.2 Time class
class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.second = second # 0-59
        
    @property
    def minute(self):
        """Return the minute."""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._minute = minute

    @property
    def second(self):
        """Return the second."""
        return self._second

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __repr__(self):
        """Return Time string for repr()."""
        return f'Time(hour={self.hour}, minute={self.minute}, second={self.second})'
