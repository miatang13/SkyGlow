#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is a helper file for SkyGlow's loading graphic.
########################################

from tkinter import *
import random
import math
import numpy as np

####################################
# customize these functions
####################################

def init(data):
    '''data.points = [(50,105), (40, 100), (50, 100), (56,56), (60,103),(52,99),\
                   #(100, 80)]
    data.points = [(20, 105), (10, 100), (50, 100), (56,56), (60,103),(52,99),\
                   (100, 80)]
    data.points = [(40, 35), (30, 40), (70, 40), (80,30), (90,50),(70,40),\
                   (130, 30)]'''
    data.decopoints = [(80, 75), (30, 80), (70, 80), (80,70), (90,90),(130,80),\
                                                    (130, 70)]
    data.decoradius = 2
    data.anchor = (700, 300)
    data.dAngle = 2 * math.pi / 65
    data.counter = 0
    data.rotateOffsetX = data.width // 2
    data.rotateOffsetY = data.height // 2
    data.lineThickMax = 5
    data.decolines = []
    data.innerLines = []
    data.innerLines1 = []
    data.linesColor = "alice blue"
    data.innerLineColor = "SlateGray3"
    data.decopointColor = "gray80"
    data.lineMax = 80
    data.backgroundColor = "SkyBlue3"
    data.innerLineOffset = 20
    twinkle(data)
    data.startDots = False

def twinkle(data):
    data.twinkle = (0, 0)
    data.twinkleR = 10 #upperbound, inclusive
    data.twinklePoint = 8 #upperbound
    data.twinkleColor = "light cyan"
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.counter += 1
    rotatePoint(data)
    newLine(data, data.decopoints)

def distance(x1, y1, x2, y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def coordToPolar(x, y):
    r = distance(x, y, 0, 0)
    theta = np.arctan2([y], [x])[0]
    return r, theta

def polarToCoord(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def rotatePoint(data):
    for i in range(len(data.decopoints)):
        point = data.decopoints[i]
        x = point[0]
        y = point[1]
        r, theta = coordToPolar(x, y)
        newTheta = theta + data.dAngle
        newY = polarToCoord(r, newTheta)[1] 
        newX = polarToCoord(r, newTheta)[0] 
        data.decopoints[i] = (newX, newY)

'''##########Line Start###########'''


def newLine(data, starInput):
    if len(data.decolines) > data.lineMax:
        data.decolines.pop(0)
    if len(data.innerLines) > data.lineMax + 10:
        data.innerLines.pop(0)


    startPoint = (500, 500)
    x1, y1 = startPoint[0], startPoint[1]

    endPoint = starInput[0] 
    x2, y2 = endPoint[0] + data.rotateOffsetY, endPoint[1] + data.rotateOffsetY

    offset = data.innerLineOffset
    innerX2, innerY2 = x2 - offset, y2 - offset
    
    data.decolines.append([(x1, y1), (x2, y2)])
    data.innerLines.append([(x1, y1),(innerX2, innerY2)])   


def simplyDrawLine(data, canvas, linesList, color):
    for i in range(len(linesList)):
        line = linesList[i]
        x1, y1 = line[0][0], line[0][1] 
        x2, y2 = line[1][0] , line[1][1]
        canvas.create_line(x1, y1, x2, y2, fill = color,\
                                             width = 1)

def drawLines(canvas, data, starInput):
    newLine(data, starInput)
    simplyDrawLine(data, canvas, data.decolines, data.linesColor)
    simplyDrawLine(data, canvas, data.innerLines, data.innerLineColor)
    #simplyDrawLine(data, canvas, data.innerLines1)

'''##########Line End#############'''

def drawPoint(canvas, data, point):
    point = point
    x = point[0] + data.rotateOffsetX
    y = point[1] + data.rotateOffsetY
    r = data.decoradius
    shift = 100
    x1, x2 = x - r + shift, x + r + shift
    y1, y2 = y - r + shift, y + r + shift
    canvas.create_oval(x1, y1, x2, y2, fill = data.decopointColor, outline = "")


'''##########Twinkle Start###########'''

#This is the main function to draw the twinkles.
def drawTwinkle(canvas,data, starInput):
    #twinkle(data, starInput)
    twinkleIndex = random.randint(0, (len(starInput))-1)
    data.twinkle = starInput[twinkleIndex]
    twinkle = data.twinkle
    cx, cy = twinkle[0] + data.rotateOffsetY, twinkle[1] + data.rotateOffsetY
    radius = random.randint(0, data.twinkleR)
    diameter = radius* 2
    numPoints = random.randint(3, data.twinklePoint)
    color = data.twinkleColor
    drawStar(canvas, data, cx, cy, diameter, numPoints, color)

#This function draws a star.
def drawStar(canvas, data, centerX, centerY, diameter, numPoints, color):
    angle = 2 * math.pi / numPoints
    #outside coordinates start with the perpendicular angle
    offSetAngle = math.pi / 2
    outerCord = findCordinates(canvas, centerX, centerY, diameter,\
                                    numPoints, angle, offSetAngle)
    #now we want to caculate the coordinates of the inner points
    diameter = diameter * 3 / 8
    offSetAngle = math.pi / 2 + angle / 2
    innerCord = findCordinates(canvas, centerX, centerY, diameter,\
                                    numPoints, angle, offSetAngle)
    #python reads the coordinates in order, thus we make sure we have an 
    #outer coordinate followed by an inner coordinate.
    allCord = interleave(outerCord, innerCord)
    canvas.create_polygon(allCord, fill = color, outline = "")

#returns a list of coordinates and we can alter where the angle starts.
def findCordinates(canvas, centerX, centerY, diameter, numPoints, angle,
                                offSetAngle):
        radius = diameter / 2
        allCord = []
        for i in range(numPoints):
            xCord = math.cos(offSetAngle + (i * angle)) * radius
            #since the y axis increases as we go down on the canvas, 
            #we want the negative.
            yCord = -math.sin(offSetAngle + (i * angle)) * radius
            xCord += centerX
            yCord += centerY
            allCord.append((xCord, yCord))
        return allCord

#This function organizes the outer coordinates and inner coordinates.
def interleave(outerCord, innerCord):
    allCord = []
    #the outerCord and innerCord should have the same length.
    for i in range (len(outerCord)):
        allCord.append(outerCord[i])
        allCord.append(innerCord[i])
    return allCord
'''##########Twinkle End##############'''

def redrawAll(canvas, data):
    '''canvas.create_rectangle(0, 0, data.width, data.height,\
                                    fill = "black", outline = "")'''
    drawTwinkle(canvas, data, data.decopoints)
    for point in data.decopoints:
        drawPoint(canvas, data, point)
    drawLines(canvas, data, data.decopoints)

    

####################################
# use the run function as-is
####################################
#Run function from CMU 15-112 Course Website
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
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
    
#run(800, 600)