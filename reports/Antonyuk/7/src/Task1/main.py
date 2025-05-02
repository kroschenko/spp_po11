import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QSpinBox, QDoubleSpinBox,
                            QGroupBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen
from geometry import Point, Rectangle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize all attributes
        self.rect_x = None
        self.rect_y = None
        self.rect_width = None
        self.rect_height = None
        self.point_count = None
        self.rectangle = None
        self.points = []
        self.canvas = None
        self.timer = None
        self.generate_btn = None
        self.screenshot_btn = None

        self._setup_window()
        self._create_layout()
        self._setup_timer()

    def _setup_window(self):
        """Configure main window settings"""
        self.setWindowTitle("Точки и прямоугольник")
        self.setGeometry(100, 100, 800, 600)

    def _create_layout(self):
        """Create and arrange UI components"""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        layout.addWidget(self._create_control_panel())
        self.canvas = Canvas()
        layout.addWidget(self.canvas)

        self.rectangle = Rectangle(0, 0, 100, 100)
        self.generate_points()

    def _create_control_panel(self):
        """Create the control panel"""
        panel = QGroupBox("Управление")
        layout = QVBoxLayout()
        panel.setLayout(layout)

        layout.addWidget(self._create_rectangle_settings())
        layout.addWidget(self._create_point_settings())
        layout.addWidget(self._create_buttons())

        return panel

    def _create_rectangle_settings(self):
        """Create rectangle configuration controls"""
        group = QGroupBox("Прямоугольник")
        vbox = QVBoxLayout()

        controls = [
            ("X:", -100, 100, 0, self._make_spinbox),
            ("Y:", -100, 100, 0, self._make_spinbox),
            ("Ширина:", 1, 200, 100, self._make_spinbox),
            ("Высота:", 1, 200, 100, self._make_spinbox)
        ]

        for label, min_val, max_val, default, factory in controls:
            vbox.addWidget(QLabel(label))
            spinner = factory(min_val, max_val, default)
            vbox.addWidget(spinner)
            setattr(self, f"rect_{label.strip(':').lower()}", spinner)

        group.setLayout(vbox)
        return group

    def _make_spinbox(self, min_val, max_val, default):
        """Helper to create spinboxes"""
        box = QDoubleSpinBox()
        box.setRange(min_val, max_val)
        box.setValue(default)
        return box

    def _create_point_settings(self):
        """Create point configuration controls"""
        group = QWidget()
        vbox = QVBoxLayout()

        self.point_count = QSpinBox()
        self.point_count.setRange(1, 100)
        self.point_count.setValue(10)

        vbox.addWidget(QLabel("Количество точек:"))
        vbox.addWidget(self.point_count)
        group.setLayout(vbox)

        return group

    def _create_buttons(self):
        """Create action buttons"""
        group = QWidget()
        vbox = QVBoxLayout()

        self.generate_btn = self._make_button(
            "Сгенерировать точки", self.generate_points)
        self.screenshot_btn = self._make_button(
            "Сделать скриншот", self.take_screenshot)

        vbox.addWidget(self.generate_btn)
        vbox.addWidget(self.screenshot_btn)
        group.setLayout(vbox)

        return group

    def _make_button(self, text, handler):
        """Helper to create buttons"""
        btn = QPushButton(text)
        btn.clicked.connect(handler)
        return btn

    def _setup_timer(self):
        """Configure update timer"""
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_display)
        self.timer.start(16)  # ~60 FPS

    def generate_points(self):
        """Generate random points"""
        self.points = [
            Point(random.uniform(-200, 200), random.uniform(-200, 200))
            for _ in range(self.point_count.value())
        ]
        self._update_display()

    def take_screenshot(self):
        """Save canvas screenshot"""
        self.canvas.grab().save("screenshot.png")

    def _update_display(self):
        """Update the displayed elements"""
        self.rectangle = Rectangle(
            self.rect_x.value(),
            self.rect_y.value(),
            self.rect_width.value(),
            self.rect_height.value()
        )
        self.canvas.set_data(self.rectangle, self.points)
        self.canvas.update()


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.rectangle = None
        self.points = []
        self.setMinimumSize(400, 400)

    def set_data(self, rectangle, points):
        """Set data to be drawn"""
        self.rectangle = rectangle
        self.points = points

    def paintEvent(self, event=None):
        """Handle paint events"""
        if event:
            event.accept()

        if not self.rectangle or not self.points:
            return

        painter = QPainter(self)
        self._draw_scene(painter)

    def _draw_scene(self, painter):
        """Draw all scene elements"""
        painter.setRenderHint(QPainter.Antialiasing)
        self._setup_coordinate_system(painter)
        self._draw_axes(painter)
        self._draw_rectangle(painter)
        self._draw_points(painter)

    def _setup_coordinate_system(self, painter):
        """Set up scaling and translation"""
        width, height = self.width(), self.height()
        scale = min(width, height) / 400
        painter.translate(width / 2, height / 2)
        painter.scale(scale, scale)

    def _draw_axes(self, painter):
        """Draw coordinate axes"""
        painter.setPen(QPen(Qt.gray, 1))
        painter.drawLine(-200, 0, 200, 0)
        painter.drawLine(0, -200, 0, 200)

    def _draw_rectangle(self, painter):
        """Draw the rectangle"""
        painter.setPen(QPen(Qt.blue, 2))
        rect = self.rectangle
        painter.drawRect(
            int(rect.x - rect.width / 2),
            int(rect.y - rect.height / 2),
            int(rect.width),
            int(rect.height)
        )

    def _draw_points(self, painter):
        """Draw all points"""
        for i, point in enumerate(self.points):
            color = Qt.green if point.is_inside_rectangle(self.rectangle) else Qt.red
            painter.setPen(QPen(color, 2))
            painter.setBrush(color)
            painter.drawEllipse(int(point.x) - 5, int(point.y) - 5, 10, 10)

            painter.setPen(QPen(Qt.black, 1))
            painter.drawText(int(point.x) + 10, int(point.y) + 5, f"P{i + 1}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
