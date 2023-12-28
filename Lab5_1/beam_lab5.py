import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget

class Simple_Drawing_Window3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple GitHub Drawing")

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)


        # Draw a yellow ellipse
        painter.setPen(QColor(255, 255, 0))
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(50, 150, 100, 100)
        painter.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_Drawing_Window3()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())