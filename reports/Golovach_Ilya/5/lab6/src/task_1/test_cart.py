from unittest.mock import patch, MagicMock
import pytest
from shopping import Cart, log_purchase, apply_coupon

# Фикстура для пустой корзины
@pytest.fixture
def empty_cart():  # Переименовано для ясности
    return Cart()

# Тест добавления товара
def test_add_item(empty_cart):  # Используем новое имя фикстуры
    empty_cart.add_item("Apple", 10.0)
    assert len(empty_cart.items) == 1
    assert empty_cart.items[0]["name"] == "Apple"
    assert empty_cart.items[0]["price"] == 10.0

# Тест на отрицательную цену
def test_negative_price(empty_cart):
    with pytest.raises(ValueError, match="Price cannot be negative"):
        empty_cart.add_item("Apple", -10.0)

# Тест вычисления общей стоимости
def test_total(empty_cart):
    empty_cart.add_item("Apple", 10.0)
    empty_cart.add_item("Banana", 20.0)
    assert empty_cart.total() == 30.0

# Параметризованный тест для apply_discount
@pytest.mark.parametrize("discount, expected_total", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount(empty_cart, discount, expected_total):
    empty_cart.add_item("Item", 100.0)
    empty_cart.apply_discount(discount)
    assert empty_cart.total() == expected_total

# Тест на недопустимые значения скидки
@pytest.mark.parametrize("invalid_discount", [-10, 110])
def test_invalid_discount(empty_cart, invalid_discount):
    empty_cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        empty_cart.apply_discount(invalid_discount)

# Тест для log_purchase с моком requests.post
@patch('requests.post')
def test_log_purchase(mock_post):
    test_item = {"name": "Apple", "price": 10.0}
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response
    log_purchase(test_item)
    mock_post.assert_called_once_with(
        "https://example.com/log",
        json=test_item
    )

# Тесты для apply_coupon
def test_apply_coupon_valid(empty_cart):
    empty_cart.add_item("Item", 100.0)
    apply_coupon(empty_cart, "SAVE10")
    assert empty_cart.total() == 90.0  # 10% скидка

def test_apply_coupon_invalid(empty_cart):
    empty_cart.add_item("Item", 100.0)
    with pytest.raises(ValueError, match="Invalid coupon"):
        apply_coupon(empty_cart, "INVALID")

# Тест с monkeypatch для мока словаря coupons
def test_apply_coupon_with_monkeypatch(empty_cart, monkeypatch):
    empty_cart.add_item("Item", 100.0)
    # Мокаем словарь купонов
    monkeypatch.setattr("shopping.coupons", {"TEST50": 50})
    apply_coupon(empty_cart, "TEST50")
    assert empty_cart.total() == 50.0
