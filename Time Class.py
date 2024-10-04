# Assignment: Modifying The Internal Data Representation of a Class
# Author: Branden Quach
# October 3, 2024
# Class modification to store time as total seconds since midnight.

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.total_seconds =self.to_total_seconds(hour, minute, second)

    def _to_total_seconds(self, hour, minute, second):
        return hour * 3600 + minute * 60 + second

    @property
    def hour(self):
        return self._total_seconds // 3600

    @hour.setter
    def hour(self, value):
        if not (0 <= value < 24):
            raise ValueError(f'Hour must be between 0 and 23.')
        self._total_seconds = (value * 3600) + (self.minute * 60) + self.second

    @property
    def minute(self):
        return (self._total_seconds % 3600) // 60

    @minute.setter
    def minute(self, value):
        if not (0 <= value < 60):
            raise ValueError(f'Minute must be between 0 and 59.')
        self._total_seconds = (self.hour * 3600) + (value * 60) + self.second

    @property
    def second(self):
        return self._total_seconds % 60

    @second.setter
    def second(self, value):
        if not (0 <= value < 60):
            raise ValueError(f'Second must be between 0 and 59.')
        self._total_seconds = (self.hour * 3600) + (self.minute * 60) + value

    def __repr__(self):
        return f'Time(hour={self.hour}, minute={Self.minute}, second={self.second})'
