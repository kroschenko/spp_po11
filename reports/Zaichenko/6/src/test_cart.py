from unittest.mock import patch
import pytest
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


def test_add_item_to_cart(cart):
    cart.add_item("orange", 3.0)
    assert len(cart.items) == 1
    assert cart.items[0]["name"] == "orange"
    assert cart.items[0]["price"] == 3.0


def test_add_multiple_items(cart):
    cart.add_item("orange", 3.0)
    cart.add_item("orange", 3.0)
    assert len(cart.items) == 2
    assert cart.items[0]["name"] == "orange"
    assert cart.items[1]["name"] == "orange"


def test_remove_item(cart_with_items_fixture):
    cart_with_items_fixture.remove_item("apple")
    assert len(cart_with_items_fixture.items) == 1
    assert cart_with_items_fixture.items[0]["name"] == "banana"


def test_remove_nonexistent_item(cart_with_items_fixture):
    with pytest.raises(ValueError):
        cart_with_items_fixture.remove_item("grape")


def test_calculate_total(cart_with_items_fixture):
    assert cart_with_items_fixture.calculate_total() == 4.0


def test_apply_discount(cart_with_items_fixture):
    cart_with_items_fixture.apply_discount(10)
    assert cart_with_items_fixture.calculate_total() == 3.6


def test_apply_invalid_discount(cart_with_items_fixture):
    with pytest.raises(ValueError):
        cart_with_items_fixture.apply_discount(120)


@patch("requests.post")
def test_log_purchase(mock_post, cart):
    item = {"name": "orange", "price": 3.0}
    cart.log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/purchase", json=item)


def test_apply_valid_coupon(cart):
    cart.add_item("item", 100.0)
    cart.apply_coupon("DISCOUNT20")
    assert cart.calculate_total() == 80.0


def test_apply_invalid_coupon(cart):
    cart.add_item("item", 100.0)
    with pytest.raises(ValueError, match="Неверный код купона"):
        cart.apply_coupon("INVALID")
