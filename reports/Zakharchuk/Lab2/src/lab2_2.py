from abc import ABC, abstractmethod
from dataclasses import dataclass

# Структура для группировки деталей рейса
@dataclass
class FlightDetails:
    flight_number: str
    departure_airport: "Airport"
    destination_airport: "Airport"

# Абстрактный класс для людей
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, возраст: {self.age}"


# Абстрактный класс для членов экипажа
class CrewMember(Person):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    @abstractmethod
    def do_job(self):
        pass


# Конкретные роли членов экипажа
class Pilot(CrewMember):
    def do_job(self):
        return f"{self.name} управляет самолетом"

    def __str__(self):
        return f"Пилот {self.name}, опыт: {self.experience} лет"


class Navigator(CrewMember):
    def do_job(self):
        return f"{self.name} прокладывает маршрут"

    def __str__(self):
        return f"Штурман {self.name}, опыт: {self.experience} лет"


class RadioOperator(CrewMember):
    def do_job(self):
        return f"{self.name} поддерживает связь"

    def __str__(self):
        return f"Радист {self.name}, опыт: {self.experience} лет"


class FlightAttendant(CrewMember):
    def do_job(self):
        return f"{self.name} обслуживает пассажиров"

    def __str__(self):
        return f"Стюардесса {self.name}, опыт: {self.experience} лет"


# Класс самолета
class Airplane:
    def __init__(self, model, capacity, max_range):
        self.model = model
        self.capacity = capacity
        self.max_range = max_range
        self.has_technical_issue = False

    def report_issue(self):
        self.has_technical_issue = True
        print(f"Самолет {self.model} сообщил о технической неисправности")

    def __str__(self):
        return f"Самолет {self.model}, вместимость: {self.capacity}, дальность: {self.max_range} км"


# Класс аэропорта
class Airport:
    def __init__(self, name, is_good_weather=True):
        self.name = name
        self.is_good_weather = is_good_weather

    def set_weather(self, is_good):
        self.is_good_weather = is_good
        print(f"Погода в аэропорту {self.name}: {'хорошая' if is_good else 'плохая'}")

    def __str__(self):
        return f"Аэропорт {self.name}"


# Класс летной бригады
class FlightCrew:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Добавлен в бригаду: {member}")

    def show_crew(self):
        print("Состав бригады:")
        for member in self.members:
            print(f"- {member}")

    def do_jobs(self):
        print("Бригада выполняет свои обязанности:")
        for member in self.members:
            print(f"- {member.do_job()}")


# Класс рейса
class Flight:
    def __init__(self, details, airplane, crew):
        self.flight_number = details.flight_number
        self.airplane = airplane
        self.crew = crew
        self.departure_airport = details.departure_airport
        self.destination_airport = details.destination_airport
        self.is_canceled = False

    def check_flight_status(self):
        if self.is_canceled:
            print(f"Рейс {self.flight_number} отменен")
            return False
        if not self.departure_airport.is_good_weather:
            print(f"Рейс {self.flight_number} не может вылететь: плохая погода в {self.departure_airport}")
            return False
        if not self.destination_airport.is_good_weather:
            print(f"Рейс {self.flight_number} не может приземлиться: плохая погода в {self.destination_airport}")
            return False
        if self.airplane.has_technical_issue:
            print(f"Рейс {self.flight_number} имеет технические проблемы")
            return False
        return True

    def cancel_flight(self):
        self.is_canceled = True
        print(f"Рейс {self.flight_number} отменен")

    def change_destination(self, new_airport):
        if self.airplane.has_technical_issue:
            self.destination_airport = new_airport
            print(f"Рейс {self.flight_number} перенаправлен в {new_airport}")
        else:
            print("Нет причин менять аэропорт назначения")

    def __str__(self):
        return (
            f"Рейс {self.flight_number}: {self.departure_airport} -> {self.destination_airport}, "
            f"самолет: {self.airplane.model}, статус: {'отменен' if self.is_canceled else 'активен'}"
        )

# Класс администратора
class Administrator:
    def __init__(self, name):
        self.name = name

    def create_crew(self):
        return FlightCrew()

    def create_flight(self, details, airplane, crew):
        flight = Flight(details, airplane, crew)
        print(f"Администратор {self.name} создал рейс: {flight}")
        return flight


