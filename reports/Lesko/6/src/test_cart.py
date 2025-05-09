from unittest.mock import patch
import pytest
from shopping import Cart, log_purchase, apply_coupon

@pytest.fixture
def test_cart():
    return Cart()

def test_add_item(cart):
    cart.add_item("Apple", 10.0)
    assert len(cart.items) == 1
    assert cart.items[0]["name"] == "Apple"
    assert cart.items[0]["price"] == 10.0

def test_negative_price(cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        cart.add_item("Apple", -10.0)

def test_total(cart):
    cart.add_item("Apple", 10.0)
    cart.add_item("Banana", 5.0)
    assert cart.total() == 15.0

@pytest.mark.parametrize("discount,expected", [
    (0, 10.0),
    (50, 5.0),
    (100, 0.0),
])
def test_apply_discount_valid(cart, discount, expected):
    cart.add_item("Apple", 10.0)
    assert cart.apply_discount(discount) == expected

@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_apply_discount_invalid(cart, invalid_discount):
    cart.add_item("Apple", 10.0)
    with pytest.raises(ValueError, match="Discount percentage must be between 0 and 100"):
        cart.apply_discount(invalid_discount)

@patch('shopping.requests.post')
def test_log_purchase(mock_post):
    item = {"name": "Apple", "price": 10.0}
    log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)

@pytest.mark.parametrize("coupon_code,expected_discount", [
    ("SAVE10", 10),
    ("HALF", 50),
])
def test_valid_coupons(cart, coupon_code, expected_discount):
    cart.add_item("Apple", 100.0)
    apply_coupon(cart, coupon_code)
    assert cart.apply_discount(expected_discount) == 100.0 * (1 - expected_discount / 100)

def test_invalid_coupon(cart):
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(cart, "INVALID")

@patch('shopping.COUPONS', {"NEW10": 10})
def test_coupon_monkeypatch(cart):
    cart.add_item("Apple", 100.0)
    apply_coupon(cart, "NEW10")
    assert cart.apply_discount(10) == 90.0
