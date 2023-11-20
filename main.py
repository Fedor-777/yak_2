import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem, QGraphicsScene, QGraphicsView


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.show()
        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)

        circle = QGraphicsEllipseItem(50, 50, diameter, diameter)
        circle.setBrush(QColor(255, 255, 0))
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
