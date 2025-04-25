"""Module for adapting analog clock to digital clock using the Adapter pattern."""

from abc import ABC, abstractmethod


class DigitalClock(ABC):
    """Abstract base class for digital clocks."""

    # pylint: disable=too-few-public-methods

    @abstractmethod
    def get_time(self):
        """Return the time in digital format (hh:mm)."""


class AnalogClock:
    """Class representing an analog clock with hour and minute hand angles."""

    # pylint: disable=too-few-public-methods

    def __init__(self, hour_angle, minute_angle):
        self.hour_angle = hour_angle
        self.minute_angle = minute_angle

    def get_angles(self):
        """Return the hour and minute hand angles."""
        return self.hour_angle, self.minute_angle


class AnalogToDigitalAdapter(DigitalClock):
    """Adapter to convert analog clock to digital clock interface."""

    # pylint: disable=too-few-public-methods

    def __init__(self, analog):
        self.analog_clock = analog

    def get_time(self):
        """Convert analog angles to digital time format (hh:mm)."""
        hour_angle, minute_angle = self.analog_clock.get_angles()
        hours = int((hour_angle % 360) / 30)
        minutes = int((minute_angle % 360) / 6)
        return f"{hours:02d}:{minutes:02d}"


def create_clock():
    """Prompt user to input angles for an analog clock."""
    while True:
        try:
            hour_angle = float(input("Enter hour hand angle (0-360): "))
            if 0 <= hour_angle <= 360:
                break
            print("Angle must be between 0 and 360.")
        except ValueError:
            print("Invalid input. Enter a number.")

    while True:
        try:
            minute_angle = float(input("Enter minute hand angle (0-360): "))
            if 0 <= minute_angle <= 360:
                break
            print("Angle must be between 0 and 360.")
        except ValueError:
            print("Invalid input. Enter a number")

    return AnalogClock(hour_angle, minute_angle)


if __name__ == "__main__":
    clock = create_clock()
    adapter = AnalogToDigitalAdapter(clock)
    print(f"Time: {adapter.get_time()}")
