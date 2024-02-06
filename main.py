import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
import random


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self):
        # Генерация случайных параметров для окружности
        x = random.randint(10, self.width() - 10)
        y = random.randint(10, self.height() - 10)
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Добавление окружности в список для отрисовки
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(color)
            painter.drawEllipse(x - diameter / 2, y - diameter / 2, diameter, diameter)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Генерация окружностей')

        self.central_widget = CircleWidget()
        self.setCentralWidget(self.central_widget)

        self.pushButton = QPushButton('Создать окружность')
        self.pushButton.clicked.connect(self.central_widget.add_circle)

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.central_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
