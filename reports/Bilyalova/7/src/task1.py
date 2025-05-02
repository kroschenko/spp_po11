import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import time
import math
from PIL import ImageGrab


class RotatingQuadrilateralApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Вращающийся четырехугольник")

        # Initialize all instance attributes here
        self.width = 400
        self.height = 400
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.vertices = [(100, 100), (300, 100), (350, 300), (50, 300)]
        self.rotation_angle = 0
        self.rotation_speed = 1
        self.fill_color = "blue"
        self.outline_color = "black"
        self.is_rotating = True
        self.quadrilateral = None
        self.vertex_entries = []

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        self.control_frame = ttk.Frame(self.master)
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        self.speed_slider = None
        self.fill_color_btn = None
        self.outline_color_btn = None
        self.pause_btn = None
        self.screenshot_btn = None
        self.update_btn = None

        self.setup_ui()
        self.animate()

    def setup_ui(self):
        self.create_speed_control()
        self.create_color_controls()
        self.create_action_buttons()
        self.create_vertex_controls()

    def create_speed_control(self):
        ttk.Label(self.control_frame, text="Скорость вращения:").pack(pady=5)
        self.speed_slider = ttk.Scale(
            self.control_frame,
            from_=0,
            to=10,
            command=self.update_speed
        )
        self.speed_slider.set(self.rotation_speed)
        self.speed_slider.pack(pady=5)

    def create_color_controls(self):
        ttk.Label(self.control_frame, text="Цвет заливки:").pack(pady=5)
        self.fill_color_btn = ttk.Button(
            self.control_frame,
            text="Выбрать",
            command=self.choose_fill_color
        )
        self.fill_color_btn.pack(pady=5)

        ttk.Label(self.control_frame, text="Цвет контура:").pack(pady=5)
        self.outline_color_btn = ttk.Button(
            self.control_frame,
            text="Выбрать",
            command=self.choose_outline_color
        )
        self.outline_color_btn.pack(pady=5)

    def create_action_buttons(self):
        self.pause_btn = ttk.Button(
            self.control_frame,
            text="Пауза",
            command=self.toggle_rotation
        )
        self.pause_btn.pack(pady=10)

        self.screenshot_btn = ttk.Button(
            self.control_frame,
            text="Сделать скриншот",
            command=self.take_screenshot
        )
        self.screenshot_btn.pack(pady=10)

    def create_vertex_controls(self):
        ttk.Label(self.control_frame, text="Вершины четырехугольника:").pack(pady=5)
        for i in range(4):
            self.create_vertex_entry(i)

        self.update_btn = ttk.Button(
            self.control_frame,
            text="Обновить вершины",
            command=self.update_vertices
        )
        self.update_btn.pack(pady=10)

    def create_vertex_entry(self, index):
        frame = ttk.Frame(self.control_frame)
        frame.pack(pady=2)
        ttk.Label(frame, text=f"Вершина {index+1}:").pack(side=tk.LEFT)
        x_entry = ttk.Entry(frame, width=5)
        x_entry.pack(side=tk.LEFT)
        y_entry = ttk.Entry(frame, width=5)
        y_entry.pack(side=tk.LEFT)
        x_entry.insert(0, str(self.vertices[index][0]))
        y_entry.insert(0, str(self.vertices[index][1]))
        self.vertex_entries.append((x_entry, y_entry))

    def rotate_point(self, point, angle):
        x, y = point
        x -= self.center_x
        y -= self.center_y

        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = x * math.sin(angle) + y * math.cos(angle)

        return (new_x + self.center_x, new_y + self.center_y)

    def draw_quadrilateral(self):
        if self.quadrilateral:
            self.canvas.delete(self.quadrilateral)

        rotated_vertices = [self.rotate_point(v, self.rotation_angle) for v in self.vertices]
        self.quadrilateral = self.canvas.create_polygon(
            rotated_vertices,
            fill=self.fill_color,
            outline=self.outline_color,
            width=2
        )

    def animate(self):
        if self.is_rotating:
            self.rotation_angle += math.radians(self.rotation_speed)
            self.draw_quadrilateral()

        self.master.after(20, self.animate)

    def update_speed(self, value):
        self.rotation_speed = float(value)

    def choose_fill_color(self):
        color = colorchooser.askcolor(title="Выберите цвет заливки")[1]
        if color:
            self.fill_color = color

    def choose_outline_color(self):
        color = colorchooser.askcolor(title="Выберите цвет контура")[1]
        if color:
            self.outline_color = color

    def toggle_rotation(self):
        self.is_rotating = not self.is_rotating
        self.pause_btn.config(text="Пауза" if self.is_rotating else "Продолжить")

    def update_vertices(self):
        try:
            new_vertices = []
            for x_entry, y_entry in self.vertex_entries:
                x = int(x_entry.get())
                y = int(y_entry.get())
                new_vertices.append((x, y))

            if len(new_vertices) == 4:
                self.vertices = new_vertices
        except ValueError:
            pass

    def take_screenshot(self):
        x = self.master.winfo_rootx() + self.canvas.winfo_x()
        y = self.master.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        screenshot = ImageGrab.grab((x, y, x1, y1))

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"quadrilateral_{timestamp}.png"

        screenshot.save(filename)

        messagebox.showinfo("Скриншот сохранен", f"Скриншот сохранен как {filename}")


def main():
    root = tk.Tk()
    RotatingQuadrilateralApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
