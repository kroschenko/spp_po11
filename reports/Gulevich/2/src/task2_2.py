from enum import Enum


class CarType(Enum):
    TRUCK = "Грузовик"
    PASSENGER = "Легковой"


class Car:
    def __init__(self, car_id: str, model: str, car_type: CarType):
        self.car_id = car_id
        self.model = model
        self.type = car_type
        self.needs_repair = False

    def __str__(self):
        status = " (требуется ремонт)" if self.needs_repair else ""
        return f"{self.type.value} {self.model} (ID: {self.car_id}){status}"


class Truck(Car):
    def __init__(self, car_id: str, model: str, max_load: float):
        super().__init__(car_id, model, CarType.TRUCK)
        self.max_load = max_load


class PassengerCar(Car):
    def __init__(self, car_id: str, model: str, seats: int):
        super().__init__(car_id, model, CarType.PASSENGER)
        self.seats = seats


class Driver:
    def __init__(self, driver_id: str, name: str):
        self.driver_id = driver_id
        self.name = name
        self.is_active = True
        self.current_car = None
        self.current_trip = None

    def request_repair(self):
        if self.current_car:
            self.current_car.needs_repair = True
            return f"Заявка на ремонт {self.current_car} отправлена."
        return "Ошибка: у водителя нет автомобиля!"

    def complete_trip(self, car_status_ok: bool):
        if self.current_trip:
            self.current_trip.is_completed = True
            if not car_status_ok:
                self.current_car.needs_repair = True
            self.current_trip = None
            return f"Рейс завершен. Статус авто: {'OK' if car_status_ok else 'Требуется ремонт'}"
        return "Ошибка: нет активного рейса!"

    def __str__(self):
        status = " (отстранен)" if not self.is_active else ""
        car_info = f", Авто: {self.current_car}" if self.current_car else ""
        trip_info = f", Рейс: {self.current_trip}" if self.current_trip else ""
        return f"{self.name} (ID: {self.driver_id}){status}{car_info}{trip_info}"


class Trip:
    def __init__(self, trip_id: str, destination: str):
        self.trip_id = trip_id
        self.destination = destination
        self.is_completed = False

    def __str__(self):
        return f"Рейс {self.trip_id} -> {self.destination} ({'завершен' if self.is_completed else 'активен'})"


class Dispatcher:
    def __init__(self, name: str):
        self.name = name

    def assign_trip(self, driver: Driver, car: Car, trip: Trip):
        if not driver.is_active:
            return f"Ошибка: {driver.name} отстранен от работы!"
        if car.needs_repair:
            return f"Ошибка: {car} требует ремонта!"
        driver.current_car = car
        driver.current_trip = trip
        return f"Назначено: {driver.name} на {trip} с {car}"

    def suspend_driver(self, driver: Driver):
        driver.is_active = False
        driver.current_trip = None
        return f"{driver.name} отстранен от работы."


def create_car():
    print("\nСоздание автомобиля:")
    car_id = input("Введите ID автомобиля: ")
    model = input("Введите модель: ")
    car_type = input("Тип (1 - Грузовик, 2 - Легковой): ")
    if car_type == "1":
        max_load = float(input("Грузоподъемность (тонн): "))
        return Truck(car_id, model, max_load)
    else:
        seats = int(input("Количество мест: "))
        return PassengerCar(car_id, model, seats)


def create_driver():
    print("\nСоздание водителя:")
    driver_id = input("Введите ID водителя: ")
    name = input("Введите ФИО водителя: ")
    return Driver(driver_id, name)


def create_trip():
    print("\nСоздание рейса:")
    trip_id = input("Введите ID рейса: ")
    destination = input("Введите пункт назначения: ")
    return Trip(trip_id, destination)


def main():
    dispatcher = Dispatcher(input("Введите ФИО диспетчера: "))
    cars = []
    drivers = []
    trips = []

    while True:
        print("\n1. Добавить автомобиль")
        print("2. Добавить водителя")
        print("3. Создать рейс")
        print("4. Назначить рейс")
        print("5. Завершить рейс")
        print("6. Подать заявку на ремонт")
        print("7. Отстранить водителя")
        print("8. Показать всех водителей")
        print("9. Показать все автомобили")
        print("10. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            cars.append(create_car())
        elif choice == "2":
            drivers.append(create_driver())
        elif choice == "3":
            trips.append(create_trip())
        elif choice == "4":
            if not drivers or not cars or not trips:
                print("Ошибка: сначала создайте водителей, автомобили и рейсы!")
                continue
            print("Выберите водителя:")
            for i, driver in enumerate(drivers):
                print(f"{i + 1}. {driver}")
            driver_idx = int(input("Номер водителя: ")) - 1
            print("Выберите автомобиль:")
            for i, car in enumerate(cars):
                print(f"{i + 1}. {car}")
            car_idx = int(input("Номер автомобиля: ")) - 1
            print("Выберите рейс:")
            for i, trip in enumerate(trips):
                print(f"{i + 1}. {trip}")
            trip_idx = int(input("Номер рейса: ")) - 1
            print(dispatcher.assign_trip(drivers[driver_idx], cars[car_idx], trips[trip_idx]))
        elif choice == "5":
            print("Выберите водителя для завершения рейса:")
            for i, driver in enumerate(drivers):
                print(f"{i + 1}. {driver}")
            driver_idx = int(input("Номер водителя: ")) - 1
            status = input("Авто в порядке? (1 - Да, 2 - Нет): ") == "1"
            print(drivers[driver_idx].complete_trip(status))
        elif choice == "6":
            print("Выберите водителя:")
            for i, driver in enumerate(drivers):
                print(f"{i + 1}. {driver}")
            driver_idx = int(input("Номер водителя: ")) - 1
            print(drivers[driver_idx].request_repair())
        elif choice == "7":
            print("Выберите водителя для отстранения:")
            for i, driver in enumerate(drivers):
                print(f"{i + 1}. {driver}")
            driver_idx = int(input("Номер водителя: ")) - 1
            print(dispatcher.suspend_driver(drivers[driver_idx]))
        elif choice == "8":
            print("\nСписок водителей:")
            for driver in drivers:
                print(driver)
        elif choice == "9":
            print("\nСписок автомобилей:")
            for car in cars:
                print(car)
        elif choice == "10":
            break
        else:
            print("Неверный ввод!")


if __name__ == "__main__":
    main()
