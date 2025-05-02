import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QSpinBox, QDoubleSpinBox,
    QGroupBox, QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from geometry import Point, Rectangle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        self._init_ui()

    def _init_ui(self):
        """Инициализация интерфейса"""
        self.setWindowTitle("Точки и прямоугольник")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        layout.addWidget(self._create_control_panel())
        self.canvas = Canvas()
        layout.addWidget(self.canvas)

        self.rectangle = Rectangle(0, 0, 100, 100)
        self.generate_points()

    def _create_control_panel(self):
        """Создание панели управления"""
        panel = QGroupBox("Управление")
        layout = QVBoxLayout()

        # Группа для настроек прямоугольника
        rect_group = QGroupBox("Прямоугольник")
        rect_layout = QVBoxLayout()

        # Создаем элементы управления
        self._add_spinbox(rect_layout, "X", -100, 100, 0)
        self._add_spinbox(rect_layout, "Y", -100, 100, 0)
        self._add_spinbox(rect_layout, "Ширина", 1, 200, 100)
        self._add_spinbox(rect_layout, "Высота", 1, 200, 100)

        rect_group.setLayout(rect_layout)
        layout.addWidget(rect_group)

        # Элементы управления для точек
        self.point_count = QSpinBox()
        self.point_count.setRange(1, 100)
        self.point_count.setValue(10)
        layout.addWidget(QLabel("Количество точек:"))
        layout.addWidget(self.point_count)

        # Кнопки
        self.generate_btn = QPushButton("Сгенерировать точки")
        self.generate_btn.clicked.connect(self.generate_points)
        layout.addWidget(self.generate_btn)

        self.screenshot_btn = QPushButton("Сделать скриншот")
        self.screenshot_btn.clicked.connect(self.take_screenshot)
        layout.addWidget(self.screenshot_btn)

        panel.setLayout(layout)
        return panel

    def _add_spinbox(self, layout, name, min_val, max_val, default):
        """Вспомогательный метод для добавления SpinBox"""
        spinbox = QDoubleSpinBox()
        spinbox.setRange(min_val, max_val)
        spinbox.setValue(default)
        layout.addWidget(QLabel(f"{name}:"))
        layout.addWidget(spinbox)
        setattr(self, f"rect_{name.lower()}", spinbox)

    def generate_points(self):
        """Генерация случайных точек"""
        self.points = [
            Point(random.uniform(-200, 200), random.uniform(-200, 200))
            for _ in range(self.point_count.value())
        ]
        self.update()

    def take_screenshot(self):
        """Сохранение скриншота"""
        self.canvas.grab().save("screenshot.png")

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

    def paintEvent(self, _):
        """Отрисовка элементов на холсте"""
        if not self.rectangle or not self.points:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()
        scale = min(width, height) / 400
        painter.translate(width / 2, height / 2)
        painter.scale(scale, -scale)  # Инвертируем ось Y

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
