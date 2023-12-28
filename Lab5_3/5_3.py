import turtle

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
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.pensize(3)
        for i in range(2):
            turtle.forward(self.width/2)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
            turtle.forward(self.width/2)
        turtle.penup()

    def newpos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def cleardisk(self):
        # using turtle to clear a disk
        turtle.penup()
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.pensize(3)
        turtle.pencolor("white")
        for i in range(2):
            turtle.forward(self.width/2)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
            turtle.forward(self.width/2)
        turtle.penup()
        turtle.pencolor("black")

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, lenght=100):
        self.name = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plenght = lenght

    def showpole(self):
        # using turtle to draw a pole
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.pendown()
        turtle.pensize(self.pthick)
        turtle.pencolor("black")
        turtle.left(90)
        turtle.forward(self.plenght)
        turtle.right(90)
        turtle.penup()
        turtle.goto(self.pxpos - 250, self.pypos - 150)
        turtle.write(self.name, font=("Arial", 16, "normal"))

    def pushdisk(self, disk):
        # using turtle to push a disk
        turtle.penup()
        disk.newpos(self.pxpos, self.toppos)
        disk.showdisk()
        self.stack.append(disk)
        self.toppos += disk.height


    def popdisk(self):
        # using turtle to pop a disk
        turtle.penup()
        disk = self.stack.pop()
        disk.cleardisk()
        self.toppos -= disk.height
        return disk

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
turtle.done()