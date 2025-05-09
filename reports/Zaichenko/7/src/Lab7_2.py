import tkinter as tk
from tkinter import colorchooser
import math
from PIL import ImageGrab


class PeanoCurveApp:
    def __init__(self, tk_root):
        self.root = tk_root
        self.root.title("Кривая Пеано")
        self.canvas_size = 600
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text="Глубина:").grid(row=0, column=0)
        self.depth_entry = tk.Entry(frame, width=4)
        self.depth_entry.insert(0, "4")
        self.depth_entry.grid(row=0, column=1)

        tk.Label(frame, text="Цвет:").grid(row=0, column=2)
        self.color_btn = tk.Button(frame, text="Выбрать", command=self.choose_color)
        self.color_btn.grid(row=0, column=3)
        self.color = "#0000FF"

        self.draw_btn = tk.Button(frame, text="Построить", command=self.draw_curve)
        self.draw_btn.grid(row=0, column=4)

        self.screenshot_btn = tk.Button(frame, text="Скриншот", command=self.screenshot)
        self.screenshot_btn.grid(row=0, column=5)

    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет")
        if color[1]:
            self.color = color[1]
            self.color_btn.config(bg=self.color)

    def draw_curve(self):
        try:
            depth = int(self.depth_entry.get())
            self.canvas.delete("all")
            self._draw_peano_curve(50, 50, self.canvas_size - 100, depth)
        except ValueError as e:
            print("Ошибка:", e)

    def _draw_peano_curve(self, x, y, size, depth):
        if depth == 0:
            return

        length = size / 3

        self._draw_peano_curve_segment(x, y, length, 0, depth)
        self._draw_peano_curve_segment(x + length, y, length, 90, depth)
        self._draw_peano_curve_segment(x + length, y + length, length, 180, depth)
        self._draw_peano_curve_segment(x, y + length, length, 270, depth)

    def _draw_peano_curve_segment(self, x, y, size, angle, depth):
        if depth == 0:
            dx = size * math.cos(math.radians(angle))
            dy = size * math.sin(math.radians(angle))
            x2 = x + dx
            y2 = y + dy
            self.canvas.create_line(x, y, x2, y2, fill=self.color)
            return x2, y2
        else:
            length = size / 3
            self._draw_peano_curve_segment(x, y, length, angle, depth - 1)
            self._draw_peano_curve_segment(x + length, y, length, angle + 90, depth - 1)
            self._draw_peano_curve_segment(x + length, y + length, length, angle + 180, depth - 1)
            self._draw_peano_curve_segment(x, y + length, length, angle + 270, depth - 1)

    def screenshot(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("peano_curve.png")


if __name__ == "__main__":
    tk_main = tk.Tk()
    app = PeanoCurveApp(tk_main)
    tk_main.mainloop()
