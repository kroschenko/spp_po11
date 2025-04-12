from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, vehicle_type, interval):
        self.vehicle_type = vehicle_type
        self.interval = interval

    @abstractmethod
    def start(self):
        pass

    def breakdown(self):
        print(f"{self.vehicle_type} сломался. Необходимо вызвать резервный транспорт.")

    def change_interval(self, new_interval):
        self.interval = new_interval
        print(f"Интервал движения на маршруте увеличен до {new_interval} минут.")


class Bus(Transport):
    def __init__(self, interval):
        super().__init__("Автобус", interval)

    def start(self):
        print(f"{self.vehicle_type} начал движение с интервалом {self.interval} минут.")


class Trolleybus(Transport):
    def __init__(self, interval):
        super().__init__("Троллейбус", interval)

    def start(self):
        print(f"{self.vehicle_type} начал движение с интервалом {self.interval} минут.")


class ReserveTransport:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def start(self):
        print(f"Резервный {self.vehicle_type} вышел на маршрут.")


class Route:
    def __init__(self, route_name, transport):
        self.route_name = route_name
        self.transport = transport
        self.reserve_transport = None

    def start_route(self):
        print(f"Маршрут {self.route_name} начинается.")
        self.transport.start()

    def breakdown(self):
        print(f"На маршруте {self.route_name} произошла поломка.")
        if self.reserve_transport:
            self.reserve_transport.start()
        else:
            self.transport.change_interval(self.transport.interval + 5)

    def assign_reserve_transport(self, reserve_transport):
        self.reserve_transport = reserve_transport
        print(f"Резервный транспорт {reserve_transport.vehicle_type} назначен на маршрут {self.route_name}.")


class CityTransportSystem:
    def __init__(self):
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def start_all_routes(self):
        for route in self.routes:
            route.start_route()


def create_transport():
    vehicle_type = input("Введите тип транспортного средства (автобус/троллейбус): ").strip().lower()
    interval = int(input("Введите интервал движения (в минутах): "))

    if vehicle_type == "автобус":
        return Bus(interval)

    if vehicle_type == "троллейбус":
        return Trolleybus(interval)

    print("Неверный тип транспортного средства. Создаем автобус по умолчанию.")
    return Bus(interval)


def create_reserve_transport():
    vehicle_type = input("Введите тип резервного транспортного средства (автобус/троллейбус): ").strip().lower()

    if vehicle_type == "автобус":
        return ReserveTransport("Автобус")

    if vehicle_type == "троллейбус":
        return ReserveTransport("Троллейбус")

    print("Неверный тип резервного транспортного средства. Создаем автобус по умолчанию.")
    return ReserveTransport("Автобус")


def create_route():
    route_name = input("Введите название маршрута: ")
    transport = create_transport()
    route = Route(route_name, transport)
    return route


def main():
    city_transport_system = CityTransportSystem()

    num_routes = int(input("Введите количество маршрутов: "))
    for _ in range(num_routes):
        route = create_route()
        reserve_transport = create_reserve_transport()
        route.assign_reserve_transport(reserve_transport)
        city_transport_system.add_route(route)

    city_transport_system.start_all_routes()

    simulate_breakdown = input("\nХотите смоделировать поломку на маршруте? (да/нет): ").strip().lower()
    if simulate_breakdown == "да":
        route_name = input("Введите название маршрута для поломки: ")
        for route in city_transport_system.routes:
            if route.route_name == route_name:
                route.breakdown()


if __name__ == "__main__":
    main()
