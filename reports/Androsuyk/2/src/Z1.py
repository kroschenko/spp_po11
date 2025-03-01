import math


class IsoscelesTriangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_isosceles(self):
        return (self.side_a == self.side_b) or (self.side_a == self.side_c) or (self.side_b == self.side_c)

    def exists(self):
        return (
            (self.side_a + self.side_b > self.side_c)
            and (self.side_a + self.side_c > self.side_b)
            and (self.side_b + self.side_c > self.side_a)
       )

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        if not self.exists():
            return 0
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def __str__(self):
        return f"Треугольник со сторонами: {self.side_a}, {self.side_b}, {self.side_c}"

    def __eq__(self, other):
        if not isinstance(other, IsoscelesTriangle):
            return False
        return sorted([self.side_a, self.side_b, self.side_c]) == sorted([other.side_a, other.side_b, other.side_c])

    # Свойства (getters и setters)
    @property
    def side_a(self):
        return self._side_a

    @side_a.setter
    def side_a(self, value):
        if value <= 0:
            raise ValueError("Длина стороны должна быть положительной")
        self._side_a = value

    @property
    def side_b(self):
        return self._side_b

    @side_b.setter
    def side_b(self, value):
        if value <= 0:
            raise ValueError("Длина стороны должна быть положительной")
        self._side_b = value

    @property
    def side_c(self):
        return self._side_c

    @side_c.setter
    def side_c(self, value):
        if value <= 0:
            raise ValueError("Длина стороны должна быть положительной")
        self._side_c = value


def input_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Число должно быть положительным. Попробуйте снова.")
            else:
                return value
        except ValueError:
            print("Ошибка: введите число.")


if __name__ == "__main__":
    print("Введите длины сторон треугольника:")
    _side_a = input_positive_number("Введите длину первой стороны: ")
    _side_b = input_positive_number("Введите длину второй стороны: ")
    _side_c = input_positive_number("Введите длину третьей стороны: ")

    triangle = IsoscelesTriangle(_side_a, _side_b, _side_c)

    if not triangle.exists():
        print("\nТреугольник с такими сторонами не существует.")
    else:
        if triangle.is_isosceles():
            print("\nТреугольник является равнобедренным.")
            print(f"Периметр треугольника: {triangle.perimeter()}")
            print(f"Площадь треугольника: {triangle.area():.2f}")
        else:
            print("\nТреугольник не является равнобедренным.")

    print(triangle)
