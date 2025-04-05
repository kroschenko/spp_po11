class Driver:
    def __init__(self, name: str):
        self.name = name
        self.assigned_trips = []
        self.is_active = True

    def assign_trip(self, trip):
        if self.is_active:
            self.assigned_trips.append(trip)
            trip.assign_driver(self)
        else:
            print(f"Водитель {self.name} отстранён и не может быть назначен на рейс.")

    def report_trip_completion(self, trip, vehicle_condition: str):
        if trip in self.assigned_trips:
            trip.complete_trip(vehicle_condition)
        else:
            print("Рейс не найден среди назначенных.")

    def request_repair(self, dispatcher, vehicle, reason: str):
        dispatcher.create_repair_request(vehicle, self, reason)

    def __str__(self):
        return f"Водитель: {self.name}, Статус: {'Активен' if self.is_active else 'Отстранён'}"


class Vehicle:
    def __init__(self, model: str):
        self.model = model
        self.is_available = True

    def __str__(self):
        return f"Автомобиль: {self.model}, Статус: {'Доступен' if self.is_available else 'Недоступен'}"


class Trip:
    def __init__(self, destination: str):
        self.destination = destination
        self.driver = None
        self.vehicle = None
        self.completed = False
        self.vehicle_condition = None

    def assign_driver(self, driver):
        self.driver = driver

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        vehicle.is_available = False

    def complete_trip(self, condition: str):
        self.completed = True
        self.vehicle_condition = condition
        self.vehicle.is_available = True

    def __str__(self):
        status = "Завершен" if self.completed else "В процессе"
        return f"Рейс в {self.destination}, Статус: {status}"


class RepairRequest:
    def __init__(self, vehicle, driver, reason: str):
        self.vehicle = vehicle
        self.driver = driver
        self.reason = reason

    def __str__(self):
        return f"Заявка на ремонт: {self.vehicle.model} от {self.driver.name}, причина: {self.reason}"


class Dispatcher:
    def __init__(self, name: str):
        self.name = name
        self.repair_requests = []

    def assign_trip(self, driver, vehicle, trip):
        if driver.is_active and vehicle.is_available:
            driver.assign_trip(trip)
            trip.assign_vehicle(vehicle)
            print(f"Рейс в {trip.destination} назначен водителю {driver.name} на автомобиле {vehicle.model}")
        else:
            print("Невозможно назначить рейс. Проверьте статус водителя и автомобиля.")

    def create_repair_request(self, vehicle, driver, reason: str):
        request = RepairRequest(vehicle, driver, reason)
        self.repair_requests.append(request)
        print(f"Создана заявка на ремонт: {request}")

    def suspend_driver(self, driver):
        driver.is_active = False
        print(f"Водитель {driver.name} отстранён от работы.")

    def __str__(self):
        return f"Диспетчер: {self.name}"


def autobase_system():
    dispatcher = Dispatcher(input("Введите имя диспетчера: "))

    drivers = []
    vehicles = []
    trips = []

    while True:
        name = input("Введите имя водителя (или 'стоп'): ")
        if name.lower() == "стоп":
            break
        drivers.append(Driver(name))

    while True:
        model = input("Введите модель автомобиля (или 'стоп'): ")
        if model.lower() == "стоп":
            break
        vehicles.append(Vehicle(model))

    while True:
        dest = input("Введите пункт назначения рейса (или 'стоп'): ")
        if dest.lower() == "стоп":
            break
        trips.append(Trip(dest))

    while True:
        print(
            "\n1. Назначить рейс\n2. Заявка на ремонт\n3. Отстранить водителя\n4. Завершить рейс\n5. Показать заявки на ремонт\n0. Выход"
        )
        choice = input("Выберите действие: ")

        if choice == "1":
            for i, d in enumerate(drivers):
                print(f"{i+1}. {d}")
            driver = drivers[int(input("Выберите водителя: ")) - 1]
            for i, v in enumerate(vehicles):
                print(f"{i+1}. {v}")
            vehicle = vehicles[int(input("Выберите автомобиль: ")) - 1]
            for i, t in enumerate(trips):
                print(f"{i+1}. {t}")
            trip = trips[int(input("Выберите рейс: ")) - 1]
            dispatcher.assign_trip(driver, vehicle, trip)

        elif choice == "2":
            for i, d in enumerate(drivers):
                print(f"{i+1}. {d}")
            driver = drivers[int(input("Выберите водителя: ")) - 1]
            for i, v in enumerate(vehicles):
                print(f"{i+1}. {v}")
            vehicle = vehicles[int(input("Выберите автомобиль: ")) - 1]
            reason = input("Причина ремонта: ")
            driver.request_repair(dispatcher, vehicle, reason)

        elif choice == "3":
            for i, d in enumerate(drivers):
                print(f"{i+1}. {d}")
            driver = drivers[int(input("Выберите водителя: ")) - 1]
            dispatcher.suspend_driver(driver)

        elif choice == "4":
            for i, t in enumerate(trips):
                print(f"{i+1}. {t}")
            trip = trips[int(input("Выберите завершённый рейс: ")) - 1]
            condition = input("Состояние автомобиля после рейса: ")
            trip.driver.report_trip_completion(trip, condition)

        elif choice == "5":
            print("Заявки на ремонт:")
            for r in dispatcher.repair_requests:
                print(r)

        elif choice == "0":
            break


if __name__ == "__main__":
    autobase_system()
