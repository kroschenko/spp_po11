from unittest.mock import patch

import pytest
from shopping import ShoppingCart


@pytest.fixture
def test_cart():
    return ShoppingCart()


@pytest.fixture
def test_filled_cart():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.add_item("banana", 0.5)
    return cart


def test_add_item(test_cart_fixture):
    """Тест добавления товара в корзину"""
    test_cart_fixture.add_item("apple", 1.0)
    assert len(test_cart_fixture.items) == 1
    assert test_cart_fixture.items[0]["name"] == "apple"
    assert test_cart_fixture.items[0]["price"] == 1.0


def test_add_item_with_quantity(test_cart_fixture):
    """Тест добавления товара с указанием количества"""
    test_cart_fixture.add_item("apple", 1.0)
    test_cart_fixture.add_item("apple", 1.0)
    assert len(test_cart_fixture.items) == 2
    assert test_cart_fixture.items[0]["name"] == "apple"
    assert test_cart_fixture.items[0]["price"] == 1.0
    assert test_cart_fixture.items[1]["name"] == "apple"
    assert test_cart_fixture.items[1]["price"] == 1.0


def test_add_existing_item(test_filled_cart_fixture):
    """Тест добавления существующего товара"""
    test_filled_cart_fixture.add_item("apple", 1.0)
    assert len(test_filled_cart_fixture.items) == 3
    assert test_filled_cart_fixture.items[0]["name"] == "apple"
    assert test_filled_cart_fixture.items[0]["price"] == 1.0


def test_remove_item(test_filled_cart_fixture):
    """Тест удаления товара из корзины"""
    test_filled_cart_fixture.remove_item("apple")
    assert len(test_filled_cart_fixture.items) == 1
    assert test_filled_cart_fixture.items[0]["name"] == "banana"


def test_remove_nonexistent_item(test_filled_cart_fixture):
    """Тест удаления несуществующего товара"""
    with pytest.raises(ValueError):
        test_filled_cart_fixture.remove_item("orange")


def test_remove_item_with_empty_name(test_filled_cart_fixture):
    """Тест удаления товара с пустым именем"""
    with pytest.raises(ValueError):
        test_filled_cart_fixture.remove_item("")


def test_get_total(test_filled_cart_fixture):
    """Тест расчета общей стоимости"""
    assert test_filled_cart_fixture.total() == 1.5


def test_apply_discount(test_filled_cart_fixture):
    """Тест применения скидки"""
    test_filled_cart_fixture.apply_discount(10)
    assert test_filled_cart_fixture.total() == 1.35


def test_apply_invalid_discount(test_filled_cart_fixture):
    """Тест применения недопустимой скидки"""
    with pytest.raises(ValueError):
        test_filled_cart_fixture.apply_discount(110)


@patch("requests.post")
def test_log_purchase(mock_post, test_cart_fixture):
    item = {"name": "Apple", "price": 10.0}
    test_cart_fixture.log_purchase(item)
    mock_post.assert_called_once_with("https://example.com/log", json=item)


def test_apply_coupon_valid(test_cart_fixture):
    """Тест применения валидного купона"""
    test_cart_fixture.add_item("Item", 100.0)
    test_cart_fixture.apply_coupon("SAVE10")
    assert test_cart_fixture.total() == 90.0


def test_apply_coupon_invalid(test_cart_fixture):
    """Тест применения невалидного купона"""
    test_cart_fixture.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Invalid coupon"):
        test_cart_fixture.apply_coupon("INVALID")
