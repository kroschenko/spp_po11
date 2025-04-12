from typing import Protocol

class DigitalThermometer(Protocol):
    def get_temperature(self) -> float: ...

class AnalogThermometer:
    def __init__(self, min_temp: float, max_temp: float):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.mercury_height: float = 0.0

    def set_mercury_height(self, height: float) -> None:
        if height < 0 or height > 100:
            raise ValueError("Height must be between 0% and 100%")
        self.mercury_height = height

    def get_analog_temp(self) -> float:
        return self.min_temp + (self.max_temp - self.min_temp) * (self.mercury_height / 100)

class ThermometerAdapter:
    def __init__(self, analog_therm: AnalogThermometer):
        self.thermometer = analog_therm

    def get_temperature(self) -> float:
        return self.thermometer.get_analog_temp()

if __name__ == "__main__":
    analog_therm = AnalogThermometer(min_temp=35.0, max_temp=42.0)

    try:
        height = float(input("Введите высоту ртутного столба (0-100%): "))
        analog_therm.set_mercury_height(height)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit()

    digital_therm = ThermometerAdapter(analog_therm)
    print(f"Текущая температура: {digital_therm.get_temperature():.1f}°C")
