from unittest.mock import patch

import pytest
from additional_functions import apply_coupon, log_purchase

from tests.shopping import Cart

Cart.log_purchase = staticmethod(log_purchase)
Cart.apply_coupon = staticmethod(apply_coupon)


@pytest.fixture
def cart_instance():
    return Cart()


def test_add_item():
    Cart.add_item("Apple", 10.0)
    assert len(Cart.items) == 1


def test_negative_price():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item("Apple", -10.0)


def test_total():
    Cart.add_item("Apple", 10.0)
    Cart.add_item("Banana", 5.0)
    assert Cart.total() == 15.0


@pytest.mark.parametrize(
    "discount, expected_price",
    [
        (0, 10.0),
        (50, 5.0),
        (100, 0.0),
    ],
)
def test_apply_discount(empty_cart, discount, expected_price):
    empty_cart.add_item("Apple", 10.0)
    empty_cart.apply_discount(discount)
    assert empty_cart.items[0]["price"] == expected_price


def test_invalid_discount():
    cart = Cart()
    cart.add_item("Apple", 10.0)
    with pytest.raises(ValueError):
        cart.apply_discount(-10)
    with pytest.raises(ValueError):
        cart.apply_discount(110)


@patch("requests.post")
def test_log_purchase(mock_post):
    item = {"name": "Test Item", "price": 10.0}
    log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)


def test_apply_coupon(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    apply_coupon(empty_cart, "SAVE10")
    assert empty_cart.items[0]["price"] == 9.0


def test_invalid_coupon(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    with pytest.raises(ValueError):
        apply_coupon(empty_cart, "INVALID")


@patch.dict("additional_functions.coupons", {"SAVE10": 20})
def test_apply_coupon_with_mocked_coupons(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    apply_coupon(empty_cart, "SAVE10")
    assert empty_cart.items[0]["price"] == 8.0
