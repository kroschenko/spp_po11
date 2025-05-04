import math
import time
import tkinter as tk
from tkinter import colorchooser, ttk

from PIL import Image, ImageGrab


class KochSnowflake:
    def __init__(self, root):
        self.root = root
        self.root.title("Снежинка Коха")
        self.root.geometry("800x600")

        # Параметры снежинки
        self.depth = 0
        self.size = 300
        self.center_x = 400
        self.center_y = 300
        self.color = "blue"  # Цвет по умолчанию

        # Создание элементов управления
        self.create_controls()

        # Создание холста
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Отрисовка снежинки
        self.draw_snowflake()

    def create_controls(self):
        control_frame = ttk.Frame(self.root)
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
        # Делаем скриншот всего экрана
        screenshot = ImageGrab.grab()

        # Создаем имя файла с текущим временем
        filename = f"screenshot_{int(time.time())}.png"

        # Сохраняем скриншот
        screenshot.save(filename)
        print(f"Скриншот сохранен как {filename}")

    def draw_snowflake(self):
        self.canvas.delete("all")

        # Вычисляем координаты вершин равностороннего треугольника
        height = self.size * math.sqrt(3) / 2
        x1 = self.center_x - self.size / 2
        y1 = self.center_y + height / 2
        x2 = self.center_x + self.size / 2
        y2 = self.center_y + height / 2
        x3 = self.center_x
        y3 = self.center_y - height / 2

        # Рисуем три стороны снежинки
        self.draw_koch_line(x1, y1, x2, y2, self.depth)
        self.draw_koch_line(x2, y2, x3, y3, self.depth)
        self.draw_koch_line(x3, y3, x1, y1, self.depth)

    def draw_koch_line(self, x1, y1, x2, y2, depth):
        if depth == 0:
            self.canvas.create_line(x1, y1, x2, y2, width=2, fill=self.color)
        else:
            # Вычисляем точки деления отрезка
            dx = x2 - x1
            dy = y2 - y1

            # Точки деления на три части
            x1_3 = x1 + dx / 3
            y1_3 = y1 + dy / 3
            x2_3 = x1 + 2 * dx / 3
            y2_3 = y1 + 2 * dy / 3

            # Вычисляем вершину треугольника
            # Поворачиваем вектор на 60 градусов
            angle = math.radians(60)
            vx = (x2_3 - x1_3) * math.cos(angle) - (y2_3 - y1_3) * math.sin(angle)
            vy = (x2_3 - x1_3) * math.sin(angle) + (y2_3 - y1_3) * math.cos(angle)

            # Координаты вершины треугольника
            x_triangle = x1_3 + vx
            y_triangle = y1_3 + vy

            # Рекурсивно рисуем четыре отрезка
            self.draw_koch_line(x1, y1, x1_3, y1_3, depth - 1)
            self.draw_koch_line(x1_3, y1_3, x_triangle, y_triangle, depth - 1)
            self.draw_koch_line(x_triangle, y_triangle, x2_3, y2_3, depth - 1)
            self.draw_koch_line(x2_3, y2_3, x2, y2, depth - 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = KochSnowflake(root)
    root.mainloop()
