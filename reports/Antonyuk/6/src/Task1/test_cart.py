from unittest.mock import patch
import pytest
from shopping import Cart, log_purchase, apply_coupon


@pytest.fixture(name="test_cart")
def empty_cart_fixture():
    """Fixture providing an empty cart for tests"""
    return Cart()


def test_add_item(test_cart):
    """Test adding item to cart"""
    test_cart.add_item("Apple", 10.0)
    assert len(test_cart.items) == 1
    assert test_cart.items[0]["name"] == "Apple"
    assert test_cart.items[0]["price"] == 10.0


def test_negative_price(test_cart):
    """Test adding item with negative price"""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        test_cart.add_item("Apple", -10.0)


def test_total(test_cart):
    """Test calculating total price"""
    test_cart.add_item("Apple", 10.0)
    test_cart.add_item("Banana", 5.0)
    assert test_cart.total() == 15.0


@pytest.mark.parametrize("discount,expected", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_valid_discounts(test_cart, discount, expected):
    """Test valid discount values"""
    test_cart.add_item("Item", 100.0)
    assert test_cart.apply_discount(discount) == expected


@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_invalid_discounts(test_cart, invalid_discount):
    """Test invalid discount values"""
    test_cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        test_cart.apply_discount(invalid_discount)


@patch('shopping.requests.post')
def test_log_purchase(mock_post):
    """Test logging purchase"""
    item = {"name": "Test", "price": 100}
    log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)


def test_apply_coupon_valid(test_cart):
    """Test applying valid coupon"""
    test_cart.add_item("Item", 100.0)
    with patch.dict('shopping.coupons', {"TEST": 20}):
        apply_coupon(test_cart, "TEST")
        assert test_cart.apply_discount(20) == 80.0


def test_apply_coupon_invalid(test_cart):
    """Test applying invalid coupon"""
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(test_cart, "INVALID")
