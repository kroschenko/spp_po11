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


def get_valid_input(prompt, options):
    """Prompt user for input and validate against provided options."""
    print(f"Available options: {', '.join(options)}")
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print("Invalid choice. Try again.")


def create_order():
    """Prompt user to create a burger order interactively."""
    builder = BurgerBuilder()

    # Define valid options for each input
    burger_types = ["vegan", "chicken"]
    drinks = ["pepsi", "cola", "coffee", "tea"]
    packagings = ["takeaway", "eat_in"]

    # Collect user inputs using reusable validation function
    burger_type = get_valid_input("Choose burger type: ", burger_types)
    builder.set_burger_type(burger_type)

    drink = get_valid_input("Choose drink: ", drinks)
    builder.set_drink(drink)

    packaging = get_valid_input("Choose packaging: ", packagings)
    builder.set_packaging(packaging)

    return builder.build()


if __name__ == "__main__":
    order = create_order()
    print(order)
    print(f"Total cost: ${order.cost()}")
