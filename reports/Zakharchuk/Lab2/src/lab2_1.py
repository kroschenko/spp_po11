import math

class IsoscelesTriangle:
    def __init__(self, a, b, c):
        if not (a == b or a == c or b == c):
            raise ValueError("Для равнобедренного треугольника две стороны должны быть равны")
        self.a = a
        self.b = b
        self.c = c

    def exists(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def perimeter(self):
        if self.exists():
            return self.a + self.b + self.c
        else:
            print("Такого треугольника не существует")
            return None

    def area(self):
        if self.exists():
            p = self.perimeter() / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            print("Такого треугольника не существует")
            return None

    def __eq__(self, other):
        if isinstance(other, IsoscelesTriangle):
            return sorted([self.a, self.b, self.c]) == sorted([other.a, other.b, other.c])
        return False

    def __str__(self):
        return f"Равнобедренный треугольник со сторонами: {self.a}, {self.b}, {self.c}"


# Ввод сторон треугольника
side1 = float(input("Введите первую сторону треугольника: "))
side2 = float(input("Введите вторую сторону треугольника: "))
side3 = float(input("Введите третью сторону треугольника: "))

# Проверка на равнобедренность
try:
    triangle = IsoscelesTriangle(side1, side2, side3)
    print(triangle)
    if triangle.exists():
        print("Периметр:", triangle.perimeter())
        print("Площадь:", triangle.area())
except ValueError as e:
    print(e)
