import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        
        p.drawPolygon([QPoint(70,220),QPoint(100,230),QPoint(130,220),QPoint(100,270)])
        p.drawPolygon([QPoint(100,230),QPoint(100,150)])
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window2()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main()) 