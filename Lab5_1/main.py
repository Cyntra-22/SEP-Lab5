import thanida_lab5
import beam_lab5
import myopapakyawLab5
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget

def main():
    app = QApplication(sys.argv)
    
    t = thanida_lab5.Simple_drawing_window2()
    t.show()
    c = beam_lab5.Simple_Drawing_Window3()
    c.show()
    p = myopapakyawLab5.Simple_drawing_window1()
    p.show()
    
    return app.exec()
    
    
if __name__ == "__main__":
    main()