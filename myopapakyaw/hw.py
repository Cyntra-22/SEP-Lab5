import sys
import string
import random

from PySide6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, 
        QApplication, QWidget)
from PySide6.QtCore import (Qt, QVariantAnimation)
from PySide6.QtGui import (QPen, QPainter, QColor)

class Arc:
    colors = list(string.ascii_lowercase[0:6]+string.digits)

    shades_of_blue = ["#7CB9E8","#00308F","#72A0C1", "#F0F8FF",
            "#007FFF", "#6CB4EE", "#002D62", "#5072A7", 
            "#002244", "#B2FFFF", "#6F00FF", "#7DF9FF","#007791",
            "#ADD8E6", "#E0FFFF", "#005f69", "#76ABDF",
            "#6A5ACD", "#008080", "#1da1f2", "#1a1f71", "#0C2340"]

    shades_of_green = ['#32CD32', '#CAE00D', '#9EFD38', '#568203', '#93C572',
            '#8DB600', '#708238', '#556B2F', '#014421', '#98FB98', '#7CFC00',
            '#4F7942', '#009E60', '#00FF7F', '#00FA9A', '#177245', '#2E8B57', 
            '#3CB371', '#A7F432', '#123524', '#5E8C31', '#90EE90', '#03C03C',
            '#66FF00', '#006600', '#D9E650']

    def __init__(self):
        self.diameter = random.randint(100, 600)

        
        self.color = QColor(Arc.shades_of_green[random.randint(0, len(Arc.shades_of_green)-1)])
       
        self.span = random.randint(40, 150)
        self.direction = 1 if random.randint(10, 15)%2 == 0 else -1
        self.startAngle = random.randint(40, 200)
        self.step = random.randint(100, 300)

class ArcWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.arcs = [Arc() for i in range(random.randint(10, 20))]
        self.startAnime()

    def initUI(self):
        #self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color:black;")

    def startAnime(self):

        self.anim = QVariantAnimation(self, duration = 2000)
        self.anim.setStartValue(0)
        self.anim.setEndValue(360)
        self.anim.valueChanged.connect(self.update)
        self.anim.start()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        for arc in self.arcs:
            painter.setPen(QPen(arc.color, 6, Qt.SolidLine))
            painter.drawArc(self.width()/2 - arc.diameter/2,
                    self.height()/2 - arc.diameter/2, arc.diameter, 
                    arc.diameter, self.anim.currentValue()*16*arc.direction+arc.startAngle*100, arc.span*16) 
            
        if self.anim.currentValue() == 360:
            
            self.startAnime()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animate Arc")
        self.setGeometry(100, 100, 600, 600)
        self.arcWidget = ArcWidget()
        self.setCentralWidget(self.arcWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec()