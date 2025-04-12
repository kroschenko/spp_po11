from unittest.mock import patch

import pytest
from shopping import ShoppingCart


@pytest.fixture
def empty_cart():
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.add_item("banana", 0.5)
    return cart


def test_add_item(empty_cart):
    """Тест добавления товара в корзину"""
    empty_cart.add_item("apple", 1.0)
    assert "apple" in empty_cart.items
    assert empty_cart.items["apple"] == 1.0


def test_add_item_with_quantity(empty_cart):
    """Тест добавления товара с указанием количества"""
    empty_cart.add_item("apple", 1.0, 2)
    assert empty_cart.items["apple"] == 2.0


def test_add_existing_item(cart_with_items):
    """Тест добавления существующего товара"""
    cart_with_items.add_item("apple", 1.0)
    assert cart_with_items.items["apple"] == 2.0


def test_remove_item(cart_with_items):
    """Тест удаления товара из корзины"""
    cart_with_items.remove_item("apple")
    assert "apple" not in cart_with_items.items


def test_remove_nonexistent_item(cart_with_items):
    """Тест удаления несуществующего товара"""
    with pytest.raises(ValueError):
        cart_with_items.remove_item("orange")


def test_remove_item_with_empty_name(cart_with_items):
    """Тест удаления товара с пустым именем"""
    with pytest.raises(ValueError):
        cart_with_items.remove_item("")


def test_get_total(cart_with_items):
    """Тест расчета общей стоимости"""
    assert cart_with_items.get_total() == 1.5


def test_apply_discount(cart_with_items):
    """Тест применения скидки"""
    cart_with_items.apply_discount(10)
    assert cart_with_items.get_total() == 1.35


def test_apply_invalid_discount(cart_with_items):
    """Тест применения недопустимой скидки"""
    with pytest.raises(ValueError):
        cart_with_items.apply_discount(110)


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
