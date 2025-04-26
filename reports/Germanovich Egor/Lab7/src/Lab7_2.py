import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab


class SierpinskiCarpetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ковер Серпинского")
        self.canvas_size = 600
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        frame = tk.Frame(root)
        frame.pack()
        tk.Label(frame, text="Глубина:").grid(row=0, column=0)
        self.depth_entry = tk.Entry(frame, width=4)
        self.depth_entry.insert(0, "3")
        self.depth_entry.grid(row=0, column=1)

        tk.Label(frame, text="Цвет:").grid(row=0, column=2)
        self.color_btn = tk.Button(frame, text="Выбрать", command=self.choose_color)
        self.color_btn.grid(row=0, column=3)
        self.color = "#0000FF"

        self.draw_btn = tk.Button(frame, text="Построить", command=self.draw_carpet)
        self.draw_btn.grid(row=0, column=4)
        self.screenshot_btn = tk.Button(frame, text="Скриншот", command=self.screenshot)
        self.screenshot_btn.grid(row=0, column=5)

    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет")
        if color[1]:
            self.color = color[1]
            self.color_btn.config(bg=self.color)

    def draw_carpet(self):
        try:
            depth = int(self.depth_entry.get())
            self.canvas.delete("all")
            self._draw_carpet(0, 0, self.canvas_size, depth)
        except Exception as e:
            print("Ошибка:", e)

    def _draw_carpet(self, x, y, size, depth):
        if depth == 0:
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=self.color, outline="")
        else:
            new_size = size // 3
            for dx in range(3):
                for dy in range(3):
                    if dx == 1 and dy == 1:
                        continue  # центр не закрашиваем
                    self._draw_carpet(x + dx * new_size, y + dy * new_size, new_size, depth - 1)

    def screenshot(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("sierpinski_carpet.png")


if __name__ == "__main__":
    root = tk.Tk()
    app = SierpinskiCarpetApp(root)
    root.mainloop()
