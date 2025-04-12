class Driver:
    def __init__(self, name):
        self.name = name
        self.suspended = False

    def __str__(self):
        return f"Водитель: {self.name}{' (отстранён)' if self.suspended else ''}"

    def request_repair(self, dispatcher, vehicle, reason):
        dispatcher.repair_requests.append((self, vehicle, reason))

    def report_trip_completion(self, trip, vehicle_condition):
        trip.completed = True
        trip.vehicle.condition = vehicle_condition


class Vehicle:
    def __init__(self, model):
        self.model = model
        self.condition = "Хорошее"

    def __str__(self):
        return f"Автомобиль: {self.model}, состояние: {self.condition}"


class Trip:
    def __init__(self, destination):
        self.destination = destination
        self.driver = None
        self.vehicle = None
        self.completed = False

    def __str__(self):
        status = "выполнен" if self.completed else "не выполнен"
        return f"Рейс в {self.destination} ({status})"


class Dispatcher:
    def __init__(self):
        self.repair_requests = []

    def assign_trip(self, driver, vehicle, trip):
        if driver.suspended:
            print("Нельзя назначить отстранённого водителя.")
            return
        trip.driver = driver
        trip.vehicle = vehicle
        print(f"Назначен рейс: {driver.name} в {trip.destination} на {vehicle.model}.")

    def suspend_driver(self, driver):
        driver.suspended = True
        print(f"Водитель {driver.name} отстранён.")

    def show_repair_requests(self):
        if not self.repair_requests:
            print("Заявки на ремонт отсутствуют.")
            return
        print("Заявки на ремонт:")
        for d, v, r in self.repair_requests:
            print(f"Водитель: {d.name}, Автомобиль: {v.model}, Причина: {r}")


def select_from_list(prompt, items):
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")
    index = int(input(prompt)) - 1
    return items[index] if 0 <= index < len(items) else None


def handle_assignment(dispatcher, drivers, vehicles, trips):
    driver = select_from_list("Выберите водителя: ", drivers)
    vehicle = select_from_list("Выберите автомобиль: ", vehicles)
    trip = select_from_list("Выберите рейс: ", trips)
    if driver and vehicle and trip:
        dispatcher.assign_trip(driver, vehicle, trip)


def handle_repair_request(dispatcher, drivers, vehicles):
    driver = select_from_list("Выберите водителя: ", drivers)
    vehicle = select_from_list("Выберите автомобиль: ", vehicles)
    if driver and vehicle:
        reason = input("Причина ремонта: ")
        driver.request_repair(dispatcher, vehicle, reason)


def handle_suspend_driver(dispatcher, drivers):
    driver = select_from_list("Выберите водителя: ", drivers)
    if driver:
        dispatcher.suspend_driver(driver)


def handle_trip_completion(trips):
    trip = select_from_list("Выберите завершённый рейс: ", trips)
    if trip and trip.driver:
        condition = input("Состояние автомобиля после рейса: ")
        trip.driver.report_trip_completion(trip, condition)


def main_menu():
    print("\nВыберите действие:")
    actions = {
        "1": "Назначить рейс",
        "2": "Заявка на ремонт",
        "3": "Отстранить водителя",
        "4": "Завершить рейс",
        "5": "Показать заявки на ремонт",
        "0": "Выход"
    }
    for k, v in actions.items():
        print(f"{k}. {v}")
    return input("Введите номер действия: ")


def main():
    dispatcher = Dispatcher()
    drivers, vehicles, trips = [], [], []

    def input_loop(label, collection, cls):
        while True:
            value = input(f"Введите {label} (или 'стоп'): ")
            if value.lower() == "стоп":
                break
            collection.append(cls(value))

    input_loop("имя водителя", drivers, Driver)
    input_loop("модель автомобиля", vehicles, Vehicle)
    input_loop("пункт назначения рейса", trips, Trip)

    while True:
        choice = main_menu()

        if choice == "0":
            break
        if choice == "1":
            handle_assignment(dispatcher, drivers, vehicles, trips)
        elif choice == "2":
            handle_repair_request(dispatcher, drivers, vehicles)
        elif choice == "3":
            handle_suspend_driver(dispatcher, drivers)
        elif choice == "4":
            handle_trip_completion(trips)
        elif choice == "5":
            dispatcher.show_repair_requests()
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()


