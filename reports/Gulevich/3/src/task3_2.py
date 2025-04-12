from abc import ABC, abstractmethod


class RemoteControl(ABC):
    @abstractmethod
    def activate_alarm(self):
        pass

    @abstractmethod
    def lock_doors(self, lock: bool):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def get_remote_type(self):
        pass


class BasicRemote(RemoteControl):
    def activate_alarm(self):
        print("Сигнализация активирована (Basic)")

    def lock_doors(self, lock: bool):
        action = "закрыты" if lock else "открыты"
        print(f"Двери {action} (Basic)")

    def start_engine(self):
        print("Двигатель запущен (Basic)")

    def get_remote_type(self):
        return "Базовый пульт"


class AdvancedRemote(RemoteControl):
    def activate_alarm(self):
        print("Сигнализация активирована с GPS-отслеживанием (Advanced)")

    def lock_doors(self, lock: bool):
        action = "закрыты" if lock else "открыты"
        print(f"Двери {action} с автоматическим доводчиком (Advanced)")

    def start_engine(self):
        print("Двигатель запущен с прогревом (Advanced)")

    def get_remote_type(self):
        return "Продвинутый пульт"


class Car:
    def __init__(self, brand: str, model: str, remote: RemoteControl):
        self.brand = brand
        self.model = model
        self.remote = remote
        self.engine_on = False
        self.doors_locked = True

    def get_full_info(self):
        return f"{self.brand} {self.model} ({self.remote.get_remote_type()})"

    def toggle_engine(self):
        if self.engine_on:
            print("Двигатель заглушен")
            self.engine_on = False
            return

        self.remote.start_engine()
        self.engine_on = True

    def toggle_doors(self):
        self.doors_locked = not self.doors_locked
        self.remote.lock_doors(self.doors_locked)

    def activate_alarm(self):
        self.remote.activate_alarm()

    def get_status(self):
        return {
            "Двигатель": "включен" if self.engine_on else "выключен",
            "Двери": "закрыты" if self.doors_locked else "открыты"
        }


def create_remote(choice: str) -> RemoteControl:
    if choice == "1":
        return BasicRemote()
    return AdvancedRemote()


def create_car():
    print("\nСоздание нового автомобиля")
    brand = input("Введите марку автомобиля: ")
    model = input("Введите модель автомобиля: ")

    print("\nВыберите тип пульта ДУ:")
    print("1. Базовый")
    print("2. Продвинутый")
    remote_choice = input("Ваш выбор (1-2): ")

    remote = create_remote(remote_choice)
    return Car(brand, model, remote)


def show_car_status(car):
    status = car.get_status()
    for key, value in status.items():
        print(f"{key}: {value}")


def handle_car_control(car):
    while True:
        print(f"\nУправление автомобилем {car.get_full_info()}")
        print("1. Включить/выключить двигатель")
        print("2. Открыть/закрыть двери")
        print("3. Активировать сигнализацию")
        print("4. Показать состояние")
        print("5. Вернуться в меню")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            car.toggle_engine()
        elif choice == "2":
            car.toggle_doors()
        elif choice == "3":
            car.activate_alarm()
        elif choice == "4":
            show_car_status(car)
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


def main():
    cars = []

    while True:
        print("\nГлавное меню:")
        print("1. Добавить автомобиль")
        print("2. Управлять автомобилем")
        print("3. Выйти из программы")

        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            car = create_car()
            cars.append(car)
            print(f"\nАвтомобиль {car.get_full_info()} успешно добавлен!")
            continue

        if choice == "2":
            if not cars:
                print("Нет доступных автомобилей!")
                continue

            print("\nСписок автомобилей:")
            for i, car in enumerate(cars, 1):
                print(f"{i}. {car.get_full_info()}")

            car_num = int(input("Выберите номер автомобиля: ")) - 1
            if 0 <= car_num < len(cars):
                handle_car_control(cars[car_num])
            else:
                print("Неверный номер. Попробуйте снова.")
            continue

        if choice == "3":
            print("Выход из программы.")
            break

        print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
