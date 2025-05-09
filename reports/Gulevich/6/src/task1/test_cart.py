from unittest.mock import patch

import pytest
from shopping import Cart, apply_coupon, log_purchase


@pytest.fixture(name="test_cart")  # Явно задаем имя для фикстуры
def fixture_cart():
    return Cart()


def test_add_item(test_cart):
    test_cart.add_item("Apple", 10.0)
    assert len(test_cart.items) == 1
    assert test_cart.items[0]["name"] == "Apple"
    assert test_cart.items[0]["price"] == 10.0


def test_negative_price(test_cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        test_cart.add_item("Apple", -10.0)


def test_total(test_cart):
    test_cart.add_item("Apple", 10.0)
    test_cart.add_item("Banana", 5.0)
    assert test_cart.total() == 15.0


@pytest.mark.parametrize(
    "discount,expected",
    [
        (0, 10.0),
        (50, 5.0),
        (100, 0.0),
    ],
)
def test_apply_discount(test_cart, discount, expected):
    test_cart.add_item("Apple", 10.0)
    assert test_cart.apply_discount(discount) == expected


@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_invalid_discount(test_cart, invalid_discount):
    test_cart.add_item("Apple", 10.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        test_cart.apply_discount(invalid_discount)


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
def test_valid_coupons(test_cart, coupon_code, discount):
    test_cart.add_item("Apple", 100.0)
    apply_coupon(test_cart, coupon_code)
    assert test_cart.apply_discount(discount) == 100.0 * (1 - discount / 100)


def test_invalid_coupon(test_cart):
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(test_cart, "INVALID")


@patch("shopping.coupons", {"TEST": 20})
def test_monkeypatch_coupons(test_cart):
    test_cart.add_item("Apple", 100.0)
    apply_coupon(test_cart, "TEST")
    assert test_cart.apply_discount(20) == 80.0
