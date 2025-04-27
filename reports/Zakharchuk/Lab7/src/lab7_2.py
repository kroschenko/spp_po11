import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk, ImageGrab
import numpy as np


class JuliaFractalApp:
    def __init__(self, root):  # pylint: disable=redefined-outer-name
        self.root = root
        self.root.title("Множество Жюлиа")

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        # Панель управления
        control_frame = tk.Frame(root)
        control_frame.pack()

        self.entries = {}
        for label in ["Re(c)", "Im(c)", "Итерации", "Масштаб"]:
            tk.Label(control_frame, text=label + ":").pack(side=tk.LEFT)
            entry = tk.Entry(control_frame, width=6)
            entry.pack(side=tk.LEFT)
            self.entries[label] = entry

        # Значения по умолчанию
        self.entries["Re(c)"].insert(0, "-0.7")
        self.entries["Im(c)"].insert(0, "0.27015")
        self.entries["Итерации"].insert(0, "300")
        self.entries["Масштаб"].insert(0, "1.5")

        tk.Button(control_frame, text="Построить", command=self.generate_fractal).pack(side=tk.LEFT)
        tk.Button(control_frame, text="Скриншот", command=self.take_screenshot).pack(side=tk.LEFT)

        self.image = None
        self.generate_fractal()

    def generate_fractal(self):
        try:
            creal = float(self.entries["Re(c)"].get())
            cimag = float(self.entries["Im(c)"].get())
            iterations = int(self.entries["Итерации"].get())
            zoom = float(self.entries["Масштаб"].get())
        except ValueError:
            print("Некорректный ввод параметров.")
            return

        width, height = 600, 600
        x = np.linspace(-zoom, zoom, width)
        y = np.linspace(-zoom, zoom, height)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        C = complex(creal, cimag)

        img = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(iterations):
            mask = np.abs(Z) <= 2
            Z[mask] = Z[mask] ** 2 + C
            img[mask] = (i % 4 * 64, i % 8 * 32, i % 16 * 16)

        pil_image = Image.fromarray(img)
        self.image = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def take_screenshot(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        screenshot = ImageGrab.grab().crop((x, y, x1, y1))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"julia_screenshot_{timestamp}.png"
        screenshot.save(filename)
        print(f"Скриншот сохранён как {filename}")


if __name__ == "__main__":
    root = tk.Tk()
    app = JuliaFractalApp(root)
    root.mainloop()