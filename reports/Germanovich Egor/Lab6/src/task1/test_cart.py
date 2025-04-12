from unittest.mock import patch

import pytest
from shopping import ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart()


@pytest.fixture
def filled_cart():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.add_item("banana", 0.5)
    return cart


def test_add_item(cart):
    """Тест добавления товара в корзину"""
    cart.add_item("apple", 1.0)
    assert len(cart.items) == 1
    assert cart.items[0]["name"] == "apple"
    assert cart.items[0]["price"] == 1.0


def test_add_item_with_quantity(cart):
    """Тест добавления товара с указанием количества"""
    cart.add_item("apple", 1.0)
    cart.add_item("apple", 1.0)
    assert len(cart.items) == 2
    assert cart.items[0]["name"] == "apple"
    assert cart.items[0]["price"] == 1.0
    assert cart.items[1]["name"] == "apple"
    assert cart.items[1]["price"] == 1.0


def test_add_existing_item(filled_cart):
    """Тест добавления существующего товара"""
    filled_cart.add_item("apple", 1.0)
    assert len(filled_cart.items) == 3
    assert filled_cart.items[0]["name"] == "apple"
    assert filled_cart.items[0]["price"] == 1.0


def test_remove_item(filled_cart):
    """Тест удаления товара из корзины"""
    filled_cart.remove_item("apple")
    assert len(filled_cart.items) == 1
    assert filled_cart.items[0]["name"] == "banana"


def test_remove_nonexistent_item(filled_cart):
    """Тест удаления несуществующего товара"""
    with pytest.raises(ValueError):
        filled_cart.remove_item("orange")


def test_remove_item_with_empty_name(filled_cart):
    """Тест удаления товара с пустым именем"""
    with pytest.raises(ValueError):
        filled_cart.remove_item("")


def test_get_total(filled_cart):
    """Тест расчета общей стоимости"""
    assert filled_cart.total() == 1.5


def test_apply_discount(filled_cart):
    """Тест применения скидки"""
    filled_cart.apply_discount(10)
    assert filled_cart.total() == 1.35


def test_apply_invalid_discount(filled_cart):
    """Тест применения недопустимой скидки"""
    with pytest.raises(ValueError):
        filled_cart.apply_discount(110)


@patch("requests.post")
def test_log_purchase(mock_post, cart):
    item = {"name": "Apple", "price": 10.0}
    cart.log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)


def test_apply_coupon_valid(cart):
    """Тест применения валидного купона"""
    cart.add_item("Item", 100.0)
    cart.apply_coupon("SAVE10")
    assert cart.total() == 90.0


def test_apply_coupon_invalid(cart):
    """Тест применения невалидного купона"""
    cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Invalid coupon"):
        cart.apply_coupon("INVALID")
