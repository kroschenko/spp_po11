from unittest.mock import patch, Mock
import pytest
from shopping import Cart, log_purchase, apply_coupon


@pytest.fixture
def empty_cart():
    return Cart()


def test_add_item(cart_fixture):
    cart_fixture.add_item("Apple", 10.0)
    assert len(cart_fixture.items) == 1
    assert cart_fixture.items[0]["name"] == "Apple"
    assert cart_fixture.items[0]["price"] == 10.0


def test_add_item_negative_price(cart_fixture):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        cart_fixture.add_item("Apple", -10.0)


def test_total(cart_fixture):
    cart_fixture.add_item("Apple", 10.0)
    cart_fixture.add_item("Banana", 20.0)
    assert cart_fixture.total() == 30.0


@pytest.mark.parametrize(
    "discount, expected_total",
    [
        (0, 100.0),
        (50, 50.0),
        (100, 0.0),
    ],
)
def test_apply_discount_valid(cart_fixture, discount, expected_total):
    cart_fixture.add_item("Item", 100.0)
    cart_fixture.apply_discount(discount)
    assert cart_fixture.total() == expected_total


@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_apply_discount_invalid(cart_fixture, invalid_discount):
    cart_fixture.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        cart_fixture.apply_discount(invalid_discount)


def test_log_purchase():
    mock_response = Mock()
    mock_response.status_code = 200
    
    with patch("requests.post", return_value=mock_response) as mock_post:
        log_purchase({"item": "Apple", "price": 10.0})
        mock_post.assert_called_once_with("https://example.com/log", json={"item": "Apple", "price": 10.0})


def test_apply_coupon_valid(cart_fixture, monkeypatch):
    cart_fixture.add_item("Item", 100.0)
    monkeypatch.setattr("shopping.coupons", {"SAVE10": 10, "HALF": 50})
    apply_coupon(cart_fixture, "SAVE10")
    assert cart_fixture.total() == 90.0
    apply_coupon(cart_fixture, "HALF")
    assert cart_fixture.total() == 45.0


def test_apply_coupon_invalid(cart_fixture, monkeypatch):
    cart_fixture.add_item("Item", 100.0)
    monkeypatch.setattr("shopping.coupons", {"SAVE10": 10, "HALF": 50})
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(cart_fixture, "INVALID")
