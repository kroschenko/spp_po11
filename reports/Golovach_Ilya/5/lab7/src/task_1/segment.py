import sys
import math
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QSlider, QPushButton, QSpinBox,
                             QColorDialog, QFileDialog)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen, QImage


class RotatingLineWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.angle = 0
        self.line_length = 150
        self.rotation_speed = 1
        self.base_point = None
        self.color = QColor(255, 0, 0)  # Красный по умолчанию
        self.is_rotating = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_rotation)

    def set_line_length(self, length):
        self.line_length = length
        self.update()

    def set_rotation_speed(self, speed):
        self.rotation_speed = speed

    def set_color(self, color):
        self.color = color
        self.update()

    def start_rotation(self):
        self.is_rotating = True
        self.timer.start(20)  # Обновление каждые 20 мс

    def stop_rotation(self):
        self.is_rotating = False
        self.timer.stop()

    def toggle_rotation(self):
        if self.is_rotating:
            self.stop_rotation()
        else:
            self.start_rotation()

    def update_rotation(self):
        self.angle = (self.angle + self.rotation_speed) % 360
        # Изменение цвета в зависимости от угла
        hue = int((self.angle / 360) * 255)
        self.color.setHsv(hue, 255, 255)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()
        self.base_point = (width // 2, height // 2)

        # Рассчитываем конечную точку отрезка
        end_x = self.base_point[0] + self.line_length * math.cos(math.radians(self.angle))
        end_y = self.base_point[1] + self.line_length * math.sin(math.radians(self.angle))

        # Рисуем отрезок
        pen = QPen(self.color, 3)
        painter.setPen(pen)
        painter.drawLine(self.base_point[0], self.base_point[1], int(end_x), int(end_y))

        # Рисуем базовую точку (центр вращения)
        painter.setPen(QPen(Qt.black, 5))
        painter.drawPoint(self.base_point[0], self.base_point[1])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вращающийся отрезок")
        self.setGeometry(100, 100, 600, 500)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.line_widget = RotatingLineWidget()
        main_layout.addWidget(self.line_widget, 1)

        self.create_control_panel(main_layout)
        self.create_parameters_panel(main_layout)

    def create_control_panel(self, main_layout):
        control_layout = QHBoxLayout()

        self.start_button = QPushButton("Старт/Стоп")
        self.start_button.clicked.connect(self.line_widget.toggle_rotation)
        control_layout.addWidget(self.start_button)

        self.color_button = QPushButton("Выбрать цвет")
        self.color_button.clicked.connect(self.choose_color)
        control_layout.addWidget(self.color_button)

        self.screenshot_button = QPushButton("Сделать скриншот")
        self.screenshot_button.clicked.connect(self.take_screenshot)
        control_layout.addWidget(self.screenshot_button)

        main_layout.addLayout(control_layout)

    def create_parameters_panel(self, main_layout):
        params_layout = QHBoxLayout()

        length_layout = QVBoxLayout()
        length_layout.addWidget(QLabel("Длина отрезка:"))
        self.length_spin = QSpinBox()
        self.length_spin.setRange(50, 300)
        self.length_spin.setValue(150)
        self.length_spin.valueChanged.connect(self.line_widget.set_line_length)
        length_layout.addWidget(self.length_spin)
        params_layout.addLayout(length_layout)

        speed_layout = QVBoxLayout()
        speed_layout.addWidget(QLabel("Скорость вращения:"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 20)
        self.speed_slider.setValue(5)
        self.speed_slider.valueChanged.connect(self.line_widget.set_rotation_speed)
        speed_layout.addWidget(self.speed_slider)
        params_layout.addLayout(speed_layout)

        main_layout.addLayout(params_layout)

    def choose_color(self):
        color = QColorDialog.getColor(self.line_widget.color, self, "Выберите цвет отрезка")
        if color.isValid():
            self.line_widget.set_color(color)

    def take_screenshot(self):
        image = QImage(self.line_widget.size(), QImage.Format_ARGB32)
        painter = QPainter(image)
        self.line_widget.render(painter)
        painter.end()

        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить скриншот", "",
                                                   "PNG Images (*.png);;JPEG Images (*.jpg *.jpeg)")
        if file_name:
            image.save(file_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
