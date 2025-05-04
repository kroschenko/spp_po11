from unittest.mock import MagicMock, patch

import pytest
from shopping import Cart, apply_coupon, log_purchase


@pytest.fixture
def empty_cart():
    return Cart()


def test_add_item(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]["name"] == "Apple"
    assert empty_cart.items[0]["price"] == 10.0


def test_negative_price(empty_cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        empty_cart.add_item("Apple", -10.0)


def test_total(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    empty_cart.add_item("Banana", 5.0)
    assert empty_cart.total() == 15.0


@pytest.mark.parametrize(
    "discount,expected",
    [
        (0, 10.0),
        (50, 5.0),
        (100, 0.0),
    ],
)
def test_apply_discount(empty_cart, discount, expected):
    empty_cart.add_item("Apple", 10.0)
    assert empty_cart.apply_discount(discount) == expected


@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_invalid_discount(empty_cart, invalid_discount):
    empty_cart.add_item("Apple", 10.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        empty_cart.apply_discount(invalid_discount)


@patch("shopping.requests.post")
def test_log_purchase(mock_post):
    item = {"name": "Apple", "price": 10.0}
    log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)


@pytest.mark.parametrize(
    "coupon_code,discount",
    [
        ("SAVE10", 10),
        ("HALF", 50),
    ],
)
def test_valid_coupons(empty_cart, coupon_code, discount):
    empty_cart.add_item("Apple", 100.0)
    apply_coupon(empty_cart, coupon_code)
    assert empty_cart.apply_discount(discount) == 100.0 * (1 - discount / 100)


def test_invalid_coupon(empty_cart):
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(empty_cart, "INVALID")


@patch("shopping.coupons", {"TEST": 20})
def test_monkeypatch_coupons(empty_cart):
    empty_cart.add_item("Apple", 100.0)
    apply_coupon(empty_cart, "TEST")
    assert empty_cart.apply_discount(20) == 80.0
