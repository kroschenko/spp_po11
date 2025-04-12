import math

class RightTriangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("Длина стороны должна быть положительной.")
        self._a = value

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("Длина стороны должна быть положительной.")
        self._b = value

    @c.setter
    def c(self, value):
        if value <= 0:
            raise ValueError("Длина стороны должна быть положительной.")
        self._c = value

    def is_valid(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)

    def area(self):
        if not self.is_valid():
            raise ValueError("Треугольник с такими сторонами не существует.")
        return (self.a * self.b) / 2

    def perimeter(self):
        if not self.is_valid():
            raise ValueError("Треугольник с такими сторонами не существует.")
        return self.a + self.b + self.c

    def __str__(self):
        return "Прямоугольный треугольник"

    def __eq__(self, other):
        if not isinstance(other, RightTriangle):
            return False
        # Сравниваем стороны, учитывая порядок
        return sorted([self.a, self.b, self.c]) == sorted([other.a, other.b, other.c])

def input_triangle():
    try:
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))
        return RightTriangle(a, b, c)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

if __name__ == "__main__":
    print("Введите данные для первого треугольника:")
    triangle1 = input_triangle()

    if triangle1:
        print("\nПервый треугольник:")
        print(triangle1) 
        if triangle1.is_valid():
            print("Площадь:", triangle1.area())
            print("Периметр:", triangle1.perimeter())
        else:
            print("Треугольник с такими сторонами не существует.")

    print("\nВведите данные для второго треугольника:")
    triangle2 = input_triangle()

    if triangle2:
        print("\nВторой треугольник:")
        print(triangle2) 
        if triangle2.is_valid():
            print("Площадь:", triangle2.area())
            print("Периметр:", triangle2.perimeter())
        else:
            print("Треугольник с такими сторонами не существует.")

    if triangle1 and triangle2:
        print("\nСравнение треугольников:")
        print("Треугольник 1 и треугольник 2 равны?", triangle1 == triangle2)