class Product:
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        return f"Product: {self.name}"


class ChocolateBar(Product):
    def __init__(self):
        super().__init__("ChocolateBar")


class Chips(Product):
    def __init__(self):
        super().__init__("Chips")


class Juice(Product):
    def __init__(self):
        super().__init__("Juice")


class ProductFactory:
    products = {
        "ChocolateBar": ChocolateBar,
        "Chips": Chips,
        "Juice": Juice,
    }

    @staticmethod
    def createProduct(product_name: str) -> Product:
        product_class = ProductFactory.products.get(product_name)
        if product_class:
            return product_class()
        raise ValueError("Unknown type of products")


if __name__ == "__main__":
    while True:
        product_type: str = input("Enter the type of product: ")
        if product_type == "q":
            break
        try:
            product: Product = ProductFactory.createProduct(product_type)
            print(product.getInfo() + " created!   ")
        except ValueError as e:
            print(e)
