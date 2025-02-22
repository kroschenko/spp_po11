class Rectangle:
    def __init__(self, rect_width: float, rect_height: float):
        if rect_width < 0 or rect_height < 0:
            raise ValueError("Ошибка: Ширина и высота прямоугольника должны быть положительными числами.")
        self._width = rect_width
        self._height = rect_height

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def is_square(self) -> bool:
        return self._width == self._height

    def is_valid(self) -> bool:
        return self._width > 0 and self._height > 0

    def __eq__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self._width == other.width and self._height == other.height
        return False

    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"


if __name__ == "__main__":
    try:
        width = float(input("Введите ширину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))
        rect = Rectangle(width, height)
        print(rect)
        print(f"Площадь: {rect.area()}")
        print(f"Периметр: {rect.perimeter()}")
        print(f"Является квадратом: {rect.is_square()}")
        print(f"Существует: {rect.is_valid()}")
        rect2 = Rectangle(4, 5)
        print(f"Сравнение с Rectangle(4, 5): {rect == rect2}")
    except ValueError as e:
        print(e)
