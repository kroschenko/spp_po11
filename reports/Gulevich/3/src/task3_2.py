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
        print("Сигнализация активирована")

    def lock_doors(self, lock: bool):
        print(f"Двери {'закрыты' if lock else 'открыты'}")

    def start_engine(self):
        print("Двигатель запущен")

    def get_remote_type(self):
        return "Базовый"


class AdvancedRemote(RemoteControl):
    def activate_alarm(self):
        print("Сигнализация активирована с GPS отслеживанием")

    def lock_doors(self, lock: bool):
        print(f"Двери {'закрыты' if lock else 'открыты'} с автоматическим доводчиком")

    def start_engine(self):
        print("Двигатель запущен с автоматическим прогревом")

    def get_remote_type(self):
        return "Продвинутый"


class Car:
    def __init__(self, brand: str, model: str, remote: RemoteControl):
        self.brand = brand
        self.model = model
        self.remote = remote
        self.engine_on = False
        self.doors_locked = True

    def get_info(self):
        return f"{self.brand} {self.model} ({self.remote.get_remote_type()} ДУ)"

    def toggle_engine(self):
        if self.engine_on:
            print("Двигатель заглушен")
            self.engine_on = False
        else:
            self.remote.start_engine()
            self.engine_on = True

    def toggle_doors(self):
        self.doors_locked = not self.doors_locked
        self.remote.lock_doors(self.doors_locked)

    def activate_alarm(self):
        self.remote.activate_alarm()

    def get_status(self):
        print(
            f"Состояние: двигатель {'включен' if self.engine_on else 'выключен'}, "
            f"двери {'закрыты' if self.doors_locked else 'открыты'}"
        )


def create_remote():
    while True:
        print("\nВыберите тип пульта ДУ:")
        print("1. Базовый")
        print("2. Продвинутый")
        choice = input("Ваш выбор (1-2): ")

        if choice == "1":
            return BasicRemote()
        if choice == "2":
            return AdvancedRemote()
        print("Неверный ввод. Попробуйте снова.")


def create_car():
    print("\nСоздание нового автомобиля")
    brand = input("Введите марку автомобиля: ")
    model = input("Введите модель автомобиля: ")
    remote = create_remote()
    return Car(brand, model, remote)


def car_control_menu():
    print("\n1. Включить/выключить двигатель")
    print("2. Открыть/закрыть двери")
    print("3. Активировать сигнализацию")
    print("4. Показать состояние")
    print("5. Вернуться в меню")


def car_control(car):
    while True:
        print(f"\nУправление автомобилем {car.get_info()}")
        car_control_menu()
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            car.toggle_engine()
        elif choice == "2":
            car.toggle_doors()
        elif choice == "3":
            car.activate_alarm()
        elif choice == "4":
            car.get_status()
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


def select_car(cars):
    print("\nСписок автомобилей:")
    for i, car in enumerate(cars, 1):
        print(f"{i}. {car.get_info()}")

    while True:
        try:
            car_num = int(input("Выберите номер автомобиля: ")) - 1
            if 0 <= car_num < len(cars):
                return car_num
            print("Неверный номер. Попробуйте снова.")
        except ValueError:
            print("Введите число!")


def main_menu():
    print("\nГлавное меню:")
    print("1. Добавить автомобиль")
    print("2. Управлять автомобилем")
    print("3. Выйти из программы")


def main():
    cars = []

    while True:
        main_menu()
        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            car = create_car()
            cars.append(car)
            print(f"\nАвтомобиль {car.get_info()} успешно добавлен!")
        elif choice == "2":
            if not cars:
                print("Нет доступных автомобилей!")
                continue

            car_num = select_car(cars)
            car_control(cars[car_num])
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
