import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer


class CircleAnimation(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Анимация окружности")
        self.setGeometry(100, 100, 600, 400)

        # Параметры окружности
        self.circle_radius = 20
        self.x = 100
        self.y = 100
        self.vx = 3
        self.vy = 3

        # Скорость таймера
        self.timer_delay = 20  # мс
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)

        # Интерфейс
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Ввод координат
        coord_layout = QHBoxLayout()
        self.x_input = QLineEdit(str(self.x))
        self.y_input = QLineEdit(str(self.y))
        coord_layout.addWidget(QLabel("X:"))
        coord_layout.addWidget(self.x_input)
        coord_layout.addWidget(QLabel("Y:"))
        coord_layout.addWidget(self.y_input)
        layout.addLayout(coord_layout)

        # Ввод скорости
        speed_layout = QHBoxLayout()
        self.vx_input = QLineEdit(str(self.vx))
        self.vy_input = QLineEdit(str(self.vy))
        speed_layout.addWidget(QLabel("Vx:"))
        speed_layout.addWidget(self.vx_input)
        speed_layout.addWidget(QLabel("Vy:"))
        speed_layout.addWidget(self.vy_input)
        layout.addLayout(speed_layout)

        # Кнопки управления
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Запустить")
        self.pause_btn = QPushButton("Пауза")
        self.screenshot_btn = QPushButton("Скриншот")

        self.start_btn.clicked.connect(self.start_animation)
        self.pause_btn.clicked.connect(self.pause_animation)
        self.screenshot_btn.clicked.connect(self.take_screenshot)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.pause_btn)
        btn_layout.addWidget(self.screenshot_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def start_animation(self):
        try:
            self.x = int(self.x_input.text())
            self.y = int(self.y_input.text())
            self.vx = int(self.vx_input.text())
            self.vy = int(self.vy_input.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректные числовые значения!")
            return

        if not self.timer.isActive():
            self.timer.start(self.timer_delay)

    def pause_animation(self):
        self.timer.stop()

    def take_screenshot(self):
        pixmap = self.grab()
        filename = f"circle_screenshot_{len(os.listdir('.'))}.png"
        pixmap.save(filename)
        QMessageBox.information(self, "Сохранено", f"Скриншот сохранен как {filename}")

    def update_position(self):
        width = self.width() - self.circle_radius * 2
        height = self.height() - self.circle_radius * 2

        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= width:
            self.vx *= -1
            self.x = max(0, min(self.x, width))

        if self.y <= 0 or self.y >= height:
            self.vy *= -1
            self.y = max(0, min(self.y, height))

        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 150, 255))
        painter.drawEllipse(self.x, self.y, self.circle_radius * 2, self.circle_radius * 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleAnimation()
    window.show()
    sys.exit(app.exec_())
