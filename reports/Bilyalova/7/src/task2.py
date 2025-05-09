import math
import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw


class SierpinskiTriangleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Треугольная салфетка Серпинского")

        # Параметры фрактала
        self.depth = 3
        self.width = 600
        self.height = 600
        self.bg_color = "white"
        self.triangle_color = "blue"
        self.padding = 20

        # Создаем холст для отрисовки
        self.canvas = tk.Canvas(
            master,
            width=self.width,
            height=self.height,
            bg=self.bg_color
        )
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Создаем панель управления
        self.control_frame = ttk.Frame(master)
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        # Элементы управления
        self._create_controls()

        self.draw_fractal()

    def _create_controls(self):
        """Создает элементы управления"""
        ttk.Label(self.control_frame, text="Глубина рекурсии:").pack(pady=5)
        self.depth_slider = ttk.Scale(
            self.control_frame,
            from_=0,
            to=8,
            command=self.update_depth
        )
        self.depth_slider.set(self.depth)
        self.depth_slider.pack(pady=5)

        self.depth_label = ttk.Label(
            self.control_frame,
            text=f"Текущая глубина: {self.depth}"
        )
        self.depth_label.pack(pady=5)

        ttk.Label(self.control_frame, text="Цвет треугольника:").pack(pady=5)
        self.color_btn = ttk.Button(
            self.control_frame,
            text="Выбрать",
            command=self.choose_color
        )
        self.color_btn.pack(pady=5)

        ttk.Label(self.control_frame, text="Цвет фона:").pack(pady=5)
        self.bg_color_btn = ttk.Button(
            self.control_frame,
            text="Выбрать",
            command=self.choose_bg_color
        )
        self.bg_color_btn.pack(pady=5)

        self.draw_btn = ttk.Button(
            self.control_frame,
            text="Нарисовать",
            command=self.draw_fractal
        )
        self.draw_btn.pack(pady=10)

        self.save_btn = ttk.Button(
            self.control_frame,
            text="Сохранить изображение",
            command=self.save_image
        )
        self.save_btn.pack(pady=10)

    def draw_fractal(self):
        """Отрисовывает фрактал на холсте"""
        self.canvas.delete("all")
        self.canvas.config(bg=self.bg_color)

        # Размеры треугольника с учетом отступов
        size = min(self.width, self.height) - 2 * self.padding
        height = size * math.sqrt(3) / 2

        # Координаты вершин
        points = self._calculate_triangle_points(size, height)

        # Рисуем фрактал
        self._draw_sierpinski_canvas(points, self.depth)

    def _calculate_triangle_points(self, size, height):
        """Вычисляет координаты вершин треугольника"""
        return [
            (self.width // 2, self.padding),
            (self.padding, self.padding + height),
            (self.padding + size, self.padding + height)
        ]

    def _draw_sierpinski_canvas(self, points, depth):
        """Рекурсивная отрисовка на холсте"""
        if depth == 0:
            self.canvas.create_polygon(
                *points,
                fill=self.triangle_color,
                outline="black"
            )
        else:
            # Вычисляем середины сторон
            mid_points = self._calculate_midpoints(points)

            # Рисуем 3 подтреугольника
            self._draw_sierpinski_canvas([points[0], mid_points[0], mid_points[1]], depth - 1)
            self._draw_sierpinski_canvas([mid_points[0], points[1], mid_points[2]], depth - 1)
            self._draw_sierpinski_canvas([mid_points[1], mid_points[2], points[2]], depth - 1)

    def _calculate_midpoints(self, points):
        """Вычисляет середины сторон треугольника"""
        return [
            ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2),
            ((points[0][0] + points[2][0]) / 2, (points[0][1] + points[2][1]) / 2),
            ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
        ]

    def update_depth(self, value):
        """Обновляет глубину рекурсии"""
        self.depth = int(float(value))
        self.depth_label.config(text=f"Текущая глубина: {self.depth}")

    def choose_color(self):
        """Выбор цвета треугольника"""
        color = colorchooser.askcolor(title="Выберите цвет треугольника")[1]
        if color:
            self.triangle_color = color

    def choose_bg_color(self):
        """Выбор цвета фона"""
        color = colorchooser.askcolor(title="Выберите цвет фона")[1]
        if color:
            self.bg_color = color
            self.canvas.config(bg=self.bg_color)

    def save_image(self):
        """Сохраняет изображение в файл"""
        image = Image.new("RGB", (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(image)

        # Рисуем фрактал на изображении
        self._draw_sierpinski_image(draw, self.depth)

        filetypes = [
            ("PNG файлы", "*.png"),
            ("JPEG файлы", "*.jpg"),
            ("Все файлы", "*.*")
        ]
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=filetypes
        )

        if not filename:
            return

        try:
            image.save(filename)
            messagebox.showinfo("Успешно", "Изображение сохранено")
        except (IOError, OSError) as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

    def _draw_sierpinski_image(self, draw, depth):
        """Отрисовка фрактала на изображении"""
        size = min(self.width, self.height) - 2 * self.padding
        height = size * math.sqrt(3) / 2
        points = self._calculate_triangle_points(size, height)
        self._draw_sierpinski_image_recursive(draw, points, depth)

    def _draw_sierpinski_image_recursive(self, draw, points, depth):
        """Рекурсивная отрисовка на изображении"""
        if depth == 0:
            draw.polygon(
                points,
                fill=self.triangle_color,
                outline="black"
            )
        else:
            mid_points = self._calculate_midpoints(points)
            self._draw_sierpinski_image_recursive(draw, [points[0], mid_points[0], mid_points[1]], depth - 1)
            self._draw_sierpinski_image_recursive(draw, [mid_points[0], points[1], mid_points[2]], depth - 1)
            self._draw_sierpinski_image_recursive(draw, [mid_points[1], mid_points[2], points[2]], depth - 1)


def main():
    root = tk.Tk()
    SierpinskiTriangleApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
