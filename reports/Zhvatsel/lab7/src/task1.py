"""Module for visualizing points relative to a line using Matplotlib and Tkinter."""

import random
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Point:
    """Represents a 2D point for point-line visualization."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        """Return the x-coordinate of the point."""
        return self.x

    def get_y(self):
        """Return the y-coordinate of the point."""
        return self.y

    def is_within_bounds(self):
        """Check if the point is within the visualization range [-10, 10]."""
        return -10 <= self.x <= 10 and -10 <= self.y <= 10

    def __str__(self):
        """Return a string representation of the point."""
        return f"VisPoint({self.x}, {self.y})"


class Line:
    """Represents a line segment between two points."""

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def side(self, point):
        """Determine which side of the line a point lies on using cross product.

        Args:
            point (Point): The point to check.

        Returns:
            float: Positive if left, negative if right, zero if on the line.
        """
        ax = self.point_b.x - self.point_a.x
        ay = self.point_b.y - self.point_a.y
        bx = point.x - self.point_a.x
        by = point.y - self.point_a.y
        return ax * by - ay * bx

    def get_point_a(self):
        """Return the first point of the line."""
        return self.point_a

    def get_point_b(self):
        """Return the second point of the line."""
        return self.point_b


class VisualizationApp:
    """Application for visualizing points and a line segment."""

    def __init__(self, root):
        """Initialize the visualization application.

        Args:
            root (tk.Tk): The Tkinter root window.
        """
        self.root = root
        self.root.title("Point and Line Visualization")
        self.points = []
        self.line = None
        self.plot_config = {
            "fig": plt.figure(),
            "ax": None,
            "canvas": None,
            "plot_frame": None,
        }
        self.entries = {
            "num_points": None,
            "ax": None,
            "ay": None,
            "bx": None,
            "by": None,
        }

        self.create_gui()
        self.plot_config["ax"] = self.plot_config["fig"].add_subplot(111)
        self.plot_config["canvas"] = FigureCanvasTkAgg(
            self.plot_config["fig"],
            master=self.plot_config["plot_frame"],
        )
        self.plot_config["canvas"].get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_gui(self):
        """Create the GUI elements for the application."""
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10, padx=10, fill=tk.X)

        ttk.Label(control_frame, text="Number of Points:").grid(row=0, column=0, padx=5)
        self.entries["num_points"] = ttk.Entry(control_frame, width=10)
        self.entries["num_points"].grid(row=0, column=1, padx=5)
        self.entries["num_points"].insert(0, "20")

        ttk.Label(control_frame, text="Point A (x, y):").grid(row=1, column=0, padx=5)
        self.entries["ax"] = ttk.Entry(control_frame, width=10)
        self.entries["ax"].grid(row=1, column=1, padx=5)
        self.entries["ax"].insert(0, "-5")
        self.entries["ay"] = ttk.Entry(control_frame, width=10)
        self.entries["ay"].grid(row=1, column=2, padx=5)
        self.entries["ay"].insert(0, "-5")

        ttk.Label(control_frame, text="Point B (x, y):").grid(row=2, column=0, padx=5)
        self.entries["bx"] = ttk.Entry(control_frame, width=10)
        self.entries["bx"].grid(row=2, column=1, padx=5)
        self.entries["bx"].insert(0, "5")
        self.entries["by"] = ttk.Entry(control_frame, width=10)
        self.entries["by"].grid(row=2, column=2, padx=5)
        self.entries["by"].insert(0, "5")

        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)

        ttk.Button(button_frame, text="Start", command=self.start_visualization).pack(
            side=tk.LEFT,
            padx=5,
        )
        ttk.Button(button_frame, text="Clear", command=self.clear_visualization).pack(
            side=tk.LEFT,
            padx=5,
        )
        ttk.Button(button_frame, text="Screenshot", command=self.take_screenshot).pack(
            side=tk.LEFT,
            padx=5,
        )

        self.plot_config["plot_frame"] = ttk.Frame(self.root)
        self.plot_config["plot_frame"].pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def generate_points(self, n):
        """Generate n random points within the range [-10, 10].

        Args:
            n (int): Number of points to generate.
        """
        self.points = [Point(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(n)]

    def start_visualization(self):
        """Start the visualization based on user input."""
        try:
            n = int(self.entries["num_points"].get())
            ax = float(self.entries["ax"].get())
            ay = float(self.entries["ay"].get())
            bx = float(self.entries["bx"].get())
            by = float(self.entries["by"].get())

            if n <= 0:
                messagebox.showerror("Error", "Number of points must be positive")
                return

            if ax == bx and ay == by:
                messagebox.showerror("Error", "Points A and B must be different")
                return

            point_a = Point(ax, ay)
            point_b = Point(bx, by)
            if not (point_a.is_within_bounds() and point_b.is_within_bounds()):
                messagebox.showerror(
                    "Error",
                    "Coordinates of points A and B must be between -10 and 10",
                )
                return

            self.line = Line(point_a, point_b)
            self.generate_points(n)
            self.draw_visualization()

        except ValueError:
            messagebox.showerror("Error", "Invalid input values")

    def clear_visualization(self):
        """Clear the current visualization."""
        self.plot_config["ax"].clear()
        self.plot_config["ax"].set_xlim(-12, 12)
        self.plot_config["ax"].set_ylim(-12, 12)
        self.plot_config["ax"].grid(True)
        self.plot_config["canvas"].draw()

    def draw_visualization(self):
        """Draw the points and line segment on the plot."""
        self.plot_config["ax"].clear()

        left_points = []
        right_points = []

        for point in self.points:
            side_value = self.line.side(point)
            if side_value > 0:
                left_points.append(point)
            elif side_value < 0:
                right_points.append(point)

        if left_points:
            x, y = zip(*[(p.x, p.y) for p in left_points])
            self.plot_config["ax"].scatter(x, y, color="blue", label="Left side")

        if right_points:
            x, y = zip(*[(p.x, p.y) for p in right_points])
            self.plot_config["ax"].scatter(x, y, color="red", label="Right side")

        self.plot_config["ax"].plot(
            [self.line.point_a.x, self.line.point_b.x],
            [self.line.point_a.y, self.line.point_b.y],
            "g-",
            label="Line",
        )

        self.plot_config["ax"].set_xlim(-12, 12)
        self.plot_config["ax"].set_ylim(-12, 12)
        self.plot_config["ax"].legend()
        self.plot_config["ax"].grid(True)
        self.plot_config["canvas"].draw()

    def take_screenshot(self):
        """Save the current plot as a screenshot."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        self.plot_config["fig"].savefig(filename)
        messagebox.showinfo("Success", f"Screenshot saved as {filename}")


def main():
    """Run the visualization application."""
    root = tk.Tk()
    VisualizationApp(root)
    root.geometry("800x600")
    root.mainloop()


if __name__ == "__main__":
    main()
