import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpinBox, QDoubleSpinBox, QGroupBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen
from geometry import Point, Rectangle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Инициализация атрибутов
        self.rect_x = None
        self.rect_y = None
        self.rect_width = None
        self.rect_height = None
        self.point_count = None
        self.rectangle = None
        self.points = []
        self.canvas = None
        self.timer = None

        self._init_ui()

    def _init_ui(self):
        """Инициализация пользовательского интерфейса"""
        self.setWindowTitle("Точки и прямоугольник")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        layout.addWidget(self._create_control_panel())
        self.canvas = Canvas()
        layout.addWidget(self.canvas)

        self.rectangle = Rectangle(0, 0, 100, 100)
        self.points = []
        self.generate_points()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16)

    def _create_control_panel(self):
        """Создание панели управления"""
        control_panel = QGroupBox("Управление")
        control_layout = QVBoxLayout()

        # Группа для настроек прямоугольника
        rect_group = QGroupBox("Прямоугольник")
        rect_layout = QVBoxLayout()

        # Создаем элементы управления для прямоугольника
        self.rect_x = QDoubleSpinBox()
        self.rect_x.setRange(-100, 100)
        self.rect_x.setValue(0)
        rect_layout.addWidget(QLabel("X:"))
        rect_layout.addWidget(self.rect_x)

        self.rect_y = QDoubleSpinBox()
        self.rect_y.setRange(-100, 100)
        self.rect_y.setValue(0)
        rect_layout.addWidget(QLabel("Y:"))
        rect_layout.addWidget(self.rect_y)

        self.rect_width = QDoubleSpinBox()
        self.rect_width.setRange(1, 200)
        self.rect_width.setValue(100)
        rect_layout.addWidget(QLabel("Ширина:"))
        rect_layout.addWidget(self.rect_width)

        self.rect_height = QDoubleSpinBox()
        self.rect_height.setRange(1, 200)
        self.rect_height.setValue(100)
        rect_layout.addWidget(QLabel("Высота:"))
        rect_layout.addWidget(self.rect_height)

        rect_group.setLayout(rect_layout)
        control_layout.addWidget(rect_group)

        # Элементы управления для точек
        self.point_count = QSpinBox()
        self.point_count.setRange(1, 100)
        self.point_count.setValue(10)
        control_layout.addWidget(QLabel("Количество точек:"))
        control_layout.addWidget(self.point_count)

        # Кнопки
        self.generate_btn = QPushButton("Сгенерировать точки")
        self.generate_btn.clicked.connect(self.generate_points)
        control_layout.addWidget(self.generate_btn)

        self.screenshot_btn = QPushButton("Сделать скриншот")
        self.screenshot_btn.clicked.connect(self.take_screenshot)
        control_layout.addWidget(self.screenshot_btn)

        control_panel.setLayout(control_layout)
        return control_panel

    def generate_points(self):
        """Генерация случайных точек"""
        self.points = [
            Point(random.uniform(-200, 200), random.uniform(-200, 200))
            for _ in range(self.point_count.value())
        ]
        self.canvas.update()

    def update(self):
        """Обновление прямоугольника и точек"""
        self.rectangle = Rectangle(
            self.rect_x.value(),
            self.rect_y.value(),
            self.rect_width.value(),
            self.rect_height.value()
        )
        self.canvas.set_data(self.rectangle, self.points)
        self.canvas.update()

    def take_screenshot(self):
        """Сохранение скриншота"""
        screenshot = self.canvas.grab()
        screenshot.save("screenshot.png")


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.rectangle = None
        self.points = []
        self.setMinimumSize(400, 400)

    def set_data(self, rectangle, points):
        """Установка данных для отрисовки"""
        self.rectangle = rectangle
        self.points = points

    def paintEvent(self, event):
        """Отрисовка элементов на холсте"""
        if not self.rectangle or not self.points:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()
        scale = min(width, height) / 400
        painter.translate(width / 2, height / 2)
        painter.scale(scale, scale)

        painter.setPen(QPen(Qt.gray, 1))
        painter.drawLine(-200, 0, 200, 0)
        painter.drawLine(0, -200, 0, 200)

        painter.setPen(QPen(Qt.blue, 2))
        painter.drawRect(
            int(self.rectangle.x - self.rectangle.width / 2),
            int(self.rectangle.y - self.rectangle.height / 2),
            int(self.rectangle.width),
            int(self.rectangle.height)
        )

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
