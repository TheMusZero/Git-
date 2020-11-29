import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(*self.random_coords())

    def random_coords(self):
        coords_x = random.randint(0, 400)
        coords_y = random.randint(0, 300)
        o = random.randint(10, 100)
        if coords_x + o > 400:
            coords_x -= coords_x + o - 400
        if coords_y + o > 300:
            coords_y -= coords_y + o - 300
        return coords_x, coords_y, o, o


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
