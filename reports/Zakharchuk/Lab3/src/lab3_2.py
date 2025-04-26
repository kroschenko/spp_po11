from abc import ABC, abstractmethod

# Интерфейс для часов
class Clock(ABC):
    @abstractmethod
    def get_time(self):
        pass


# Класс цифровых часов
class DigitalClock(Clock):
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}"


# Класс аналоговых часов (хранит углы стрелок)
class AnalogClock:
    def __init__(self, hour_angle, minute_angle):
        self.hour_angle = hour_angle  # угол часовой стрелки (градусы)
        self.minute_angle = minute_angle  # угол минутной стрелки (градусы)

    def get_angles(self):
        return self.hour_angle, self.minute_angle


# Адаптер для аналоговых часов
class AnalogToDigitalAdapter(Clock):
    def __init__(self, analog_clock):
        self.analog_clock = analog_clock

    def get_time(self):
        # Преобразуем углы в часы и минуты
        hour_angle, minute_angle = self.analog_clock.get_angles()
        # 360 градусов = 12 часов, 1 час = 30 градусов
        hours = int(hour_angle // 30) % 12
        # 360 градусов = 60 минут, 1 минута = 6 градусов
        minutes = int(minute_angle // 6)
        return f"{hours:02d}:{minutes:02d}"


# Демонстрация работы
def main():
    while True:
        print("\nВведите время для часов (или 'q' для выхода)")
        time_input = input("Формат ЧЧ:ММ (например, 14:45): ").strip()

        if time_input.lower() == 'q':
            print("Выход из программы.")
            break

        try:
            # Проверяем формат времени
            hours, minutes = map(int, time_input.split(':'))
            if not (0 <= hours <= 23 and 0 <= minutes <= 59):
                print("Ошибка: Часы должны быть от 0 до 23, минуты от 0 до 59.")
                continue

            # Создаем цифровые часы
            digital_clock = DigitalClock(hours, minutes)
            print("Цифровые часы:", digital_clock.get_time())

            # Преобразуем время в углы для аналоговых часов
            # Часовая стрелка: 30 градусов за час + 0.5 градуса за минуту
            hour_angle = (hours % 12) * 30 + minutes * 0.5
            # Минутная стрелка: 6 градусов за минуту
            minute_angle = minutes * 6
            analog_clock = AnalogClock(hour_angle, minute_angle)
            # Используем адаптер
            adapted_clock = AnalogToDigitalAdapter(analog_clock)
            print("Аналоговые часы (через адаптер):", adapted_clock.get_time())

        except ValueError:
            print("Ошибка: Неверный формат времени. Используйте ЧЧ:ММ (например, 14:45).")
            continue


if __name__ == "__main__":
    main()
