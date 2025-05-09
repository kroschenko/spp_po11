import sys
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QPushButton, QLabel, QSpinBox,
                            QComboBox)
from PyQt5.QtCore import QTimer, QPoint
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap

class CharacterAnimation(QWidget):
    def __init__(self):
        super().__init__()
        self.characters = []
        self.current_char_index = 0
        self.speed = 100  # миллисекунды
        self.is_running = False
        self.target_text = "Hello World!"
        self.corners = ['top_left', 'top_right', 'bottom_left', 'bottom_right']
        self.current_corner = 0

        # Initialize UI elements
        self.speed_spin = None
        self.text_combo = None
        self.start_button = None
        self.screenshot_button = None
        self.animation_area = None
        self.timer = None

        self.init_ui()

    def init_ui(self):
        self.setMinimumSize(800, 600)
        self.setWindowTitle('Анимация символов')

        # Create main layout and widgets
        main_layout = QVBoxLayout()
        self.animation_area = QWidget()
        self.animation_area.setMinimumSize(800, 500)

        # Create controls
        controls = self._create_controls()

        # Setup layout
        main_layout.addWidget(self.animation_area)
        main_layout.addLayout(controls)
        self.setLayout(main_layout)

        # Setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)

    def _create_controls(self):
        """Create and return the controls layout with all widgets."""
        controls_layout = QHBoxLayout()

        # Speed control
        speed_label = QLabel('Скорость (мс):')
        self.speed_spin = QSpinBox()
        self.speed_spin.setRange(50, 1000)
        self.speed_spin.setValue(self.speed)
        self.speed_spin.valueChanged.connect(self.update_speed)

        # Text input
        text_label = QLabel('Текст:')
        self.text_combo = QComboBox()
        self.text_combo.setEditable(True)
        self.text_combo.addItems(['Hello World!', 'Python', 'Animation'])
        self.text_combo.currentTextChanged.connect(self.update_text)

        # Control buttons
        self.start_button = QPushButton('Старт')
        self.start_button.clicked.connect(self.toggle_animation)

        self.screenshot_button = QPushButton('Сделать скриншот')
        self.screenshot_button.clicked.connect(self.take_screenshot)

        # Add widgets to layout
        controls_layout.addWidget(speed_label)
        controls_layout.addWidget(self.speed_spin)
        controls_layout.addWidget(text_label)
        controls_layout.addWidget(self.text_combo)
        controls_layout.addWidget(self.start_button)
        controls_layout.addWidget(self.screenshot_button)

        return controls_layout

    def update_speed(self, value):
        self.speed = value
        if self.is_running:
            self.timer.setInterval(self.speed)

    def update_text(self, text):
        self.target_text = text
        self.reset_animation()

    def toggle_animation(self):
        if self.is_running:
            self.timer.stop()
            self.start_button.setText('Старт')
        else:
            self.timer.start(self.speed)
            self.start_button.setText('Стоп')
        self.is_running = not self.is_running

    def reset_animation(self):
        self.characters = []
        self.current_char_index = 0
        self.current_corner = 0
        self.update()

    def get_corner_position(self, corner):
        margin = 50
        if corner == 'top_left':
            return QPoint(margin, margin)
        if corner == 'top_right':
            return QPoint(self.width() - margin, margin)
        if corner == 'bottom_left':
            return QPoint(margin, self.height() - margin)
        return QPoint(self.width() - margin, self.height() - margin)

    def update_animation(self):
        if self.current_char_index < len(self.target_text):
            corner = self.corners[self.current_corner]
            start_pos = self.get_corner_position(corner)
            target_x = 100 + len(self.characters) * 30  # Располагаем символы горизонтально
            target_y = self.height() // 2

            self.characters.append({
                'char': self.target_text[self.current_char_index],
                'pos': start_pos,
                'target': QPoint(target_x, target_y),
                'progress': 0
            })

            self.current_char_index += 1
            self.current_corner = (self.current_corner + 1) % len(self.corners)
        else:
            self.reset_animation()

        self.update()

    def paintEvent(self, _):
        """Handle the paint event for the widget."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Рисуем фон
        painter.fillRect(self.rect(), QColor(240, 240, 240))

        # Рисуем символы
        font = QFont('Arial', 24)
        painter.setFont(font)

        for char_data in self.characters:
            progress = char_data['progress']
            current_x = char_data['pos'].x() + (char_data['target'].x() - char_data['pos'].x()) * progress
            current_y = char_data['pos'].y() + (char_data['target'].y() - char_data['pos'].y()) * progress

            painter.drawText(int(current_x), int(current_y), char_data['char'])
            char_data['progress'] = min(1.0, char_data['progress'] + 0.1)

    def take_screenshot(self):
        screenshot = QPixmap(self.size())
        self.render(screenshot)

        # Создаем имя файла с временной меткой
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'screenshot_{timestamp}.png'

        # Сохраняем скриншот
        screenshot.save(filename)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.animation = CharacterAnimation()
        self.setCentralWidget(self.animation)
        self.setWindowTitle('Анимация символов')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
