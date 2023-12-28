import turtle
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget


class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
    
    def showdisk(self):
        # using turtle to draw a disk
        turtle.penup()

    def newpos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def cleardisk(self):
        # using turtle to clear a disk
        turtle.penup()


class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, lenght=100):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.thick = thick
        self.lenght = lenght

    def showpole(self):
        # using turtle to draw a pole
        turtle.penup()

    def pushdisk(self, disk):
        # using turtle to push a disk
        turtle.penup()

    def popdisk(self):
        # using turtle to pop a disk
        turtle.penup()


class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d" + str(i), 0, i*150, 20, (n-i)*30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

h = Hanoi()
h.solve()