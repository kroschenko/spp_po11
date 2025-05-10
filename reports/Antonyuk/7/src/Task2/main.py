import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QPushButton, QLabel, QSpinBox,
                            QDoubleSpinBox, QGroupBox, QColorDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from fractal import Point, HFractal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Инициализация всех атрибутов
        self.size = None
        self.depth = None
        self.line_width = None
        self.color_btn = None
        self.screenshot_btn = None
        self.canvas = None
        self.fractal = None
        self.line_color = QColor(Qt.black)

        # Настройка основного окна
        self.setWindowTitle("Н-фрактал")
        self.setGeometry(100, 100, 800, 600)

        # Инициализация интерфейса
        self._init_ui()

    def _init_ui(self):
        """Инициализация пользовательского интерфейса"""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QHBoxLayout(main_widget)
        layout.addWidget(self._create_control_panel())
        self.canvas = Canvas()
        layout.addWidget(self.canvas)

        self.update_fractal()

    def _create_control_panel(self):
        """Создание панели управления"""
        panel = QGroupBox("Управление")
        layout = QVBoxLayout()

        # Создание элементов управления
        self.size = self._create_spinbox_control(10, 1000, 400, "Размер:")
        self.depth = self._create_spinbox_control(1, 10, 4, "Глубина:")
        self.line_width = self._create_spinbox_control(1, 10, 1, "Толщина линий:")

        # Добавление элементов в layout
        for control in [self.size, self.depth, self.line_width]:
            layout.addLayout(control['layout'])

        # Кнопки
        self.color_btn = QPushButton("Выбрать цвет")
        self.color_btn.clicked.connect(self.choose_color)
        layout.addWidget(QLabel("Цвет линий:"))
        layout.addWidget(self.color_btn)

        self.screenshot_btn = QPushButton("Сделать скриншот")
        self.screenshot_btn.clicked.connect(self.take_screenshot)
        layout.addWidget(self.screenshot_btn)

        panel.setLayout(layout)
        return panel

    def _create_spinbox_control(self, min_val, max_val, default, label_text):
        """Создание элемента управления SpinBox"""
        spinbox = QDoubleSpinBox() if isinstance(default, float) else QSpinBox()
        spinbox.setRange(min_val, max_val)
        spinbox.setValue(default)
        spinbox.valueChanged.connect(self.update_fractal)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(label_text))
        layout.addWidget(spinbox)
        return {'spinbox': spinbox, 'layout': layout}

    def choose_color(self):
        """Выбор цвета линий"""
        color = QColorDialog.getColor(self.line_color, self, "Выберите цвет линий")
        if color.isValid():
            self.line_color = color
            self.update_fractal()

    def update_fractal(self):
        """Обновление параметров фрактала"""
        center = Point(0, 0)
        size = self.size['spinbox'].value()
        depth = self.depth['spinbox'].value()
        line_width = self.line_width['spinbox'].value()

        self.fractal = HFractal(center, size, depth)
        self.canvas.set_fractal(self.fractal, self.line_color, line_width)
        self.canvas.update()

    def take_screenshot(self):
        """Сохранение скриншота"""
        self.canvas.grab().save("fractal_screenshot.png")

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.fractal = None
        self.line_color = Qt.black
        self.line_width = 1
        self.setMinimumSize(400, 400)

    def set_fractal(self, fractal, color, width):
        """Установка параметров фрактала"""
        self.fractal = fractal
        self.line_color = color
        self.line_width = width

    def paintEvent(self, event):
        """Отрисовка фрактала"""
        del event  # Явное указание неиспользуемого параметра

        if not self.fractal:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Настройка масштабирования
        width = self.width()
        height = self.height()
        scale = min(width, height) / (self.fractal.size * 1.2)
        painter.translate(width/2, height/2)
        painter.scale(scale, scale)

        # Отрисовка линий фрактала
        painter.setPen(QPen(self.line_color, self.line_width))
        for line in self.fractal.lines:
            painter.drawLine(
                int(line[0].x), int(line[0].y),
                int(line[1].x), int(line[1].y)
            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
