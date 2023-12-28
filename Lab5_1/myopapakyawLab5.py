import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self,e):
        p = QPainter(self)
        p.begin(self)

        p.setPen(QColor(255, 0, 0)) 
        p.setBrush(QColor(255, 0, 0))  

        p.drawPie(100, 100, 200, 200, 45 * 16, 180 * 16)  
        p.drawPie(200, 100, 200, 200, 135 * 16, 180 * 16)  
        p.drawChord(130, 100, 150, 100, 0, 180 * 16)  

        p.end()


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())