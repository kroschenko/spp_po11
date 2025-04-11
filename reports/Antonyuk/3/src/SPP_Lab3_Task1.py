from abc import ABC, abstractmethod
from datetime import datetime

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    @abstractmethod
    def get_info(self):
        pass

    def calculate_age(self):
        current_year = datetime.now().year
        age = current_year - self.year
        if age == 1:
            return f"{age} год"
        elif 2 <= age <= 4:
            return f"{age} года"
        else:
            return f"{age} лет"

class Sedan(Car):
    def get_info(self):
        return f"Седан {self.brand} {self.model} {self.year} года ({self.calculate_age()})"

class SUV(Car):
    def get_info(self):
        return f"Внедорожник {self.brand} {self.model} {self.year} года ({self.calculate_age()})"

class Truck(Car):
    def get_info(self):
        return f"Грузовик {self.brand} {self.model} {self.year} года ({self.calculate_age()})"

class CarFactory(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def create_sedan(self, model, year) -> Sedan:
        pass
    
    @abstractmethod
    def create_suv(self, model, year) -> SUV:
        pass
    
    @abstractmethod
    def create_truck(self, model, year) -> Truck:
        pass

class ToyotaFactory(CarFactory):
    def __init__(self):
        super().__init__("Toyota")
    
    def create_sedan(self, model, year) -> Sedan:
        return Sedan(self.brand, model if model else "Camry", year)
    
    def create_suv(self, model, year) -> SUV:
        return SUV(self.brand, model if model else "RAV4", year)
    
    def create_truck(self, model, year) -> Truck:
        return Truck(self.brand, model if model else "Hilux", year)

class FordFactory(CarFactory):
    def __init__(self):
        super().__init__("Ford")
    
    def create_sedan(self, model, year) -> Sedan:
        return Sedan(self.brand, model if model else "Focus", year)
    
    def create_suv(self, model, year) -> SUV:
        return SUV(self.brand, model if model else "Explorer", year)
    
    def create_truck(self, model, year) -> Truck:
        return Truck(self.brand, model if model else "F-150", year)

class VolkswagenFactory(CarFactory):
    def __init__(self):
        super().__init__("Volkswagen")
    
    def create_sedan(self, model, year) -> Sedan:
        return Sedan(self.brand, model if model else "Passat", year)
    
    def create_suv(self, model, year) -> SUV:
        return SUV(self.brand, model if model else "Tiguan", year)
    
    def create_truck(self, model, year) -> Truck:
        return Truck(self.brand, model if model else "Amarok", year)

def get_user_choice(options, prompt):
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    
    while True:
        choice = input("Ваш выбор: ")
        if choice in options:
            return choice
        print("Некорректный ввод. Попробуйте снова.")

def get_valid_year():
    current_year = datetime.now().year
    while True:
        try:
            year = int(input(f"Введите год выпуска (1886-{current_year}): "))
            if 1886 <= year <= current_year:
                return year
            print(f"Год должен быть между 1886 и {current_year}")
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    factories = {
        '1': ToyotaFactory(),
        '2': FordFactory(),
        '3': VolkswagenFactory()
    }
    
    car_types = {
        '1': ('Седан', 'create_sedan'),
        '2': ('Внедорожник', 'create_suv'),
        '3': ('Грузовик', 'create_truck')
    }
    
    print("\nСистема создания автомобилей с полными характеристиками")
    
    while True:
        # Выбор марки
        factory_options = {k: v.brand for k, v in factories.items()}
        factory_choice = get_user_choice(factory_options, "\nВыберите марку автомобиля:")
        factory = factories[factory_choice]
        
        # Выбор типа
        type_choice = get_user_choice(
            {k: v[0] for k, v in car_types.items()}, 
            "\nВыберите тип автомобиля:"
        )
        car_type, create_method = car_types[type_choice]
        
        # Ввод модели
        model = input(f"\nВведите модель {factory.brand} (или нажмите Enter для модели по умолчанию): ").strip()
        
        # Ввод года
        year = get_valid_year()
        
        # Создание автомобиля
        car = getattr(factory, create_method)(model, year)
        
        # Вывод результата
        print(f"\nСоздан автомобиль: {car.get_info()}")
        
        # Повтор
        if input("\nСоздать еще один автомобиль? (да/нет): ").lower() != 'да':
            print("\nСпасибо за использование системы!")
            break

if __name__ == "__main__":
    main()
