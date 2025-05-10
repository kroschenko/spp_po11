import threading
from abc import ABC, abstractmethod

# Базовый класс для всех музыкальных товаров
class MusicProduct(ABC):
    def __init__(self, name: str, price: float):
        self.name = name  # Название товара
        self.price = price  # Цена товара

    @abstractmethod
    def play_sample(self):
        """Воспроизведение демо-версии товара."""
        pass

    def __str__(self):
        return f"{self.name} (${self.price})"  # Строковое представление товара

# Конкретные классы для товаров разных музыкальных направлений
class RockMusic(MusicProduct):
    def play_sample(self):
        print(f"Воспроизводится рок-демо для {self.name}")

class PopMusic(MusicProduct):
    def play_sample(self):
        print(f"Воспроизводится поп-демо для {self.name}")

class ClassicalMusic(MusicProduct):
    def play_sample(self):
        print(f"Воспроизводится классическое демо для {self.name}")

# Абстрактная фабрика для создания музыкальных товаров
class MusicFactory(ABC):
    @abstractmethod
    def create_product(self, name: str, price: float) -> MusicProduct:
        pass

# Конкретные фабрики для каждого направления
class RockMusicFactory(MusicFactory):
    def create_product(self, name: str, price: float) -> MusicProduct:
        return RockMusic(name, price)

class PopMusicFactory(MusicFactory):
    def create_product(self, name: str, price: float) -> MusicProduct:
        return PopMusic(name, price)

class ClassicalMusicFactory(MusicFactory):
    def create_product(self, name: str, price: float) -> MusicProduct:
        return ClassicalMusic(name, price)

# Класс магазина
class MusicStore:
    def __init__(self):
        self.factories = {
            "rock": RockMusicFactory(),  # Фабрика для рока
            "pop": PopMusicFactory(),  # Фабрика для поп-музыки
            "classical": ClassicalMusicFactory(),  # Фабрика для классической музыки
        }

    def order_product(self, genre: str, name: str, price: float) -> MusicProduct:
        if genre not in self.factories:
            raise ValueError(f"Неизвестный музыкальный жанр: {genre}")
        factory = self.factories[genre]
        product = factory.create_product(name, price)
        print(f"Заказ товара: {product}")
        return product

# Функция для имитации поведения покупателя
def customer_behavior(store, customer_id, orders):
    print(f"Покупатель {customer_id} начал делать покупки...")
    for genre, name, price in orders:
        try:
            product = store.order_product(genre, name, price)
            product.play_sample()  # Воспроизведение демо-версии товара
        except ValueError as e:
            print(f"Покупатель {customer_id}: Ошибка - {e}")
    print(f"Покупатель {customer_id} завершил покупки.")

# Пример использования с многопоточностью
if __name__ == "__main__":
    # Создаем магазин
    store = MusicStore()

    # Определяем заказы для нескольких покупателей
    customer_orders = [
        ("rock", "Лучшие хиты", 19.99),  # Заказ рок-музыки
        ("pop", "Летний хит", 9.99),  # Заказ поп-музыки
        ("classical", "Симфония №5", 29.99),  # Заказ классической музыки
    ]

    # Создаем несколько потоков для имитации одновременного обслуживания
    threads = []
    for i in range(3):  # 3 покупателя
        thread = threading.Thread(target=customer_behavior, args=(store, i + 1, customer_orders))
        threads.append(thread)
        thread.start()  # Запуск потока

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    print("Все покупатели обслужены.")
    