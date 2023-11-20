import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка интерфейса из файла UI.ui
        uic.loadUi('UI.ui', self)

        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        # Генерация случайных координат и диаметра для окружности
        x = random.randint(0, self.view.width())
        y = random.randint(0, self.view.height())
        diameter = random.randint(10, 100)

        # Создание окружности и добавление её на сцену
        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QColor(255, 255, 0))  # Желтый цвет
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
