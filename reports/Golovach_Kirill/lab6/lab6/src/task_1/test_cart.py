from unittest.mock import patch, MagicMock
import pytest
from shopping import Cart, log_purchase, apply_coupon

# Фикстура для пустой корзины с явным указанием имени для использования в тестах
@pytest.fixture(name="cart")  # Теперь фикстура будет доступна как 'cart' в тестах
def empty_cart_fixture():
    return Cart()

# Тест добавления товара
def test_add_item(cart):
    cart.add_item("Pear", 10.0)
    assert len(cart.items) == 1
    assert cart.items[0]["name"] == "Pear"
    assert cart.items[0]["price"] == 10.0

# Тест на отрицательную цену
def test_negative_price(cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        cart.add_item("Pear", -10.0)

# Тест вычисления общей стоимости
def test_total(cart):
    cart.add_item("Pear", 10.0)
    cart.add_item("Banana", 20.0)
    assert cart.total() == 30.0

# Параметризованный тест для apply_discount
@pytest.mark.parametrize("discount, expected_total", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount(cart, discount, expected_total):
    cart.add_item("Item", 100.0)
    cart.apply_discount(discount)
    assert cart.total() == expected_total

# Тест на недопустимые значения скидки
@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_invalid_discount(cart, invalid_discount):
    cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        cart.apply_discount(invalid_discount)

# Тест для log_purchase с моком requests.post
@patch('requests.post')
def test_log_purchase(mock_post):
    test_item = {"name": "Pear", "price": 10.0}
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response
    log_purchase(test_item)
    mock_post.assert_called_once_with(
        "https://example.com/log",
        json=test_item
    )

# Тесты для apply_coupon
def test_apply_coupon_valid(cart):
    cart.add_item("Item", 100.0)
    apply_coupon(cart, "SAVE10")
    assert cart.total() == 90.0  # 10% скидка

def test_apply_coupon_invalid(cart):
    cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(cart, "INVALID")

# Тест с monkeypatch для мока словаря coupons
def test_apply_coupon_with_monkeypatch(cart, monkeypatch):
    cart.add_item("Item", 100.0)
    monkeypatch.setattr("shopping.coupons", {"TEST50": 50})
    apply_coupon(cart, "TEST50")
    assert cart.total() == 50.0
