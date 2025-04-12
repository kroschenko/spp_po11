class DigitalClock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display_time(self):
        return f"Цифровые часы: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


class AnalogClock:
    def __init__(self, hour_angle, minute_angle, second_angle):
        self.hour_angle = hour_angle  # Поворот часовой стрелки (0-360 градусов)
        self.minute_angle = minute_angle  # Поворот минутной стрелки (0-360 градусов)
        self.second_angle = second_angle  # Поворот секундной стрелки (0-360 градусов)

    def display_time(self):
        return (
            f"Часы со стрелками: Часовая стрелка: {self.hour_angle}°, "
            f"Минутная стрелка: {self.minute_angle}°, "
            f"Секундная стрелка: {self.second_angle}°"
        )


class DigitalToAnalogAdapter(AnalogClock):
    def __init__(self, digital_clock: DigitalClock):
        hours = digital_clock.hours % 12
        minutes = digital_clock.minutes
        seconds = digital_clock.seconds

        hour_angle = (hours * 30) + (minutes * 0.5)  # 30° на час + 0.5° на минуту
        minute_angle = minutes * 6  # 6° на минуту
        second_angle = seconds * 6  # 6° на секунду

        super().__init__(hour_angle, minute_angle, second_angle)


def get_time_from_user():
    while True:
        time_input = input("Введите время в формате ЧЧ:ММ:СС или 'q', если нужно выйти: ").strip()

        if time_input.lower() == "q":
            return None

        hours, minutes, seconds = map(int, time_input.split(":"))
        if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
            return hours, minutes, seconds
        print("Ошибка.")


if __name__ == "__main__":
    while True:
        time_data = get_time_from_user()

        if time_data is None:
            print("Выход")
            break

        _hours, _minutes, _seconds = time_data
        _digital_clock = DigitalClock(_hours, _minutes, _seconds)

        analog_clock = DigitalToAnalogAdapter(_digital_clock)

        print(_digital_clock.display_time())
        print(analog_clock.display_time())
