#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is a helper file for SkyGlow's interactive graphics when user are
#clicking the stars.
########################################


from tkinter import *
import random
import math

def init(data):
    data.counter = 0 
    data.radius = 5
    data.points = []
    data.removed = []
    data.twinkle = (0, 0)
    data.twinkleR = 20 #upperbound, inclusive
    data.twinklePoint = 15 #upperbound
    data.twinkleColor = "light cyan"
    data.lines = []
    data.lineMax = 5
    data.lineThickMax = 2
    data.lineColor = 'gray94'
    data.backgroundColor = 'SkyBlue3'
    data.pointColor = "white"
    data.clickConfirm = 0

def timerFired(data):
    data.counter += 1
    #every half second, a random star sparkles
    #if data.counter % 3 == 0:
    if len(data.points) > 1:
        twinkleIndex = random.randint(0, (len(data.points))-1)
        data.twinkle = data.points[twinkleIndex]
    newLine(data)
    if data.counter >= 50:
        data.done = True

def mousePressed(event, data):
    data.points.append((event.x, event.y))

def keyPressed(event, data):
    if event.keysym == "BackSpace":
        if len(data.points) >= 1:
            thePoint = data.points[-1]
            data.removed.append(thePoint)
            data.points.pop()
       
    if event.keysym == "Right":
        if len(data.removed) > 1:
            data.points.append(data.removed[-1])
            data.removed.pop()

################################DRAW FUNCTIONS##################################

def drawPoints(canvas, data):
    for point in data.points:
        x = point[0]
        y = point[1]
        r = data.radius
        bigRadius = r * 2
        x1, x2 = x - r, x + r
        y1, y2 = y - r, y + r
        bigX1, bigX2 = x - bigRadius, x + bigRadius
        bigY1, bigY2 = y - bigRadius, y + bigRadius
        canvas.create_oval(bigX1, bigY1, bigX2, bigY2, outline = "SlateGray3")
        canvas.create_oval(x1, y1, x2, y2, fill = data.pointColor, outline = "")
        

'''##########Line Start###########'''

def getNewLine(data):
    points = len(data.points) - 1
    startIndex = random.randint(0, points)
    endIndex = random.randint(0, points)
    startPoint = data.points[startIndex]
    endPoint = data.points[endIndex]
    return (startPoint, endPoint)

def thickness(data):
    thickness = random.randint(0, data.lineThickMax)
    return thickness

def newLine(data):
    if len(data.points) < 2:
        return
    if len(data.lines) > data.lineMax:
        popIndex = random.randint(0, len(data.lines)-1)
        data.lines.pop(popIndex)
    if data.counter % 10 == 0:
        startPoint, endPoint = getNewLine(data)[0], getNewLine(data)[1]
        x1, y1 = startPoint[0], startPoint[1]
        x2, y2 = endPoint[0], endPoint[1]
        width = thickness(data)
        data.lines.append([(x1, y1), (x2, y2), width])

#def boundary(data):

def drawLines(canvas, data):
    for line in range(len(data.lines)):
        line = data.lines[line]
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]
        thickness = line[2]
        if (x1, y1) in data.points and (x2, y2) in data.points:
            canvas.create_line(x1, y1, x2, y2, fill = data.lineColor)

'''##########Line End#############'''


'''##########Twinkle Start###########'''
#This is the main function to draw the twinkles.
def drawTwinkle(canvas,data):
    twinkle = data.twinkle
    cx, cy = twinkle[0], twinkle[1]
    if cx == 0 and cy == 0:
        return 
    if (cx, cy) not in data.points:
        return
    radius = random.randint(0, data.twinkleR)
    diameter = radius* 2
    numPoints = random.randint(3, data.twinklePoint)
    color = data.twinkleColor
    drawStar(canvas, data, cx, cy, diameter, numPoints, color)

#This has used some code from the hw star assignment with adjustments.
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
        canvas.create_polygon(allCord, fill = color)

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
    #canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    drawTwinkle(canvas,data)
    drawPoints(canvas,data)
    drawLines(canvas,data)


#Run function from CMU 15-112 Course Website
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def run(width=600, height=500):
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
    
    print("bye!")

#run()