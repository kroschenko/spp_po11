"""Railway ticket system for managing trains, passenger requests, and invoices."""

from datetime import datetime
from typing import List, Optional, Tuple


class Train:
    """Represents a train with details like ID, stations, price."""

    def __init__(
        self,
        train_id_: str,
        route_: Tuple[str, str],  # Tuple of (start_station, end_station)
        price_: float = 0.0,
        middle_stations_: Optional[List[str]] = None,
    ) -> None:
        """Initialize a train with given attributes."""
        self.train_id = train_id_
        self.route = route_  # Stores start and end stations as a tuple
        self.middle_stations = middle_stations_ if middle_stations_ is not None else []
        self.price = price_

    def __str__(self) -> str:
        """Return a string representation of the train."""
        return f"Поезд {self.train_id}: {self.route[0]} -> {self.route[1]}, Цена: {self.price}"

    def get_route(self) -> List[str]:
        """Return the full route including all stations."""
        return [self.route[0]] + self.middle_stations + [self.route[1]]


class Request:
    """Represents a passenger's travel request."""

    def __init__(self, p_name: str, destination_: str, date: datetime, time: str) -> None:
        """Initialize a request with passenger details."""
        self.p_name = p_name
        self.destination = destination_
        self.date = date
        self.time = time  # Time added for passenger request
        self.selected_train: Optional[Train] = None

    def __str__(self) -> str:
        """Return a string representation of the request."""
        return f"{self.p_name} - {self.destination} Дата: {self.date.date()} Время: {self.time}"

    def is_valid(self) -> bool:
        """Check if the request has valid attributes."""
        return bool(self.p_name and self.destination and self.date and self.time)


class Invoice:
    """Represents an invoice for a passenger's train ticket."""

    def __init__(self, request_: Request, train_: Train) -> None:
        """Initialize an invoice with request and train details."""
        self.request = request_
        self.train = train_
        self.amount = train_.price

    def __str__(self) -> str:
        """Return a string representation of the invoice."""
        return f"Счет {self.request.p_name}: Поезд {self.train.train_id}, Сумма: {self.amount}"

    def get_details(self) -> dict:
        """Return detailed information about the invoice."""
        return {
            "passenger": self.request.p_name,
            "train_id": self.train.train_id,
            "route": self.train.get_route(),
            "price": self.amount,
            "date": self.request.date,
        }


class RailwaySystem:
    """Manages trains, passenger requests, and ticketing operations."""

    def __init__(self) -> None:
        """Initialize an empty railway system."""
        self.trains: List[Train] = []
        self.requests: List[Request] = []

    def add_train(self, train_: Train) -> None:
        """Add a train to the system (for administrators)."""
        self.trains.append(train_)

    def create_request(self, p_name: str, destination_: str, date: datetime, time: str) -> Request:
        """Create and store a passenger request."""
        new_request = Request(p_name, destination_, date, time)
        self.requests.append(new_request)
        return new_request

    def find_trains(self, request_: Request) -> List[Train]:
        """Find trains matching the request's destination."""
        return [
            transport
            for transport in self.trains
            if request_.destination in [transport.route[1]] + transport.middle_stations
        ]

    def select_train(self, request_: Request, train_: Train) -> None:
        """Assign a train to a request (for passengers)."""
        request_.selected_train = train_

    def create_invoice(self, request_: Request) -> Invoice:
        """Create an invoice for a request with a selected train."""
        if request_.selected_train is None:
            raise ValueError("Поезд не выбран")
        return Invoice(request_, request_.selected_train)


