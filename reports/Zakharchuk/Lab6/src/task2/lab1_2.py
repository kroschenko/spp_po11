def generate_pascal_triangle(num_rows):
    """Генерирует треугольник Паскаля с заданным количеством строк."""
    if num_rows < 0:
        raise ValueError("Количество строк не может быть отрицательным")
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


def main():
    """Основная функция для ввода и вывода."""
    try:
        num = int(input("Введите количество строк: "))
        triangle = generate_pascal_triangle(num)
        for row in triangle:
            print(row)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
