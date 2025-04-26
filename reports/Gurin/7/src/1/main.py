import random
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QFont, QPainter
from PyQt5.QtWidgets import (
    QApplication,
    QColorDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class MovingText:
    def __init__(self, text, width, height, color):
        self.text = text
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.color = color
        self.dx = random.choice([-3, -2, -1, 1, 2, 3])
        self.dy = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self, width, height):
        self.x = (self.x + self.dx) % width
        self.y = (self.y + self.dy) % height


class TextScene(QWidget):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_scene)
        self.speed = 30

    def start(self):
        self.timer.start(1000 // self.speed)

    def stop(self):
        self.timer.stop()

    def add_text(self, text, color):
        self.texts.append(MovingText(text, self.width(), self.height(), color))

    def update_scene(self):
        for text in self.texts:
            text.update(self.width(), self.height())
        self.update()

    def paintEvent(self, event):
        print(event) #to fix W0613: Unused argument 'event' (unused-argument)
        painter = QPainter(self)
        painter.setFont(QFont("Arial", 12))

        for text in self.texts:
            painter.setPen(text.color)
            painter.drawText(text.x, text.y, text.text)

    def resizeEvent(self, event):
        print(event) #to fix W0613: Unused argument 'event' (unused-argument)
        for text in self.texts:
            text.x = text.x % self.width()
            text.y = text.y % self.height()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.scene = TextScene()
        self.text_input = QLineEdit()
        self.color_btn = QPushButton("Выбрать цвет")
        self.add_btn = QPushButton("Добавить текст")
        self.pause_btn = QPushButton("Пауза")
        self.screenshot_btn = QPushButton("Скриншот")
        self.speed_slider = QSlider(Qt.Horizontal)

        self.init_ui()

        self.add_btn.clicked.connect(self.add_text)
        self.pause_btn.clicked.connect(self.toggle_pause)
        self.screenshot_btn.clicked.connect(self.save_screenshot)
        self.color_btn.clicked.connect(self.choose_color)
        self.speed_slider.valueChanged.connect(self.change_speed)

        self.current_color = QColor(0, 0, 0)  # Черный по умолчанию
        self.speed_slider.setRange(1, 60)
        self.speed_slider.setValue(30)

    def init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        control_panel = QHBoxLayout()
        control_panel.addWidget(QLabel("Текст:"))
        control_panel.addWidget(self.text_input)
        control_panel.addWidget(self.color_btn)
        control_panel.addWidget(self.add_btn)
        control_panel.addWidget(self.pause_btn)
        control_panel.addWidget(self.screenshot_btn)
        control_panel.addWidget(QLabel("Скорость:"))
        control_panel.addWidget(self.speed_slider)

        layout.addLayout(control_panel)
        layout.addWidget(self.scene)

        central.setLayout(layout)
        self.setCentralWidget(central)
        self.setGeometry(100, 100, 800, 600)

    def add_text(self):
        text = self.text_input.text()
        if text:
            self.scene.add_text(text, self.current_color)
            self.scene.start()
            self.text_input.clear()

    def toggle_pause(self):
        if self.scene.timer.isActive():
            self.scene.stop()
            self.pause_btn.setText("Продолжить")
        else:
            self.scene.start()
            self.pause_btn.setText("Пауза")

    def save_screenshot(self):
        pixmap = self.scene.grab()
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pixmap.save(filename)
        print(f"Скриншот сохранен как {filename}")

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.current_color = color

    def change_speed(self, value):
        self.scene.speed = value
        if self.scene.timer.isActive():
            self.scene.timer.setInterval(1000 // value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
