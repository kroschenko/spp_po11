"""Module for managing a shopping cart and related operations."""

import requests


class Cart:
    """A class representing a shopping cart with items and discount functionality."""

    def __init__(self):
        """Initialize an empty shopping cart with no items and zero discount."""
        self.items = []
        self.discount = 0

    def add_item(self, name, price):
        """Add an item to the cart with the specified name and price.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append({"name": name, "price": price})

    def total(self):
        """Calculate the total price of items in the cart after applying discount.

        Returns:
            float: The total price after discount.
        """
        total_price = sum(item["price"] for item in self.items)
        return total_price * (1 - self.discount / 100)

    def apply_discount(self, discount):
        """Apply a discount percentage to the cart.

        Args:
            discount (float): The discount percentage (0 to 100).

        Raises:
            ValueError: If the discount is not between 0 and 100.
        """
        if not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self.discount = discount


def log_purchase(item):
    """Log a purchase by sending item details to a remote server.

    Args:
        item (dict): The item details to log, containing name and price.
    """
    requests.post("https://example.com/log", json=item, timeout=5)


def apply_coupon(cart, coupon_code):
    """Apply a coupon code to the cart to set a discount.

    Args:
        cart (Cart): The shopping cart to apply the coupon to.
        coupon_code (str): The coupon code to apply.

    Raises:
        ValueError: If the coupon code is invalid.
    """
    coupons = {"SAVE10": 10, "HALF": 50}
    if coupon_code in coupons:
        cart.apply_discount(coupons[coupon_code])
    else:
        raise ValueError("Invalid coupon")