def add_train_interactively(railway: RailwaySystem) -> None:
    """Interactively add a train to the railway system (for administrators)."""
    print("=== Добавление нового поезда (для администратора) ===")
    train_id = input("Введите номер поезда: ")
    start_station = input("Введите начальную станцию: ")
    end_station = input("Введите конечную станцию: ")
    print("Введите промежуточные станции (пустая строка для завершения):")
    stations = []
    while True:
        station = input("Промежуточная станция: ")
        if station == "":
            break
        stations.append(station)
    while True:
        try:
            price = float(input("Введите цену билета: "))
            if price < 0:
                raise ValueError("Цена не может быть отрицательной")
            break
        except ValueError as e:
            print(f"Ошибка: {e if str(e) else 'введите число'}")
    new_train = Train(train_id, (start_station, end_station), price, stations)
    railway.add_train(new_train)
    print("Поезд добавлен.")


def get_valid_date() -> datetime:
    """Prompt for and validate a travel date."""
    while True:
        try:
            travel_date = input("Введите дату поездки (ГГГГ-ММ-ДД): ")
            return datetime.strptime(travel_date, "%Y-%m-%d")
        except ValueError:
            print("Ошибка: введите дату в формате ГГГГ-ММ-ДД")


def get_valid_time() -> str:
    """Prompt for and validate a travel time."""
    while True:
        travel_time = input("Введите время поездки (ЧЧ:ММ): ")
        try:
            datetime.strptime(travel_time, "%H:%M")
            return travel_time
        except ValueError:
            print("Ошибка: введите время в формате ЧЧ:ММ")


def display_available_trains(trains: List[Train]) -> None:
    """Display a list of available trains."""
    print("\nДоступные поезда:")
    for i, train_item in enumerate(trains, 1):
        print(f"{i}. {train_item}")


def get_train_choice(trains: List[Train]) -> Optional[Train]:
    """Prompt user to select a train and return the chosen train or None if canceled."""
    while True:
        try:
            train_choice = int(input("Выберите номер поезда (0 для отмены): "))
            if train_choice == 0:
                print("Выбор отменен.")
                return None
            if 1 <= train_choice <= len(trains):
                return trains[train_choice - 1]
            print("Неверный номер поезда.")
        except ValueError:
            print("Ошибка: введите число.")


def process_train_selection(railway: RailwaySystem, req: Request, selected_train: Train) -> None:
    """Assign the selected train to the request and create an invoice."""
    railway.select_train(req, selected_train)
    invoice = railway.create_invoice(req)
    print("\nВаш счет на оплату создан:")
    print(invoice)


def select_train_interactively(railway: RailwaySystem, req: Request) -> None:
    """Interactively select a train for the given request."""
    matching_trains = railway.find_trains(req)
    if not matching_trains:
        print("Подходящих поездов не найдено.")
        return
    display_available_trains(matching_trains)
    selected_train = get_train_choice(matching_trains)
    if selected_train:
        process_train_selection(railway, req, selected_train)


def create_request_interactively(railway: RailwaySystem) -> None:
    """Interactively create a passenger request and process it (for passengers)."""
    print("=== Создание заявки (для пассажира) ===")
    passenger = input("Введите ваше имя: ")
    destination = input("Введите станцию назначения: ")
    date = get_valid_date()
    time = get_valid_time()
    new_request = railway.create_request(passenger, destination, date, time)
    print("Ваша заявка создана:", new_request)
    select_train_interactively(railway, new_request)


if __name__ == "__main__":
    print("=== Железнодорожная касса ===")
    system = RailwaySystem()
    while True:
        print("\n1. Добавить поезд (для администратора)")
        print("2. Создать заявку и выбрать поезд (для пассажира)")
        print("3. Показать все поезда")
        print("4. Показать все заявки")
        print("5. Выход")
        choice = input("Ваш выбор(1-5): ")
        if choice == "1":
            add_train_interactively(system)
        elif choice == "2":
            create_request_interactively(system)
        elif choice == "3":
            if not system.trains:
                print("Поездов нет.")
            else:
                print("\nСписок всех поездов:")
                for train in system.trains:
                    print(train)
        elif choice == "4":
            if not system.requests:
                print("Заявок нет.")
            else:
                print("\nСписок всех заявок:")
                for request in system.requests:
                    print(request)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
