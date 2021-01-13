from tkinter import *
import math
import random

class Vertex(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.radius = 2
        self.angle = random.randint(0, 360)
        self.directionX = 1
        self.directionY = 1

    def draw(self, canvas):
        canvas.create_oval(self.cx - self.radius, self.cy - self.radius,
                    self.cx + self.radius, self.cy + self.radius, fill = "gray23")

    def move(self, data):
        theta = math.radians(self.angle)
        dX, dY = math.cos(theta) * 2 * self.directionX, - math.sin(theta) * 3 * self.directionY
        self.cx += dX
        self.cy += dY
        if self.cx < 300:
            self.directionX *= -1
            self.cx += 5
        if self.cx > 500:
            self.directionX *= -1
            self.cx -= 5
        if self.cy <= 100:
            self.directionY *= -1
            self.cy += 5
        if self.cy >= 250:
            self.directionY *= -1
            self.cy -= 5

class Tetrahedron(object):
    def __init__(self, vert1, vert2, vert3, vert4):
        self.vert1 = vert1
        self.vert2 = vert2
        self.vert3 = vert3
        self.vert4 = vert4

    def checkVertex(self, data):
        if self.vert1 not in data.vertex or self.vert2 not in data.vertex or\
            self.vert3 not in data.vertex or self.vert4 not in data.vertex:
            data.tetraremove.add(self)
            

    def draw(self, canvas):
        v1x, v1y = self.vert1.cx, self.vert1.cy 
        v2x, v2y = self.vert2.cx, self.vert2.cy 
        v3x, v3y = self.vert3.cx, self.vert3.cy
        v4x, v4y = self.vert4.cx, self.vert4.cy
        canvas.create_line(v1x, v1y, v2x, v2y, fill = "SlateGray3")
        canvas.create_line(v2x, v2y, v3x, v3y, fill = "honeydew4")
        canvas.create_line(v3x, v3y, v4x, v4y, fill = "light steel blue")
        canvas.create_line(v1x, v1y, v4x, v4y, fill = "LightSteelBlue4")

def init(data):
    data.vertex = set()
    data.tetrahedron = set()
    data.tetratimer = 0
    data.tetraremove = set()

def timerFired(data):
    data.tetratimer += 1
    if len(data.tetrahedron) > 40:
        data.tetrahedron.clear()
    for vert in data.vertex:
        vert.move(data)
    for tetra in data.tetrahedron:
        tetra.checkVertex(data)
    for tetra in data.tetraremove:
        data.tetrahedron.remove(tetra)
    data.tetraremove = set()
    if data.tetratimer % 15 == 0:
        newVertX = random.choice([350, 400, 450])
        newVertY = random.choice([250, 200, 150]) #, 350, 400, 450
        data.vertex.add(Vertex(newVertX, newVertY))
        vertexList = list(data.vertex)
        vert1 = random.choice(vertexList)
        vert2 = random.choice(vertexList)
        vert3 = random.choice(vertexList)
        vert4 = random.choice(vertexList)
        data.tetrahedron.add(Tetrahedron(vert1, vert2, vert3, vert4))

def motion(event, data):
    pass

def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    for vert in data.vertex:
        vert.draw(canvas)
    for tetra in data.tetrahedron:
        tetra.draw(canvas)

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass




#Run function from CMU 15-112 Course Website
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def motionWrapper(event, canvas, data):
        motion(event, data)
        #redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)


    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 25 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
                            motionWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

#run(600, 600)
