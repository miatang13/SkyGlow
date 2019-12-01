#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is a helper file for SkyGlow's background graphics.
########################################

from tkinter import *
import random


class Dots(object):

    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.radius = 2
        self.color = random.choice(["gray39", "gray", "gray80"])

    def draw(self, canvas):
        x1, y1 = self.cx - self.radius, self.cy - self.radius
        x2, y2 = self.cx + self.radius, self.cy + self.radius
        canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = "")

    def lightUp(self):
        self.color = "light grey"
    
    def back(self):
        self.color = random.choice(["white", "gray", "gray"])

    def onTimerFired(self, data):
        if data.bkcounter % 30 == 0:
            self.lightUp()
        else:
            self.back()
    
class SmallDots(Dots):
    def __init__(self, cx, cy, shift):
        super().__init__(cx, cy)
        self.radius = self.radius // 2
        self.cx = cx + shift
        self.cy = cy + shift

    def changeColor(self):
        self.color = random.choice(["honeydew2", "lavender", "azure"])
        
    def shrinking(self):
        self.radius -= 5

    def expanding(self):
        self.radius += 5

    def onTimerFired(self, data):  
        if data.bkcounter % 5 == 0:
            self.shrinking()
        else:
            self.expanding()
        if self.radius > 5:
            self.shrinking()
        if data.bkcounter % 10 == 0:
            self.radius = 2
        self.changeColor()

class CenterDots(Dots):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.color = "dim gray"
        self.radius = self.radius 

    '''def distance(self, other):
        return (math.sqrt((other.cx - self.cx)**2 + (other.cy - self.cy)**2)'''

    def onTimerFired(self, data):
        stepX = (data.width // 2 - self.cx) // 10
        stepY = (data.height // 2 - self.cy) // 10
        self.cx += stepX
        self.cy += stepY

class Line(object):
    def __init__(self, start, end, width):
        self.start = start
        self.end = end
        self.width = width
        self.color = random.choice(["dim gray", "gray20"])

    def draw(self, canvas):
        startX, startY= self.start[0], self.start[1]
        endX, endY = self.end[0], self.end[1]
        canvas.create_line(startX, startY, endX, endY, fill = self.color,
                                        width = self.width)


####################################
# customize these functions
####################################
#Run function from CMU 15-112 Course Website
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def init(data):
    data.bkColor = "SkyBlue3"
    data.bkdots = []
    data.bkcounter = 0
    data.bklines = []


def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def getCord(data):
    oneFifthX = data.width // 5
    oneFifthY = data.height // 5
    cx = random.choice([oneFifthX, 2 * oneFifthX, 3 * oneFifthX, 4 * oneFifthX])
    cy = random.choice([oneFifthY, 2 * oneFifthY, 3 * oneFifthY, 4 * oneFifthY])
    #left = (data.width // 5, data.height // 2) # leftX, leftY
   # top = (data.width // 2, data.height // 5) #topX, topY
    #right = (data.width - data.width // 5, data.height // 2) #rightX, rightY
    #bot = (data.width // 2, data.height - data.height // 5) #botX, botY
    '''resultIndex = random.randint(0, 2)
    choices = [(200, 300), (300, 100), (400, 300)]
    result = choices[resultIndex]'''
    #print(left, top, right, bot)
    result = (cx, cy)
    return result

def newDots(data):
     #cx, cy = getCord(data)[0], getCord(data)[1]  
    cx, cy = random.randint(100, data.width -100), random.randint(100, data.height -100)
    data.bkdots.append(Dots(cx, cy))
    shift = random.randint(-100, 100)
    #data.dots.append(SmallDots(cx, cy, shift))
    data.bkdots.append(CenterDots(cx, cy))

def cleanDotsLine(data):
    if len(data.bkdots) > 300:
        data.bkdots.clear()
        data.bklines.clear()

def timerFired(data):
    data.bkcounter += 1
    newDots(data)
    cleanDotsLine(data)
    if data.bkcounter % 2 == 0:
        newLine(data)
    if len(data.bklines) > 1:
        if data.bkcounter % 3 == 0:
            data.bklines.pop(0)
    for dot in data.bkdots:
        dot.onTimerFired(data)
    
def newLine(data):
    if len(data.bkdots) < 1:
        return 
    i = random.randint(0, len(data.bkdots) - 1)
    j = random.randint(0, len(data.bkdots) - 1)
    dot1, dot2 = data.bkdots[i], data.bkdots[j]
    x1, y1 = dot1.cx, dot1.cy
    start = (x1, y1)
    x2, y2 = dot2.cx, dot2.cy
    end = (x2, y2)
    width = 1
    data.bklines.append(Line(start, end, width))
   
def redrawAll(canvas, data):
    #canvas.create_rectangle(0, 0, data.width, data.height, fill = data.bkColor)
    for dot in data.bkdots:
        dot.draw(canvas)


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
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    
#run(600,600)