from abc import ABC, abstractmethod

class Sedan(ABC):
    @abstractmethod
    def drive(self):
        pass

class SUV(ABC):
    @abstractmethod
    def drive(self):
        pass


class GermanSedan(Sedan):
    def drive(self):
        print("Немецкий седан")

class GermanSUV(SUV):
    def drive(self):
        print("Немецкий внедорожник")


class JapaneseSedan(Sedan):
    def drive(self):
        print("Японский седан")

class JapaneseSUV(SUV):
    def drive(self):
        print("Японский внедорожник")


class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Sedan:
        pass

    @abstractmethod
    def create_suv(self) -> SUV:
        pass


class GermanCarFactory(CarFactory):
    def create_sedan(self) -> Sedan:
        return GermanSedan()

    def create_suv(self) -> SUV:
        return GermanSUV()


class JapaneseCarFactory(CarFactory):
    def create_sedan(self) -> Sedan:
        return JapaneseSedan()

    def create_suv(self) -> SUV:
        return JapaneseSUV()


def user_interface():
    while True:
        print("Выберите завод:")
        print("1 — Немецкий завод")
        print("2 — Японский завод")
        print("0 — Выход")

        factory_choice = input("Ваш выбор: ").strip()
        if factory_choice == "0":
            print("До свидания!")
            break

        if factory_choice == "1":
            factory = GermanCarFactory()
        elif factory_choice == "2":
            factory = JapaneseCarFactory()
        else:
            print("Неверный выбор завода. Попробуйте снова.\n")
            continue

        print("\nВыберите тип автомобиля для производства:")
        print("1 — Седан")
        print("2 — Внедорожник")
        car_choice = input("Ваш выбор: ").strip()

        if car_choice == "1":
            car = factory.create_sedan()
            car.drive()
        elif car_choice == "2":
            car = factory.create_suv()
            car.drive()
        else:
            print("Неверный тип автомобиля. Попробуйте снова.\n")



if __name__ == "__main__":
    user_interface()