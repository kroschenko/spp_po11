import sys
import math
from dataclasses import dataclass
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QSpinBox,
                             QColorDialog, QDoubleSpinBox)
from PyQt5.QtGui import QPainter, QColor, QPen


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    end: Point


@dataclass
class DrawingContext:
    painter: QPainter
    color: QColor
    depth: int


class PythagorasTreeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.depth = 5
        self.angle = math.pi / 4  # 45 degrees
        self.ratio = 0.7
        self.color1 = QColor(139, 69, 19)  # Brown
        self.color2 = QColor(34, 139, 34)  # Green
        self.bg_color = QColor(240, 248, 255)  # AliceBlue

    def set_depth(self, depth):
        self.depth = depth
        self.update()

    def set_angle(self, angle):
        self.angle = math.radians(angle)
        self.update()

    def set_ratio(self, ratio):
        self.ratio = ratio
        self.update()

    def set_color1(self, color):
        self.color1 = color
        self.update()

    def set_color2(self, color):
        self.color2 = color
        self.update()

    def set_bg_color(self, color):
        self.bg_color = color
        self.update()

    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), self.bg_color)

        width = self.width()
        height = self.height()
        start_point = Point(width // 2, height - 50)
        length = height // 3

        self.draw_tree(painter=painter, start_point=start_point, length=length, angle=-math.pi / 2, depth=self.depth)

    def draw_tree(self, painter, start_point, length, angle, depth):
        if depth == 0:
            return

        end_point = Point(
            start_point.x + int(math.cos(angle) * length),
            start_point.y + int(math.sin(angle) * length)
        )

        color = self.get_color_for_depth(depth=depth)
        line = Line(start=start_point, end=end_point)
        context = DrawingContext(painter=painter, color=color, depth=depth)

        self.draw_branch(line=line, context=context)

        if depth > 1:
            new_length = length * self.ratio
            self.draw_tree(painter=painter, start_point=end_point, length=new_length, angle=angle - self.angle,
                           depth=depth - 1)
            self.draw_tree(painter=painter, start_point=end_point, length=new_length, angle=angle + self.angle,
                           depth=depth - 1)

    def get_color_for_depth(self, depth):
        if depth == self.depth:
            return self.color1

        t = (self.depth - depth) / self.depth
        r = int(self.color1.red() * (1 - t) + self.color2.red() * t)
        g = int(self.color1.green() * (1 - t) + self.color2.green() * t)
        b = int(self.color1.blue() * (1 - t) + self.color2.blue() * t)
        return QColor(r, g, b)

    @staticmethod
    def draw_branch(line: Line, context: DrawingContext):
        pen = QPen(context.color)
        pen.setWidth(max(1, context.depth))
        context.painter.setPen(pen)
        context.painter.drawLine(line.start.x, line.start.y, line.end.x, line.end.y)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Дерево Пифагора")
        self.setGeometry(100, 100, 800, 600)

        # Initialize UI components
        self.tree_widget = None
        self.depth_spin = None
        self.angle_spin = None
        self.ratio_spin = None
        self.color1_button = None
        self.color2_button = None
        self.bg_color_button = None

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.tree_widget = PythagorasTreeWidget()
        main_layout.addWidget(self.tree_widget, 1)
        self.create_control_panel(main_layout)

    def create_control_panel(self, main_layout):
        control_layout = QHBoxLayout()
        self.create_depth_control(control_layout)
        self.create_angle_control(control_layout)
        self.create_ratio_control(control_layout)
        self.create_color_buttons(control_layout)
        main_layout.addLayout(control_layout)

    def create_depth_control(self, layout):
        depth_layout = QVBoxLayout()
        depth_layout.addWidget(QLabel("Глубина:"))
        self.depth_spin = QSpinBox()
        self.depth_spin.setRange(1, 15)
        self.depth_spin.setValue(5)
        self.depth_spin.valueChanged.connect(self.tree_widget.set_depth)
        depth_layout.addWidget(self.depth_spin)
        layout.addLayout(depth_layout)

    def create_angle_control(self, layout):
        angle_layout = QVBoxLayout()
        angle_layout.addWidget(QLabel("Угол (град):"))
        self.angle_spin = QSpinBox()
        self.angle_spin.setRange(0, 90)
        self.angle_spin.setValue(45)
        self.angle_spin.valueChanged.connect(self.tree_widget.set_angle)
        angle_layout.addWidget(self.angle_spin)
        layout.addLayout(angle_layout)

    def create_ratio_control(self, layout):
        ratio_layout = QVBoxLayout()
        ratio_layout.addWidget(QLabel("Коэффициент:"))
        self.ratio_spin = QDoubleSpinBox()
        self.ratio_spin.setRange(0.1, 0.9)
        self.ratio_spin.setSingleStep(0.05)
        self.ratio_spin.setValue(0.7)
        self.ratio_spin.valueChanged.connect(self.tree_widget.set_ratio)
        ratio_layout.addWidget(self.ratio_spin)
        layout.addLayout(ratio_layout)

    def create_color_buttons(self, layout):
        self.color1_button = QPushButton("Цвет ствола")
        self.color1_button.clicked.connect(lambda: self.choose_color(self.tree_widget.set_color1))
        layout.addWidget(self.color1_button)

        self.color2_button = QPushButton("Цвет листьев")
        self.color2_button.clicked.connect(lambda: self.choose_color(self.tree_widget.set_color2))
        layout.addWidget(self.color2_button)

        self.bg_color_button = QPushButton("Цвет фона")
        self.bg_color_button.clicked.connect(lambda: self.choose_color(self.tree_widget.set_bg_color))
        layout.addWidget(self.bg_color_button)

    @staticmethod
    def choose_color(setter):
        color = QColorDialog.getColor()
        if color.isValid():
            setter(color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
