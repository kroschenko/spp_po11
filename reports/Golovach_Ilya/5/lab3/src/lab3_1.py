from typing import Dict, Type

class Smartphone:
    def __init__(self, name: str):
        self.name = name

    def get_specs(self) -> str:
        return f"Smartphone: {self.name}"

class IPhone(Smartphone):
    def __init__(self):
        super().__init__('iPhone 15 Pro | A17 Pro | 6.1" OLED | 48MP')

class Galaxy(Smartphone):
    def __init__(self):
        super().__init__('Galaxy S23 Ultra | Snapdragon 8 Gen 2 | 6.8" AMOLED | 200MP')

class Pixel(Smartphone):
    def __init__(self):
        super().__init__('Pixel 8 Pro | Tensor G3 | 6.7" OLED | 50MP')

class SmartphoneFactory:
    _models: Dict[str, Type[Smartphone]] = {
        "iphone": IPhone,
        "galaxy": Galaxy,
        "pixel": Pixel,
    }

    @staticmethod
    def create_smartphone(model_name: str) -> Smartphone:
        model_class = SmartphoneFactory._models.get(model_name.lower())
        if model_class:
            return model_class()
        raise ValueError(f"Unknown smartphone model: {model_name}")

if __name__ == "__main__":
    print("Available models: iphone, galaxy, pixel")
    print("Enter 'q' to quit.")

    while True:
        user_input = input("Enter smartphone model: ").strip()
        if user_input == "q":
            break

        try:
            phone = SmartphoneFactory.create_smartphone(user_input)
            print(phone.get_specs())
        except ValueError as e:
            print(e)
