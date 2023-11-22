import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect
import random

class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.diameter = 0

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(QRect(10, 10, self.diameter, self.diameter))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle("Circle App")

        self.circle_widget = CircleWidget(self)
        self.setCentralWidget(self.circle_widget)

        self.button = QPushButton("Создать окружность", self)
        self.button.setGeometry(50, 200, 200, 30)
        self.button.clicked.connect(self.create_circle)

    def create_circle(self):
        diameter = random.randint(10, 100)
        self.circle_widget.diameter = diameter
        self.circle_widget.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())