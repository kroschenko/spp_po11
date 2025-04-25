"""Module for managing burger orders using the Builder pattern."""


class Burger:
    """Class representing a burger order with type, drink, and packaging."""

    def __init__(self):
        self.burger_type = None
        self.drink = None
        self.packaging = None

    def __str__(self):
        """Return string representation of the burger order."""
        return f"Burger: {self.burger_type}, Drink: {self.drink}, Packaging: {self.packaging}"

    def cost(self):
        """Calculate total cost of the burger order."""
        cost_map = {
            "vegan": 10,
            "chicken": 12,
            "pepsi": 3,
            "cola": 3,
            "coffee": 4,
            "tea": 4,
            "takeaway": 1,
            "eat_in": 0,
        }
        burger_cost = cost_map.get(self.burger_type, 0)
        drink_cost = cost_map.get(self.drink, 0)
        packaging_cost = cost_map.get(self.packaging, 0)
        return burger_cost + drink_cost + packaging_cost


class BurgerBuilder:
    """Builder class for constructing a Burger object step-by-step."""

    def __init__(self):
        self.burger = Burger()

    def set_burger_type(self, burger_type):
        """Set the burger type."""
        self.burger.burger_type = burger_type
        return self

    def set_drink(self, drink):
        """Set the drink type."""
        self.burger.drink = drink
        return self

    def set_packaging(self, packaging):
        """Set the packaging type."""
        self.burger.packaging = packaging
        return self

    def build(self):
        """Return the constructed Burger object."""
        return self.burger


def create_order():
    """Prompt user to create a burger order interactively."""
    builder = BurgerBuilder()

    print("Available burgers: vegan, chicken")
    while True:
        burger_type = input("Choose burger type: ").lower()
        if burger_type in ["vegan", "chicken"]:
            builder.set_burger_type(burger_type)
            break
        print("Invalid choice. Try again.")

    print("Available drinks: pepsi, cola, coffee, tea")
    while True:
        drink = input("Choose drink: ").lower()
        if drink in ["pepsi", "cola", "coffee", "tea"]:
            builder.set_drink(drink)
            break
        print("Invalid choice. Try again.")

    print("Available packaging: takeaway, eat_in")
    while True:
        packaging = input("Choose packaging: ").lower()
        if packaging in ["takeaway", "eat_in"]:
            builder.set_packaging(packaging)
            break
        print("Invalid choice. Try again.")

    return builder.build()


if __name__ == "__main__":
    order = create_order()
    print(order)
    print(f"Total cost: ${order.cost()}")
