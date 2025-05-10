"""Module for generating and visualizing Minkowski Island fractals using Tkinter and Turtle."""

import colorsys
import math
import tkinter as tk
import turtle
from tkinter import ttk


class Point:
    """Represents a 2D point for Minkowski Island fractals."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        """Return point as (x, y) tuple for Turtle."""
        return (self.x, self.y)

    def scale(self, factor):
        """Return a scaled Point."""
        return Point(self.x * factor, self.y * factor)


class MinkowskiIslandApp:
    """Application for rendering Minkowski Island fractals."""

    def __init__(self, root):  # pylint: disable=redefined-outer-name
        self.root = root
        self.root.title("Minkowski Island")
        self.entries = {}
        self.turtle = None
        self.turtle_screen = None
        self.selected_color = tk.StringVar(value="gray")
        self.color_indicator = None
        self.setup_gui()
        self.root.bind("<Configure>", self.on_resize)

    def setup_gui(self):
        """Set up GUI elements."""
        control_frame = ttk.Frame(self.root)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        for label, default in [("Level:", "3"), ("Size:", "500")]:
            ttk.Label(control_frame, text=label).pack(side=tk.LEFT, padx=5)
            entry = ttk.Entry(control_frame, width=6)
            entry.insert(0, default)
            entry.pack(side=tk.LEFT, padx=5)
            self.entries[label] = entry

        ttk.Label(control_frame, text="Color:").pack(side=tk.LEFT, padx=5)
        color_canvas = tk.Canvas(control_frame, width=100, height=20, highlightthickness=1)
        color_canvas.pack(side=tk.LEFT, padx=5)
        self.draw_color_bar(color_canvas)
        color_canvas.bind("<Button-1>", self.pick_color)

        build_button = ttk.Button(control_frame, text="Build", command=self.generate_fractal)
        build_button.pack(side=tk.LEFT, padx=5)

        plot_frame = ttk.Frame(self.root)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        canvas = tk.Canvas(plot_frame, bg="light gray")
        canvas.pack(fill=tk.BOTH, expand=True)
        self.turtle_screen = turtle.TurtleScreen(canvas)
        self.turtle_screen.tracer(0, 0)
        self.turtle = turtle.RawTurtle(self.turtle_screen)
        self.turtle.speed(0)
        self.turtle.hideturtle()

        self.generate_fractal()

    def draw_color_bar(self, canvas):
        """Draw a simplified color bar with a selection indicator."""
        width, height = 100, 20
        for x in range(width):
            hue = x / width
            rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            color = f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"
            canvas.create_rectangle(x, 0, x + 1, height, fill=color, outline=color)

        self.color_indicator = canvas.create_oval(5, 5, 15, 15, outline="black", width=2, fill="")

    def pick_color(self, event):
        """Select color from the bar and update indicator position."""
        x = event.x
        width = 100
        if 0 <= x < width:
            hue = x / width
            rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            color = f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"
            self.selected_color.set(color)
            canvas = event.widget
            canvas.coords(self.color_indicator, x - 5, 5, x + 5, 15)

    def compute_minkowski_points(self, start, end):
        """Compute points for a Minkowski curve segment."""
        dx, dy = end.x - start.x, end.y - start.y
        dist = math.sqrt(dx**2 + dy**2)
        direction = math.atan2(dy, dx)
        cos_dir, sin_dir = math.cos(direction), math.sin(direction)
        cos_90, sin_90 = math.cos(direction + math.pi / 2), math.sin(direction + math.pi / 2)
        cos_neg90, sin_neg90 = math.cos(direction - math.pi / 2), math.sin(direction - math.pi / 2)

        points = []
        points.append(Point(start.x + dist / 4 * cos_dir, start.y + dist / 4 * sin_dir))
        points.append(Point(points[0].x + dist / 4 * cos_90, points[0].y + dist / 4 * sin_90))
        points.append(Point(points[1].x + dist / 4 * cos_dir, points[1].y + dist / 4 * sin_dir))
        points.append(Point(points[2].x + dist / 4 * cos_neg90, points[2].y + dist / 4 * sin_neg90))
        points.append(Point(points[3].x + dist / 4 * cos_neg90, points[3].y + dist / 4 * sin_neg90))
        points.append(Point(points[4].x + dist / 4 * cos_dir, points[4].y + dist / 4 * sin_dir))
        points.append(Point(start.x + 3 * dist / 4 * cos_dir, start.y + 3 * dist / 4 * sin_dir))

        return points

    def minkowski_curve(self, start, end, n):
        """Draw Minkowski curve recursively."""
        if n == 0:
            self.turtle.goto(*end.to_tuple())
            return
        points = self.compute_minkowski_points(start, end)
        self.minkowski_curve(start, points[0], n - 1)
        for i in range(len(points) - 1):
            self.minkowski_curve(points[i], points[i + 1], n - 1)
        self.minkowski_curve(points[-1], end, n - 1)

    def draw_minkowski_island(self, size, n, fill_color):
        """Draw the Minkowski Island."""
        self.turtle.clear()
        self.turtle.up()
        self.turtle.goto(-size / 2, -size / 2)
        self.turtle.down()
        self.turtle.fillcolor(fill_color)
        self.turtle.begin_fill()

        corners = [
            Point(-size / 2, -size / 2),
            Point(-size / 2, size / 2),
            Point(size / 2, size / 2),
            Point(size / 2, -size / 2),
        ]
        for i in range(4):
            self.minkowski_curve(corners[i], corners[(i + 1) % 4], n)

        self.turtle.end_fill()
        self.turtle_screen.update()

    def generate_fractal(self):
        """Generate fractal based on user input."""
        try:
            n = int(self.entries["Level:"].get())
            size = float(self.entries["Size:"].get())
            if n < 0 or size <= 0:
                print("Level must be non-negative and size must be positive.")
                return
        except ValueError:
            print("Invalid input parameters.")
            return

        canvas_size = min(self.turtle_screen.canvwidth, self.turtle_screen.canvheight)
        scale = canvas_size / 600
        self.draw_minkowski_island(size * scale, n, self.selected_color.get())

    def on_resize(self, event):
        """Redraw fractal on window resize."""
        if event.widget == self.root and self.turtle_screen.canvwidth > 1:
            self.generate_fractal()


if __name__ == "__main__":
    root = tk.Tk()
    app = MinkowskiIslandApp(root)
    root.mainloop()