# Функции для ввода
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите число.")


def create_airports():
    airports = []
    num_airports = get_int_input("Сколько аэропортов вы хотите создать (минимум 2)? ")
    while num_airports < 2:
        print("Требуется минимум 2 аэропорта.")
        num_airports = get_int_input("Сколько аэропортов вы хотите создать (минимум 2)? ")

    for i in range(num_airports):
        name = input(f"Введите название аэропорта {i + 1}: ")
        weather_input = input("Хорошая погода в этом аэропорту? (да/нет): ").lower()
        is_good_weather = weather_input == "да"
        airports.append(Airport(name, is_good_weather))
    return airports


def create_airplane():
    plane_model = input("Введите модель самолета: ")
    plane_capacity = get_int_input("Введите вместимость самолета (пассажиры): ")
    plane_range = get_int_input("Введите дальность полета самолета (км): ")
    return Airplane(plane_model, plane_capacity, plane_range)


def create_crew(admin):
    crew = admin.create_crew()
    num_crew = get_int_input("Сколько членов экипажа вы хотите добавить? ")
    for i in range(num_crew):
        print(f"\nДобавление члена экипажа {i + 1}")
        name = input("Введите имя: ")
        age = get_int_input("Введите возраст: ")
        experience = get_float_input("Введите опыт (в годах): ")
        print("Выберите роль:")
        print("1. Пилот")
        print("2. Штурман")
        print("3. Радист")
        print("4. Стюардесса")
        role = get_int_input("Введите номер роли (1-4): ")
        while role not in [1, 2, 3, 4]:
            print("Неверный выбор роли.")
            role = get_int_input("Введите номер роли (1-4): ")

        if role == 1:
            crew.add_member(Pilot(name, age, experience))
        elif role == 2:
            crew.add_member(Navigator(name, age, experience))
        elif role == 3:
            crew.add_member(RadioOperator(name, age, experience))
        elif role == 4:
            crew.add_member(FlightAttendant(name, age, experience))
    return crew


def select_airport(airports, prompt, exclude_idx=None):
    print(prompt)
    for i, airport in enumerate(airports):
        print(f"{i + 1}. {airport}")
    idx = get_int_input("Введите номер аэропорта: ") - 1
    while idx < 0 or idx >= len(airports) or (exclude_idx is not None and idx == exclude_idx):
        print("Неверный выбор аэропорта.")
        idx = get_int_input("Введите номер аэропорта: ") - 1
    return idx


def create_flight(admin, airplane, crew, airports):
    flight_number = input("Введите номер рейса: ")
    dep_idx = select_airport(airports, "Выберите аэропорт вылета:")
    dest_idx = select_airport(airports, "Выберите аэропорт назначения:", exclude_idx=dep_idx)
    details = FlightDetails(flight_number, airports[dep_idx], airports[dest_idx])
    return admin.create_flight(details, airplane, crew)


def simulate_issues(flight, airports, dep_idx):
    simulate = input("\nХотите симулировать проблемы (погода/неисправность)? (да/нет): ").lower()
    if simulate != "да":
        return

    # Симуляция плохой погоды
    weather_idx = select_airport(airports, "\nВыберите аэропорт для изменения погоды:")
    airports[weather_idx].set_weather(False)

    if not flight.check_flight_status():
        flight.cancel_flight()

    # Симуляция технической неисправности
    print("\nСимуляция технической неисправности:")
    airports[weather_idx].set_weather(True)
    flight.airplane.report_issue()
    if not flight.check_flight_status():
        new_dest_idx = select_airport(airports, "Выберите новый аэропорт назначения:", exclude_idx=dep_idx)
        flight.change_destination(airports[new_dest_idx])

def main():
    admin_name = input("Введите имя администратора: ")
    admin = Administrator(admin_name)

    airports = create_airports()
    airplane = create_airplane()
    crew = create_crew(admin)
    crew.show_crew()

    flight = create_flight(admin, airplane, crew, airports)

    print("\nПроверка статуса рейса:")
    if flight.check_flight_status():
        print("Рейс готов к выполнению!")
        crew.do_jobs()

    simulate_issues(flight, airports, airports.index(flight.departure_airport))

    print(f"\nИтоговый статус: {flight}")


if __name__ == "__main__":
    main()
