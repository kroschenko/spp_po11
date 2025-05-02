import pytest
from shopping import Cart, log_purchase, apply_coupon
import requests
from unittest.mock import patch, Mock

@pytest.fixture
def empty_cart():
    return Cart()

def test_add_item(empty_cart):
    cart = empty_cart
    cart.add_item("Apple", 10.0)
    assert len(cart.items) == 1
    assert cart.items[0]["name"] == "Apple"
    assert cart.items[0]["price"] == 10.0

def test_add_item_negative_price(empty_cart):
    cart = empty_cart
    with pytest.raises(ValueError, match="Price cannot be negative"):
        cart.add_item("Apple", -10.0)

def test_total(empty_cart):
    cart = empty_cart
    cart.add_item("Apple", 10.0)
    cart.add_item("Banana", 20.0)
    assert cart.total() == 30.0

@pytest.mark.parametrize("discount, expected_total", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount_valid(empty_cart, discount, expected_total):
    cart = empty_cart
    cart.add_item("Item", 100.0)
    cart.apply_discount(discount)
    assert cart.total() == expected_total

@pytest.mark.parametrize("invalid_discount", [
    -10, 110
])
def test_apply_discount_invalid(empty_cart, invalid_discount):
    cart = empty_cart
    cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        cart.apply_discount(invalid_discount)

def test_log_purchase():
    mock_response = Mock()
    mock_response.status_code = 200
    
    with patch('requests.post', return_value=mock_response) as mock_post:
        log_purchase({"item": "Apple", "price": 10.0})
        
        mock_post.assert_called_once_with(
            "https://example.com/log",
            json={"item": "Apple", "price": 10.0}
        )

def test_apply_coupon_valid(empty_cart, monkeypatch):
    cart = empty_cart
    cart.add_item("Item", 100.0)
    
    monkeypatch.setattr("shopping.coupons", {"SAVE10": 10, "HALF": 50})
    
    apply_coupon(cart, "SAVE10")
    assert cart.total() == 90.0
    
    apply_coupon(cart, "HALF")
    assert cart.total() == 45.0

def test_apply_coupon_invalid(empty_cart, monkeypatch):
    cart = empty_cart
    cart.add_item("Item", 100.0)
    
    monkeypatch.setattr("shopping.coupons", {"SAVE10": 10, "HALF": 50})
    
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(cart, "INVALID")
