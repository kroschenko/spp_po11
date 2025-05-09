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
        self.depth_entry.insert(0, "3")
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
            start_x = 50
            start_y = 50
            size = self.canvas_size - 100
            self.peano(start_x, start_y, size, size, depth)
        except ValueError as e:
            print("Ошибка:", e)

    def peano(self, x, y, dx, dy, depth):
        if depth == 0:
            x1 = x + dx / 2
            y1 = y + dy / 2
            self.points.append((x1, y1))
        else:
            dx3 = dx / 3
            dy3 = dy / 3
            self.peano(x, y, dx3, dy3, depth - 1)
            self.peano(x + dx3, y, dx3, dy3, depth - 1)
            self.peano(x + 2 * dx3, y, dx3, dy3, depth - 1)
            self.peano(x + 2 * dx3, y + dy3, dx3, dy3, depth - 1)
            self.peano(x + dx3, y + dy3, dx3, dy3, depth - 1)
            self.peano(x, y + dy3, dx3, dy3, depth - 1)
            self.peano(x, y + 2 * dy3, dx3, dy3, depth - 1)
            self.peano(x + dx3, y + 2 * dy3, dx3, dy3, depth - 1)
            self.peano(x + 2 * dx3, y + 2 * dy3, dx3, dy3, depth - 1)

    def screenshot(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("peano_curve.png")

    def draw_curve(self):
        try:
            depth = int(self.depth_entry.get())
            self.canvas.delete("all")
            self.points = []
            start_x = 50
            start_y = 50
            size = self.canvas_size - 100
            self.peano(start_x, start_y, size, size, depth)
            self.draw_lines()
        except ValueError as e:
            print("Ошибка:", e)

    def draw_lines(self):
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill=self.color)


if __name__ == "__main__":
    tk_main = tk.Tk()
    app = PeanoCurveApp(tk_main)
    tk_main.mainloop()
