import math
import time
import tkinter as tk
from tkinter import ttk

from PIL import ImageGrab


class RotatingLineApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Вращающийся отрезок")
        self.root_window.geometry("800x600")

        # Параметры анимации
        self.rotation_angle = 0
        self.point_position = 0
        self.rotation_speed = 1
        self.point_speed = 0.5
        self.is_paused = False

        # Координаты отрезка
        self.x1 = 300
        self.y1 = 300
        self.x2 = 500
        self.y2 = 300

        # Создание элементов управления
        self.create_controls()

        # Создание холста
        self.canvas = tk.Canvas(root_window, width=800, height=600, bg="white")
        self.canvas.pack()

        # Запуск анимации
        self.animate()

    def create_controls(self):
        control_frame = ttk.Frame(self.root_window)
        control_frame.pack(pady=10)

        # Кнопка паузы
        self.pause_button = ttk.Button(control_frame, text="Пауза", command=self.toggle_pause)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        # Кнопка скриншота
        self.screenshot_button = ttk.Button(control_frame, text="Скриншот", command=self.take_screenshot)
        self.screenshot_button.pack(side=tk.LEFT, padx=5)

        # Трекбар скорости
        self.speed_label = ttk.Label(control_frame, text="Скорость: 5")
        self.speed_label.pack(side=tk.LEFT, padx=5)

        self.speed_scale = ttk.Scale(control_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.update_speed)
        self.speed_scale.set(5)
        self.speed_scale.pack(side=tk.LEFT, padx=5)

        # Поля ввода координат
        coord_frame = ttk.Frame(self.root_window)
        coord_frame.pack(pady=10)

        # X1
        ttk.Label(coord_frame, text="X1:").pack(side=tk.LEFT, padx=5)
        self.x1_entry = ttk.Entry(coord_frame, width=5)
        self.x1_entry.insert(0, str(self.x1))
        self.x1_entry.pack(side=tk.LEFT, padx=5)

        # Y1
        ttk.Label(coord_frame, text="Y1:").pack(side=tk.LEFT, padx=5)
        self.y1_entry = ttk.Entry(coord_frame, width=5)
        self.y1_entry.insert(0, str(self.y1))
        self.y1_entry.pack(side=tk.LEFT, padx=5)

        # X2
        ttk.Label(coord_frame, text="X2:").pack(side=tk.LEFT, padx=5)
        self.x2_entry = ttk.Entry(coord_frame, width=5)
        self.x2_entry.insert(0, str(self.x2))
        self.x2_entry.pack(side=tk.LEFT, padx=5)

        # Y2
        ttk.Label(coord_frame, text="Y2:").pack(side=tk.LEFT, padx=5)
        self.y2_entry = ttk.Entry(coord_frame, width=5)
        self.y2_entry.insert(0, str(self.y2))
        self.y2_entry.pack(side=tk.LEFT, padx=5)

        # Кнопка обновления координат
        self.update_coords_button = ttk.Button(coord_frame, text="Обновить", command=self.update_coordinates)
        self.update_coords_button.pack(side=tk.LEFT, padx=5)

    def update_coordinates(self):
        try:
            self.x1 = int(self.x1_entry.get())
            self.y1 = int(self.y1_entry.get())
            self.x2 = int(self.x2_entry.get())
            self.y2 = int(self.y2_entry.get())
        except ValueError:
            pass

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        self.pause_button.config(text="Продолжить" if self.is_paused else "Пауза")

    def update_speed(self, value):
        try:
            speed = float(value)
            self.rotation_speed = speed
            self.speed_label.config(text=f"Скорость: {speed:.1f}")
        except ValueError:
            pass

    def take_screenshot(self):
        screenshot = ImageGrab.grab()
        filename = f"screenshot_{int(time.time())}.png"
        screenshot.save(filename)
        print(f"Скриншот сохранен как {filename}")

    def animate(self):
        if not self.is_paused:
            self.rotation_angle += self.rotation_speed * 0.1
            self.point_position += self.point_speed * 0.1
            if self.point_position > 1:
                self.point_position = 0
            self.draw_line()
        self.root_window.after(16, self.animate)

    def draw_line(self):
        self.canvas.delete("all")
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        length = math.sqrt(dx * dx + dy * dy)
        angle = math.atan2(dy, dx)
        new_angle = angle + self.rotation_angle
        half_length = length / 2
        x1_new = center_x - half_length * math.cos(new_angle)
        y1_new = center_y - half_length * math.sin(new_angle)
        x2_new = center_x + half_length * math.cos(new_angle)
        y2_new = center_y + half_length * math.sin(new_angle)
        self.canvas.create_line(x1_new, y1_new, x2_new, y2_new, width=2, fill="blue")
        self.canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = RotatingLineApp(root)
    root.mainloop()
