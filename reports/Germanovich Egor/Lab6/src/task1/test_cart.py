from unittest.mock import patch

import pytest
import requests
from shopping import Cart


@pytest.fixture
def empty_cart():
    return Cart()


def test_add_item(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]["name"] == "Apple"
    assert empty_cart.items[0]["price"] == 10.0


def test_add_item_negative_price(empty_cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        empty_cart.add_item("Apple", -10.0)


def test_total(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    empty_cart.add_item("Banana", 5.0)
    assert empty_cart.total() == 15.0


@pytest.mark.parametrize("discount,expected_total", [(0, 100.0), (50, 50.0), (100, 0.0)])
def test_apply_discount_valid(empty_cart, discount, expected_total):
    empty_cart.add_item("Item", 100.0)
    empty_cart.apply_discount(discount)
    assert empty_cart.total() == expected_total


@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_apply_discount_invalid(empty_cart, invalid_discount):
    empty_cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Invalid discount percent"):
        empty_cart.apply_discount(invalid_discount)


@patch("requests.post")
def test_log_purchase(mock_post, empty_cart):
    item = {"name": "Apple", "price": 10.0}
    empty_cart.log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)


def test_apply_coupon_valid(empty_cart):
    empty_cart.add_item("Item", 100.0)
    empty_cart.apply_coupon("SAVE10")
    assert empty_cart.total() == 90.0


def test_apply_coupon_invalid(empty_cart):
    empty_cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Invalid coupon"):
        empty_cart.apply_coupon("INVALID")
