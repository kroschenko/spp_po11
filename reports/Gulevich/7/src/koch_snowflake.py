import math
import time
import tkinter as tk
from tkinter import colorchooser, ttk

from PIL import ImageGrab


class KochSnowflake:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Снежинка Коха")
        self.root_window.geometry("800x600")

        # Параметры снежинки
        self.depth = 0
        self.size = 300
        self.center_x = 400
        self.center_y = 300
        self.color = "blue"  # Цвет по умолчанию

        # Создание элементов управления
        self.create_controls()

        # Создание холста
        self.canvas = tk.Canvas(root_window, width=800, height=600, bg="white")
        self.canvas.pack()

        # Отрисовка снежинки
        self.draw_snowflake()

    def create_controls(self):
        control_frame = ttk.Frame(self.root_window)
        control_frame.pack(pady=10)

        # Кнопка выбора цвета
        self.color_button = ttk.Button(control_frame, text="Выбрать цвет", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5)

        # Кнопка скриншота
        self.screenshot_button = ttk.Button(control_frame, text="Скриншот", command=self.take_screenshot)
        self.screenshot_button.pack(side=tk.LEFT, padx=5)

        # Слайдер глубины рекурсии
        self.depth_label = ttk.Label(control_frame, text="Глубина: 0")
        self.depth_label.pack(side=tk.LEFT, padx=5)

        self.depth_scale = ttk.Scale(control_frame, from_=0, to=7, orient=tk.HORIZONTAL, command=self.update_depth)
        self.depth_scale.set(0)
        self.depth_scale.pack(side=tk.LEFT, padx=5)

    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет снежинки")
        if color[1]:  # Если цвет выбран (не нажата кнопка отмены)
            self.color = color[1]
            self.draw_snowflake()

    def update_depth(self, value):
        try:
            self.depth = int(float(value))
            self.depth_label.config(text=f"Глубина: {self.depth}")
            self.draw_snowflake()
        except ValueError:
            pass

    def take_screenshot(self):
        screenshot = ImageGrab.grab()
        filename = f"screenshot_{int(time.time())}.png"
        screenshot.save(filename)
        print(f"Скриншот сохранен как {filename}")

    def draw_snowflake(self):
        self.canvas.delete("all")
        height = self.size * math.sqrt(3) / 2
        points = [
            (self.center_x - self.size / 2, self.center_y + height / 2),  # Нижняя левая точка
            (self.center_x + self.size / 2, self.center_y + height / 2),  # Нижняя правая точка
            (self.center_x, self.center_y - height / 2),  # Верхняя точка
        ]

        # Рисуем три стороны снежинки
        self.draw_koch_line(points[0], points[1], self.depth)
        self.draw_koch_line(points[1], points[2], self.depth)
        self.draw_koch_line(points[2], points[0], self.depth)

    def draw_koch_line(self, start_point, end_point, depth):
        """Рисует линию Коха с заданной глубиной рекурсии.

        Args:
            start_point: Кортеж (x, y) начальной точки
            end_point: Кортеж (x, y) конечной точки
            depth: Глубина рекурсии
        """
        if depth == 0:
            self.canvas.create_line(
                start_point[0], start_point[1], end_point[0], end_point[1], width=2, fill=self.color
            )
            return

        # Разбиваем отрезок на части
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]

        # Точки на 1/3 и 2/3 отрезка
        p1 = (start_point[0] + dx / 3, start_point[1] + dy / 3)
        p2 = (start_point[0] + 2 * dx / 3, start_point[1] + 2 * dy / 3)

        # Вычисляем вершину треугольника
        angle = math.radians(60)
        vx = (p2[0] - p1[0]) * math.cos(angle) - (p2[1] - p1[1]) * math.sin(angle)
        vy = (p2[0] - p1[0]) * math.sin(angle) + (p2[1] - p1[1]) * math.cos(angle)
        triangle_point = (p1[0] + vx, p1[1] + vy)

        # Рекурсивно рисуем 4 новых отрезка
        segments = [(start_point, p1), (p1, triangle_point), (triangle_point, p2), (p2, end_point)]

        for segment in segments:
            self.draw_koch_line(segment[0], segment[1], depth - 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = KochSnowflake(root)
    root.mainloop()
