import math


class Triangle:
    def __init__(self, a=1.0, b=1.0, c=1.0):
        """
        Конструктор класса Triangle с проверкой на равносторонность.
        :param a: длина первой стороны
        :param b: длина второй стороны
        :param c: длина третьей стороны
        """
        self.set_sides(a, b, c)

    def set_sides(self, a, b, c):
        """
        Устанавливает стороны треугольника с проверкой на равносторонность.
        :param a: длина первой стороны
        :param b: длина второй стороны
        :param c: длина третьей стороны
        """
        if not (math.isclose(a, b, rel_tol=1e-9) and math.isclose(a, c, rel_tol=1e-9)):
            raise ValueError("Треугольник должен быть равносторонним (все стороны равны)")

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длины сторон должны быть положительными числами")

        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    def perimeter(self):
        """Вычисление периметра треугольника"""
        return self._a + self._b + self._c

    def area(self):
        """Вычисление площади треугольника"""
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    def is_valid(self):
        """
        Проверка, соответствует ли треугольник неравенству треугольника
        Для равностороннего треугольника всегда True если стороны положительные
        """
        return self._a + self._b > self._c and self._a + self._c > self._b and self._b + self._c > self._a

    def __str__(self):
        """Строковое представление объекта"""
        return f"Равносторонний треугольник со сторонами: a={self._a}, b={self._b}, c={self._c}"

    def __eq__(self, other):
        """
        Сравнение двух треугольников на равенство сторон
        :param other: другой объект Triangle
        :return: True, если треугольники равны (по сторонам), иначе False
        """
        if not isinstance(other, Triangle):
            return False
        return math.isclose(self._a, other._a) and math.isclose(self._b, other._b) and math.isclose(self._c, other._c)


def validate_input(prompt):
    """Функция для валидации ввода чисел"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Длина стороны должна быть положительной. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print("Пожалуйста, введите корректное число.")


def main():
    print("Введите длины сторон равностороннего треугольника:")
    while True:
        try:
            a = validate_input("Введите длину стороны a: ")
            b = validate_input("Введите длину стороны b: ")
            c = validate_input("Введите длину стороны c: ")

            triangle = Triangle(a, b, c)
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Пожалуйста, введите равные длины для всех трех сторон.\n")

    print("\nИнформация о треугольнике:")
    print(triangle)
    print(f"Периметр: {triangle.perimeter()}")
    print(f"Площадь: {triangle.area():.2f}")
    print(f"Треугольник существует: {'да' if triangle.is_valid() else 'нет'}")

    # Создадим второй треугольник для сравнения
    print("\nСоздадим второй треугольник для сравнения:")
    while True:
        try:
            a2 = validate_input("Введите длину стороны a для второго треугольника: ")
            b2 = validate_input("Введите длину стороны b для второго треугольника: ")
            c2 = validate_input("Введите длину стороны c для второго треугольника: ")

            triangle2 = Triangle(a2, b2, c2)
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Пожалуйста, введите равные длины для всех трех сторон.\n")

    print(f"\nСравнение треугольников: {'равны' if triangle == triangle2 else 'не равны'}")


if __name__ == "__main__":
    main()
