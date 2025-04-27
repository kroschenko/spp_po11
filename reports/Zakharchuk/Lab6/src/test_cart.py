import pytest
from unittest.mock import patch

from shopping import Cart, apply_coupon


@pytest.fixture
def empty_cart():
    return Cart()


def test_add_item(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]["name"] == "Apple"
    assert empty_cart.items[0]["price"] == 10.0


def test_negative_price_raises_error(empty_cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        empty_cart.add_item("Apple", -10.0)


def test_total_calculation(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    empty_cart.add_item("Banana", 20.0)
    assert empty_cart.total() == 30.0


@pytest.mark.parametrize(
    "discount,expected_total",
    [
        (0, 10.0),
        (50, 5.0),
        (100, 0.0),
    ],
)
def test_apply_discount(empty_cart, discount, expected_total):
    empty_cart.add_item("Apple", 10.0)
    empty_cart.apply_discount(discount)
    assert empty_cart.total() == expected_total


@pytest.mark.parametrize("invalid_discount", [-1, 101])
def test_invalid_discount_raises_error(empty_cart, invalid_discount):
    empty_cart.add_item("Apple", 10.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        empty_cart.apply_discount(invalid_discount)


@patch("requests.post")
def test_log_purchase(mock_post, empty_cart):
    item = {"name": "Apple", "price": 10.0}
    empty_cart.add_item("Apple", 10.0)
    empty_cart.log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)


@pytest.mark.parametrize(
    "coupon_code,expected_total",
    [
        ("SAVE10", 9.0),
        ("HALF", 5.0),
    ],
)
def test_apply_coupon_valid(empty_cart, coupon_code, expected_total, monkeypatch):
    coupons = {"SAVE10": 10, "HALF": 50}
    monkeypatch.setattr("shopping.coupons", coupons)
    empty_cart.add_item("Apple", 10.0)
    apply_coupon(empty_cart, coupon_code)
    assert empty_cart.total() == expected_total


def test_apply_coupon_invalid(empty_cart, monkeypatch):
    coupons = {"SAVE10": 10, "HALF": 50}
    monkeypatch.setattr("shopping.coupons", coupons)
    empty_cart.add_item("Apple", 10.0)
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(empty_cart, "INVALID")
