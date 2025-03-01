import math

class IsoscelesTriangle:
    def __init__(self, side_a, side_b, side_c):
        """
        Конструктор класса.
        :param side_a: длина первой стороны
        :param side_b: длина второй стороны
        :param side_c: длина третьей стороны
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_isosceles(self):
        """
        Проверяет, является ли треугольник равнобедренным.
        :return: True, если треугольник равнобедренный, иначе False
        """
        return (self.side_a == self.side_b) or (self.side_a == self.side_c) or (self.side_b == self.side_c)

    def exists(self):
        """
        Проверяет, существует ли треугольник с заданными сторонами.
        :return: True, если треугольник существует, иначе False
        """
        return (self.side_a + self.side_b > self.side_c) and \
               (self.side_a + self.side_c > self.side_b) and \
               (self.side_b + self.side_c > self.side_a)

    def perimeter(self):
        """
        Вычисляет периметр треугольника.
        :return: периметр треугольника
        """
        return self.side_a + self.side_b + self.side_c

    def area(self):
        """
        Вычисляет площадь треугольника по формуле Герона.
        :return: площадь треугольника
        """
        if not self.exists():
            return 0
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        :return: строковое описание треугольника
        """
        return f"Треугольник со сторонами: {self.side_a}, {self.side_b}, {self.side_c}"

    def __eq__(self, other):
        """
        Сравнивает два объекта класса IsoscelesTriangle.
        :param other: другой объект класса IsoscelesTriangle
        :return: True, если треугольники равны, иначе False
        """
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


# Ввод данных от пользователя
def input_positive_number(prompt):
    """
    Функция для ввода положительного числа.
    :param prompt: подсказка для пользователя
    :return: положительное число
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Число должно быть положительным. Попробуйте снова.")
            else:
                return value
        except ValueError:
            print("Ошибка: введите число.")


# Основная программа
if __name__ == "__main__":
    print("Введите длины сторон треугольника:")
    side_a = input_positive_number("Введите длину первой стороны: ")
    side_b = input_positive_number("Введите длину второй стороны: ")
    side_c = input_positive_number("Введите длину третьей стороны: ")

    # Создаем объект треугольника
    triangle = IsoscelesTriangle(side_a, side_b, side_c)

    # Проверяем существование треугольника
    if not triangle.exists():
        print("\nТреугольник с такими сторонами не существует.")
    else:
        # Проверяем, является ли треугольник равнобедренным
        if triangle.is_isosceles():
            print("\nТреугольник является равнобедренным.")
            print(f"Периметр треугольника: {triangle.perimeter()}")
            print(f"Площадь треугольника: {triangle.area():.2f}")
        else:
            print("\nТреугольник не является равнобедренным.")

    # Выводим информацию о треугольнике
    print(triangle)
    