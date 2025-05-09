import pytest
from unittest.mock import patch
from shopping import ShoppingCart


@pytest.fixture
def empty_cart():
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    cart.add_item("apple", 2.5)
    cart.add_item("banana", 1.5)
    return cart


def test_add_item_to_cart(empty_cart):
    empty_cart.add_item("orange", 3.0)
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]["name"] == "orange"
    assert empty_cart.items[0]["price"] == 3.0


def test_add_multiple_items(empty_cart):
    empty_cart.add_item("orange", 3.0)
    empty_cart.add_item("orange", 3.0)
    assert len(empty_cart.items) == 2
    assert empty_cart.items[0]["name"] == "orange"
    assert empty_cart.items[1]["name"] == "orange"


def test_remove_item(cart_with_items):
    cart_with_items.remove_item("apple")
    assert len(cart_with_items.items) == 1
    assert cart_with_items.items[0]["name"] == "banana"


def test_remove_nonexistent_item(cart_with_items):
    with pytest.raises(ValueError):
        cart_with_items.remove_item("grape")


def test_calculate_total(cart_with_items):
    assert cart_with_items.calculate_total() == 4.0


def test_apply_discount(cart_with_items):
    cart_with_items.apply_discount(10)
    assert cart_with_items.calculate_total() == 3.6


def test_apply_invalid_discount(cart_with_items):
    with pytest.raises(ValueError):
        cart_with_items.apply_discount(120)


@patch("requests.post")
def test_log_purchase(mock_post, empty_cart):
    item = {"name": "orange", "price": 3.0}
    empty_cart.log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/purchase", json=item)


def test_apply_valid_coupon(empty_cart):
    empty_cart.add_item("item", 100.0)
    empty_cart.apply_coupon("DISCOUNT20")
    assert empty_cart.calculate_total() == 80.0


def test_apply_invalid_coupon(empty_cart):
    empty_cart.add_item("item", 100.0)
    with pytest.raises(ValueError, match="Неверный код купона"):
        empty_cart.apply_coupon("INVALID")
