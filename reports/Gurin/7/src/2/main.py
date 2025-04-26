import turtle


def generate_dragon_curve(axiom: str, rules: dict, iterations: int) -> str:
    """
    Генерирует строку для фрактала по L-системе.

    Параметры:
    - axiom: начальная строка.
    - rules: словарь правил переписывания.
    - iterations: число итераций переписывания.

    Возвращает итоговую строку, где записаны команды для рисования.
    """
    sequence = axiom
    for _ in range(iterations):
        next_sequence = ""
        for ch in sequence:
            next_sequence += rules.get(ch, ch)
        sequence = next_sequence
    return sequence


def draw_dragon(sequence: str, step: float, angle: float):
    """
    Рисует кривую дракона по сгенерированной строке.

    Параметры:
    - sequence: строка команд.
    - step: длина шага для команды 'F'.
    - angle: угол поворота.
    """
    for command in sequence:
        if command == "F":
            turtle.forward(step)
        elif command == "+":
            turtle.left(angle)
        elif command == "-":
            turtle.right(angle)


def main():
    try:
        iterations = int(input("Введите число итераций (например, 10): "))
    except ValueError:
        print("Неверный ввод итераций. Используется значение по умолчанию: 10")
        iterations = 10

    try:
        step_length = float(input("Введите длину отрезка (например, 5): "))
    except ValueError:
        print("Неверный ввод длины. Используется значение по умолчанию: 5")
        step_length = 5

    pen_color = input("Введите цвет пера (например, blue): ")
    bg_color = input("Введите цвет фона (например, black): ")

    turtle.setup(width=800, height=600)
    turtle.title("Кривая дракона")
    turtle.bgcolor(bg_color)
    turtle.speed(0)
    turtle.color(pen_color)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.hideturtle()

    # Определение аксиомы и правил L-системы
    axiom = "FX"
    rules = {"X": "X+YF+", "Y": "-FX-Y"}

    # Генерация строки с командами
    instructions = generate_dragon_curve(axiom, rules, iterations)

    # Рисование кривой
    draw_dragon(instructions, step_length, 90)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
