"""Module for testing the shopping cart functionality."""

from unittest.mock import patch

import pytest

from .shopping import Cart, apply_coupon, log_purchase


@pytest.fixture
def cart():
    """Create and return an empty Cart instance.

    Returns:
        Cart: An empty shopping cart.
    """
    return Cart()


def test_add_item_adds_one_item(test_cart):
    """Test that adding an item increases the cart's item count and stores details correctly."""
    test_cart.add_item("Apple", 10.0)
    assert len(test_cart.items) == 1
    assert test_cart.items[0] == {"name": "Apple", "price": 10.0}


def test_add_item_negative_price_raises_error(test_cart):
    """Test that adding an item with a negative price raises a ValueError."""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        test_cart.add_item("Apple", -10.0)


def test_total_calculation(test_cart):
    """Test that the total price is calculated correctly for multiple items."""
    test_cart.add_item("Apple", 10.0)
    test_cart.add_item("Banana", 20.0)
    assert test_cart.total() == 30.0


@pytest.mark.parametrize(
    "discount, expected_total",
    [
        (0, 10.0),  # 0% discount
        (50, 5.0),  # 50% discount
        (100, 0.0),  # 100% discount
    ],
)
def test_apply_discount(test_cart, discount, expected_total):
    """Test that applying a discount correctly adjusts the total price.

    Args:
        test_cart (Cart): The cart fixture.
        discount (float): The discount percentage to apply.
        expected_total (float): The expected total price after discount.
    """
    test_cart.add_item("Apple", 10.0)
    test_cart.apply_discount(discount)
    assert test_cart.total() == expected_total


@pytest.mark.parametrize("invalid_discount", [-1, 101])
def test_apply_discount_invalid_raises_error(test_cart, invalid_discount):
    """Test that applying an invalid discount raises a ValueError.

    Args:
        test_cart (Cart): The cart fixture.
        invalid_discount (float): The invalid discount value to test.
    """
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        test_cart.apply_discount(invalid_discount)


@patch("requests.post")
def test_log_purchase(mock_post, test_cart):
    """Test that log_purchase sends the correct item data to the server.

    Args:
        mock_post: Mocked requests.post function.
        test_cart (Cart): The cart fixture.
    """
    item = {"name": "Apple", "price": 10.0}
    test_cart.add_item("Apple", 10.0)
    log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item, timeout=5)


def test_apply_coupon_valid(test_cart):
    """Test that applying valid coupon codes correctly adjusts the total price."""
    test_cart.add_item("Apple", 10.0)
    apply_coupon(test_cart, "SAVE10")
    assert test_cart.total() == 9.0  # 10% discount

    apply_coupon(test_cart, "HALF")
    assert test_cart.total() == 5.0  # 50% discount


def test_apply_coupon_invalid_raises_error(test_cart):
    """Test that applying an invalid coupon code raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(test_cart, "INVALID")


def test_apply_coupon_another_valid(test_cart):
    """Test that applying the HALF coupon correctly adjusts the total price."""
    test_cart.add_item("Apple", 10.0)
    apply_coupon(test_cart, "HALF")
    assert test_cart.total() == 5.0  # 50% discount
