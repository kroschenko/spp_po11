import sys
from dataclasses import dataclass

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QPushButton, QLabel, QSpinBox,
                            QColorDialog)
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor, QPen

@dataclass
class HilbertCurveParams:
    """Class to hold Hilbert curve parameters."""
    order: int
    x: int
    y: int
    xi: int
    xj: int
    yi: int
    yj: int

class HilbertCurve(QWidget):
    def __init__(self):
        super().__init__()
        self.order = 3  # Порядок кривой
        self.size = 600  # Размер области рисования
        self.line_color = QColor(0, 0, 0)  # Синий цвет по умолчанию
        self.line_width = 2

        # Initialize UI elements
        self.order_spin = None
        self.width_spin = None
        self.color_button = None
        self.drawing_area = None

        self.init_ui()

    def init_ui(self):
        self.setMinimumSize(self.size + 50, self.size + 100)
        self.setWindowTitle('Кривая Гильберта')

        # Create main layout and widgets
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        # Create drawing area
        self.drawing_area = QWidget()
        self.drawing_area.setMinimumSize(self.size, self.size)

        # Create controls
        controls = self._create_controls()

        # Setup layout
        main_layout.addWidget(self.drawing_area)
        main_layout.addStretch()
        main_layout.addLayout(controls)
        self.setLayout(main_layout)

    def _create_controls(self):
        """Create and return the controls layout with all widgets."""
        controls_layout = QHBoxLayout()
        controls_layout.setContentsMargins(10, 10, 10, 10)

        # Order control
        order_label = QLabel('Порядок:')
        self.order_spin = QSpinBox()
        self.order_spin.setRange(1, 8)
        self.order_spin.setValue(self.order)
        self.order_spin.valueChanged.connect(self.update_order)

        # Line width control
        width_label = QLabel('Толщина линии:')
        self.width_spin = QSpinBox()
        self.width_spin.setRange(1, 10)
        self.width_spin.setValue(self.line_width)
        self.width_spin.valueChanged.connect(self.update_line_width)

        # Color button
        self.color_button = QPushButton('Выбрать цвет')
        self.color_button.setMinimumWidth(120)
        self.color_button.clicked.connect(self.choose_color)

        # Add widgets to layout
        controls_layout.addWidget(order_label)
        controls_layout.addWidget(self.order_spin)
        controls_layout.addWidget(width_label)
        controls_layout.addWidget(self.width_spin)
        controls_layout.addWidget(self.color_button)

        return controls_layout

    def update_order(self, value):
        self.order = value
        self.update()

    def update_line_width(self, value):
        self.line_width = value
        self.update()

    def choose_color(self):
        color = QColorDialog.getColor(self.line_color, self, "Выберите цвет линии")
        if color.isValid():
            self.line_color = color
            self.update()

    def _calculate_hilbert_point(self, params: HilbertCurveParams) -> QPoint:
        """Calculate a single point of the Hilbert curve."""
        return QPoint(params.x + (params.xi + params.yi) // 2,
                     params.y + (params.xj + params.yj) // 2)

    def hilbert_curve(self, params: HilbertCurveParams, points: list) -> None:
        """Generate points for the Hilbert curve.

        Args:
            params (HilbertCurveParams): Parameters for the Hilbert curve
            points (list): List to store the generated points
        """
        if params.order == 0:
            points.append(self._calculate_hilbert_point(params))
            return

        # Calculate half values
        xi_half = params.xi // 2
        xj_half = params.xj // 2
        yi_half = params.yi // 2
        yj_half = params.yj // 2

        # Recursive calls for each quadrant
        self.hilbert_curve(HilbertCurveParams(
            order=params.order - 1,
            x=params.x,
            y=params.y,
            xi=yi_half,
            xj=yj_half,
            yi=xi_half,
            yj=xj_half
        ), points)

        self.hilbert_curve(HilbertCurveParams(
            order=params.order - 1,
            x=params.x + xi_half,
            y=params.y + xj_half,
            xi=xi_half,
            xj=xj_half,
            yi=yi_half,
            yj=yj_half
        ), points)

        self.hilbert_curve(HilbertCurveParams(
            order=params.order - 1,
            x=params.x + xi_half + yi_half,
            y=params.y + xj_half + yj_half,
            xi=xi_half,
            xj=xj_half,
            yi=yi_half,
            yj=yj_half
        ), points)

        self.hilbert_curve(HilbertCurveParams(
            order=params.order - 1,
            x=params.x + xi_half + params.yi,
            y=params.y + xj_half + params.yj,
            xi=-yi_half,
            xj=-yj_half,
            yi=-xi_half,
            yj=-xj_half
        ), points)

    def paintEvent(self, _):
        """Handle the paint event for the widget."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Set color and line width
        pen = QPen(self.line_color, self.line_width)
        painter.setPen(pen)

        # Generate curve points
        points = []
        self.hilbert_curve(HilbertCurveParams(
            order=self.order,
            x=25,
            y=25,
            xi=self.size,
            xj=0,
            yi=0,
            yj=self.size
        ), points)

        # Draw lines between points
        for i in range(len(points) - 1):
            painter.drawLine(points[i], points[i + 1])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hilbert = HilbertCurve()
        self.setCentralWidget(self.hilbert)
        self.setWindowTitle('Кривая Гильберта')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
