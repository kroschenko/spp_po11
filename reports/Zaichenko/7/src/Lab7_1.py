import tkinter as tk
from tkinter import colorchooser
from dataclasses import dataclass  
from PIL import ImageGrab


@dataclass
class BallParams:
    radius: int
    speed: float
    color: str
    x: float
    y: float


class Ball:
    def __init__(self, params: BallParams):
        self.radius = params.radius
        self.speed = params.speed
        self.color = params.color
        self.x = params.x
        self.y = params.y
        self.direction = 1

    def move(self):
        self.x += self.speed * self.direction
        if self.x - self.radius < 0 or self.x + self.radius > 600:
            self.direction *= -1

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius,
                           fill=self.color, outline="black")


class App:
    def __init__(self, root):
        self.root = root
        self.color = "#000000"
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()
        self._create_controls()
        self.ball = None
        self.animating = False
        self.anim_id = None
        self.set_default_ball()
        self.draw()

    def _create_controls(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text="X").grid(row=0, column=0)
        tk.Label(frame, text="Y").grid(row=1, column=0)
        tk.Label(frame, text="Скорость").grid(row=2, column=0)

        self.x_entry = tk.Entry(frame, width=4)
        self.y_entry = tk.Entry(frame, width=4)
        self.speed_entry = tk.Entry(frame, width=4)

        self.x_entry.grid(row=0, column=1)
        self.y_entry.grid(row=1, column=1)
        self.speed_entry.grid(row=2, column=1)

        self.color_btn = tk.Button(frame, text="Выбрать цвет", command=self.choose_color)
        self.color_btn.grid(row=0, column=2)

        self.start_btn = tk.Button(frame, text="Старт", command=self.start_anim)
        self.start_btn.grid(row=3, column=0)

        self.stop_btn = tk.Button(frame, text="Стоп", command=self.stop_anim)
        self.stop_btn.grid(row=3, column=1)

        self.update_btn = tk.Button(frame, text="Обновить", command=self.update_ball)
        self.update_btn.grid(row=3, column=2)

        self.screenshot_btn = tk.Button(frame, text="Скриншот", command=self.screenshot)
        self.screenshot_btn.grid(row=3, column=3)

    def set_default_ball(self):
        self.x_entry.delete(0, tk.END)
        self.x_entry.insert(0, "100")
        self.y_entry.delete(0, tk.END)
        self.y_entry.insert(0, "200")
        self.speed_entry.delete(0, tk.END)
        self.speed_entry.insert(0, "5")
        self.update_ball()

    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет")
        if color[1]:
            self.color = color[1]
            self.color_btn.config(bg=self.color)
            self.update_ball()

    def update_ball(self):
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            speed = float(self.speed_entry.get())
            params = BallParams(radius=20, speed=speed, color=self.color, x=x, y=y)
            self.ball = Ball(params=params)
            self.draw()
        except ValueError as e:
            print("Ошибка параметров:", e)

    def draw(self):
        self.canvas.delete("all")
        if self.ball:
            self.ball.draw(self.canvas)

    def animate(self):
        if self.animating and self.ball:
            self.ball.move()
            self.draw()
            self.anim_id = self.root.after(30, self.animate)

    def start_anim(self):
        self.animating = True
        self.animate()

    def stop_anim(self):
        self.animating = False
        if self.anim_id:
            self.root.after_cancel(self.anim_id)
            self.anim_id = None

    def screenshot(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("screenshot.png")
        print("Скриншот сохранен!")


if __name__ == "__main__":
    tk_main = tk.Tk()
    app = App(tk_main)
    tk_main.mainloop()
