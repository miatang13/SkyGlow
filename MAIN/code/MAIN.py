#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is the main file for SkyGlow.
########################################


#modules
from tkinter import *
from PIL import Image, ImageTk
import string
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import copy
import time


#files
import starryBackground as introBackground
import userClickPoints as clickPoints
import constellationData as constellationData
import Transform as transformfl
import loadRotateGraphic as rotateGraphic
import Compare as comparefl
import tetrahedron as tetraGraphic
import openingCircle as openCircle


def init(data):
    data.stage = "open"
    openData(data)
    graphicsData(data)
    browseData(data)
    inputData(data)
    evaluateGraphicsData(data)
    transformData(data)
    resultData(data)

def openData(data):
    openCircle.init(data)
    data.openBackgroundColor = "black"
    data.lightBackground = False

def graphicsData(data):
    data.titleTextColor = "honeydew4"
    data.headTextColor = "ivory4"
    data.subTextColor = "dim gray"
    introBackground.init(data)
    data.backgroundImg = Image.open("marble.png")
    data.backgroundImg = ImageTk.PhotoImage(data.backgroundImg)

def browseData(data):
    data.constellations = ['Virgo', 'Taurus', "Scorpio", 'Pisces',\
        'Sagittarius','Libra', 'Capricorn','Cancer', 'Aries', 'Aquarius', \
            'Leo', 'Gemini', 'Ophiuchus']
    data.browseConstCx = data.width // 5 * 4
    data.browseConstCy = data.height // 9 * 4.5
    data.browseConstellation = None
    data.browseText = ""
    constellationData.constellationImages(data)
    data.constellationImages = [data.Virgo, data.Taurus, data.Scorpio,\
         data.Pisces, data.Sagittarius, data.Libra, data.Capricorn,data.Cancer,\
              data.Aries, data.Aquarius, data.Leo, data.Gemini, data.Ophiuchus]
    constellationData.constellationText(data)
    data.constellationText = [data.VirgoText, data.TaurusText, data.ScorpioText,\
        data.PiscesText, data.SagittariusText, data.LibraText, \
        data.CapricornText,data.CancerText, data.AriesText, data.AquariusText,\
             data.LeoText, data.GeminiText, data.OphiuchusText ]

def inputData(data):
    data.userFileInput = ""
    data.fileName = ""
    data.userImage = ""
    clickPoints.init(data)
    data.startClick = False
    data.completeClick = False

def evaluateGraphicsData(data):
    rotateGraphic.init(data)
    data.evaluate = False
    data.analyzeTimer = 0

def transformData(data):
    constellationData.constellationPoints(data)
    data.constellationCoordinates = [data.VirgoPoints, data.TaurusPoints,\
    data.ScorpioPoints, data.PiscesPoints, data.SagittariusPoints, \
    data.LibraPoints, data.CapricornPoints,data.CancerPoints, data.AriesPoints,\
    data.AquariusPoints, data.LeoPoints, data.GeminiPoints, data.OphiuchusPoints]
    data.constellationLen = [12, 12, 13, 15, 21, 8, 13, 5, 6, 16, 10, 16, 22]
    data.starFarthestPoint = [-412.53484701295235, 440.72894164100455,\
    485.9650193172344, 378.89312477267254, 426.2510997053263, -386.20331433067736,\
    -484.62047005878736, 451.9214533522391, 423.46782640479313, 483.125242561388,\
    -548.0036496228835, 444.94606414710535, -440.2238067165382]
    data.transformedPoints = []
    data.possibleConstellations = []
    data.possibleConstellationsIndex = []
    data.finalConstellation = ""
    data.finalScore = 0
    data.loading = False

def resultData(data):
    data.resultTimer = 0
    tetraGraphic.init(data)

def timerFired(data):
    if data.stage == "open":
        openTimerFired(data)
    if data.stage == "intro":
        introTimerFired(data)
    if data.stage == "stars":
        clickPoints.timerFired(data)
    if data.stage == "analyze":
        analyzeTimerFired(data)
    if data.stage == "result":
        resultTimerFired(data)
    
def keyPressed(event, data):
    if data.stage == "open":
        keyPressedOpen(event, data)
    if data.stage == "intro":
        keyPressedIntro(event, data)
    if data.stage == "upload":
        keyPressedUpload(event, data)
    if data.stage == "stars":
        keyPressedStars(event, data)

def mousePressed(event, data):
    print(data.stage)
    if data.stage == "intro": #intro
        mousePressedIntro(event, data)
    if data.stage == "greeting": #greets
        mousePressedGreeting(event, data)
    if data.stage == "browse": #look through 13 constellations
        mousePressedBrowse(event, data)
    if data.stage == "upload": #upload photo and draw points
        mousePressedUpload(event, data)
    if data.stage == "stars": #
        mousePressedStars(event, data)
    if data.stage == "analyze": #analyze graphics
        mousePressedAnalyze(event, data)
    if data.stage == "result":
        mousePressedResult(event, data)
    
def mouseMotion(event, data):
    if data.stage == "open":
        mouseMotionOpen(event, data)
    if data.stage == "browse":
        mouseMotionBrowse(event, data)

def redrawAll(canvas, data):
    if data.stage == "open":
        drawOpen(canvas, data)
    if data.stage == "intro":
        drawIntro(canvas, data)
    elif data.stage == "greeting":
        drawGreeting(canvas, data)
    elif data.stage == "browse": #browse through stars
        drawBrowse(canvas, data)
    elif data.stage == "upload": #browse through stars
        drawUpload(canvas, data)
    elif data.stage == "stars": 
        drawStars(canvas, data)
    elif data.stage == "analyze":
        drawAnalyze(canvas, data)
    elif data.stage == "result":
        drawResult(canvas, data)


######################Open##########################


def openTimerFired(data):
    openCircle.timerFired(data)

def keyPressedOpen(event, data):
    if event.keysym == "space":
        if data.lightBackground:
            data.littleCircleColor = "black"
            data.lightBackground = False
        else:
            data.littleCircleColor = "snow3"
            data.lightBackground = True
    if event.keysym == "Return":
        data.stage = "intro"

def mouseMotionOpen(event, data):
    openCircle.motion(event, data)

def drawOpen(canvas, data):
     #canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    if data.lightBackground:
        canvas.create_rectangle(0, 0, data.width, data.height, \
                                    fill = "SlateGray3", outline = "")
        for i in range(len(data.planet.littleCircles)):
            data.planet.littleCircles[i].fill = random.choice(["light blue", \
                                            "LightBlue2", "light steel blue", "lavender"])
    else:
        canvas.create_rectangle(0, 0, data.width, data.height, \
                                    fill = data.openBackgroundColor)
        for i in range(len(data.planet.littleCircles)):
            data.planet.littleCircles[i].fill = "black"
    openCircle.redrawAll(canvas, data)


######################Intro#########################

def keyPressedIntro(event, data):
    if event.keysym == "Left":
        data.stage = "open"

def mousePressedIntro(event,data):
    cx, cy = data.width // 2, data.height // 2
    space = 50
    if event.x in range(cx - space, cx + space) and event.y in range(cy - space, cy + space):
        data.stage = "greeting"

def introTimerFired(data):
    pass

def drawIntro(canvas, data):
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    titleCx, titleCy = data.width//2, data.height//2
    rectWidth, rectHeight = 130, 20
    offset = 30
    canvas.create_text(titleCx, titleCy, text = "S k y G l o w",\
     font = "Times 30", fill = data.titleTextColor)
    canvas.create_text(titleCx, titleCy + offset, \
                text = "L e t ' s  s e e  t h e  s t a r s . ",\
                font = "Times 15", fill = data.titleTextColor)

######################Greetings######################


def mousePressedGreeting(event, data):
    cx, cy = data.width - data.width // 6, data.height // 2
    space = 20
    if event.x in range(cx - space, cx + space) and event.y in range(cy - space, cy + space):
        data.stage = "browse"

def drawGreeting(canvas, data):
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    titleCx, titleCy = data.width//2, data.height//2
    mainOffset, subOffset = 10, 30
    canvas.create_text(titleCx, titleCy - mainOffset, text = "H e y,", \
        font = "Times 30", fill = data.titleTextColor)
    canvas.create_text(titleCx, titleCy + subOffset,\
        text = "I hope the day has been going well for you. \n What constellation are you seeing today ? ",\
                             font = "Times 15", fill = data.titleTextColor)
    cx, cy, r = data.width - data.width // 6, data.height // 2, 20
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = "ivory2", outline = "")

######################Browse Stars###################

def mousePressedBrowse(event, data):
    clickNext(event, data)
    
def clickNext(event, data):
    headingOffsetX, headingOffsetY = data.width // 10, data.height // 10
    nextCx, nextCy = data.width - headingOffsetX, data.height - headingOffsetY
    space = 50
    if event.x in range(nextCx - space, nextCx + space) and\
         event.y in range(nextCy - space, nextCy + space):
        data.stage = "upload"

def mouseMotionBrowse(event, data):
    browseStar(event, data)

def browseStar(event, data):
    contentOffsetX, boarderX = data.height // 15, data.width // 6
    contentOffsetY, boarderY = data.height // 20, data.height // 5 + 10
    for i in range(len(data.constellations)):
        cx = i * contentOffsetX + boarderX
        cy = i * contentOffsetY + boarderY
        space = 20
        if event.x in range(cx - space, cx + space) and event.y in range(cy - space, cy + space):
            constellation = data.constellations[i]
            data.browseConstellation = data.constellationImages[i]
            data.browseText = data.constellationText[i]

def displayStarImage(canvas, data):
    cx = data.browseConstCx 
    cy = data.browseConstCy
    rectSide = 80
    canvas.create_rectangle(cx - rectSide, cy - rectSide, cx + rectSide, cy + rectSide,\
    fill = data.titleTextColor, outline = "")
    canvas.create_image(cx, cy, image = data.browseConstellation)

def drawBrowse(canvas, data): #main draw function
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    headingOffsetX, headingOffsetY = data.width // 10, data.height // 10
    canvas.create_text(data.width - headingOffsetX, headingOffsetY,\
     text = "C o n s t e l l a t i o n s", anchor = "ne", font = "Times 18",\
                                                 fill = data.titleTextColor)
    canvas.create_text(data.width - headingOffsetX, data.height - headingOffsetY,\
         text = "N e x t", anchor = 'se', font = "Times 18", fill = data.titleTextColor)
    writeNames(canvas, data)
    if data.browseConstellation != None:
        displayStarImage(canvas, data)
        writeDescription(canvas, data)

def writeNames(canvas, data):
    contentOffsetX, boarderX = data.height // 15, data.width // 6
    contentOffsetY, boarderY = data.height // 20, data.height // 5 + 10
    for i in range(len(data.constellations)):
        cx = i * contentOffsetX + boarderX
        cy = i * contentOffsetY + boarderY
        canvas.create_text(cx, cy, text = data.constellations[i], \
            font = "Times 15", fill = data.headTextColor)
        offset = 10
        canvas.create_line(data.width // offset, cy + offset, cx,  cy + offset,\
            fill = data.headTextColor)

def writeDescription(canvas, data):
    cx = data.width // 2
    cy = data.height // 7
    canvas.create_text(cx, cy, text = data.browseText, anchor = NW,\
         font = "Times 13", fill = data.headTextColor)


######################Upload + draw Photo#############

def confirmInput(data):
    data.fileName = data.userFileInput
    data.userImage = Image.open(data.fileName)
    maxLen = data.height
    ratio = (maxLen / max(data.userImage.width, data.userImage.height))
    newWidth, newHeight = int(data.userImage.width * ratio), int(data.userImage.height * ratio)
    data.userImage = data.userImage.resize((newWidth, newHeight), Image.ANTIALIAS)
    data.userImage = ImageTk.PhotoImage(data.userImage)
    data.stage = "stars"

def mousePressedUpload(event, data):
    if data.userFileInput != "":
        clickConfirm(event, data)

def keyPressedUpload(event, data):
    if event.keysym in string.ascii_letters:
        data.userFileInput += event.keysym
    if event.keysym == "period":
        data.userFileInput += "."
    if event.keysym == "BackSpace":
        data.userFileInput = data.userFileInput[:-1]
    if event.keysym == "enter":
        if data.userFileInput != "":
            confirmInput(data)

def clickConfirm(event, data):
    space = 20
    cx, cy = data.width // 3 * 2, data.height // 3 * 2
    if event.x in range(cx - space, cx + space) and event.y in range(cy - space, cy + space):
        confirmInput(data)

def drawInstructionText(canvas, data):
    canvas.create_text(data.width//3, data.height//2 + 5,\
    text = "Please enter your file name here:", font = "Times 18 bold",\
         fill = data.titleTextColor)

    canvas.create_text(data.width//3, data.height // 2 + 30, \
    text = "Make sure it is in the same folder as this file. :)", \
        font = "Times 13", fill = data.headTextColor)
    canvas.create_text(data.width - data.width // 4, data.height // 3 * 2, \
    text = "Let's see the stars.", font = "Times 15 bold", fill = data.headTextColor)

def drawUserInput(canvas, data):
    rectHeight, rectWidth = data.height // 20 + 10, data.width // 3
    leftx, lefty = data.width // 2 , data.height // 2
    canvas.create_rectangle(leftx, lefty, leftx + rectWidth, lefty + rectHeight,\
         fill = "ivory2", outline = "")
    textOffset = 15
    canvas.create_text(leftx + textOffset, lefty + textOffset + 5,\
    text = data.userFileInput, font = "Times 20 bold", fill = "ivory4", anchor = W)

def drawUpload(canvas, data):
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    cx, cy, r = data.width // 3 * 2 - 10, data.height // 3 * 2, 10
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = "ivory2", outline = "")
    drawInstructionText(canvas, data)
    drawUserInput(canvas, data)


#####################draw star#########################


def mousePressedStars(event, data):
    if data.startClick == False:
        space = 100
        if event.x in range(data.width // 2 - space, data.width // 2 + space) \
            and event.y in range(data.height // 2 - space, data.height // 2 + space):
            data.startClick = True
            return
    checkComplete(event, data)
    if data.startClick and data.completeClick == False:
        clickPoints.mousePressed(event, data)
        clickPoints.getNewLine(data)
        clickPoints.thickness(data)
        clickPoints.newLine(data)
    clickReturnBrowse(event, data)

def clickReturnBrowse(event, data):
    space = 50
    cx, cy = data.width // 8, data.height // 12 * 11
    if event.x in range(cx, cx + space * 2) and event.y in range(cy - space, cy + space):
        data.startClick = False
        data.completeClick = False
        data.pointColor = "white"
        data.stage = "browse"
        data.clickConfirm = 0

def checkComplete(event, data): 
    cx, cy = data.width // 5 * 4, data.height // 12 * 11  
    space = 40
    if event.x in range(cx - space, cx + space) and event.y in range(cy - space, cy + space):
        data.completeClick = True
        data.pointColor = "salmon1"
        data.clickConfirm += 1
    if data.clickConfirm >= 2:
        data.stage = "analyze"

def keyPressedStars(event, data):
    clickPoints.keyPressed(event, data)

def drawBeforeStart(canvas, data):
    cx, cy = data.width // 2, data.height // 2
    diamondR = data.width // 5
    r = data.width // 10
    canvas.create_rectangle(cx - 2*r, cy - r //2 , cx + r * 2, cy + r // 2, \
        fill = "ivory2", outline = "")
    canvas.create_text(cx, cy, text = "C l i c k  t h e  s t a r s", \
                            font = "Times 18 bold", fill = data.titleTextColor)

def drawStarBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "SkyBlue3",\
                                                            outline = "")

def drawStars(canvas, data): #main draw function
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    canvas.create_text(data.width // 2, data.height // 10, \
    text = "L e t  t h e  s t a r s  s h i n e ", font = "Times 15 bold", \
        fill = data.titleTextColor)
    canvas.create_image(data.width//2, data.height // 2 + 10, imag = data.userImage)
    canvas.create_text(data.width // 5 * 4, data.height // 12 * 11, \
        text = "C o m p l e t e", font = "Times 15 bold", fill = data.titleTextColor)
    canvas.create_text(data.width // 8, data.height // 12 * 11 - 10, \
    text = "Take another look at the Constellations", font = "Times 10 ", \
        anchor = NW, fill = data.titleTextColor )
    if data.startClick == False:
        drawBeforeStart(canvas, data)  
    if data.startClick:
        clickPoints.drawPoints(canvas, data)
        clickPoints.drawLines(canvas, data)
        clickPoints.drawTwinkle(canvas, data)


######################Analyze###########################

def mousePressedAnalyze(event, data):
    cx, cy, space = data.width // 2, data.height // 2, 50
    if data.evaluate == False:
        if event.x in range(cx - space, cx + space) and event.y in range(cy - space, cx + space):
            determinePossibleConstellation(data)
            data.evaluate = True
    else:
        cx, cy = data.width // 2, data.height // 5 * 3
        yesCX, yesCY = cx - 80, cy + 100
        noCX, noCY = cx + 80, cy + 100
        if event.x in range(yesCX - space, yesCX + space) and event.y in range(yesCY - space, yesCY + space):
            data.loading = True
        if event.x in range(noCX - space, noCX + space) and event.y in range(noCY - space, noCY + space):
            data.stage = "stars"
            data.points = []
            data.completeClick = False
            data.clickConfirm = 0
            data.startClick = False
            data.pointColor = "white"
   
#returns a list of possible constellations depending on the number of points
def determinePossibleConstellation(data): 
    inputCordNum = len(data.points)
    for i in range(len(data.constellationLen) - 1):
        numPointsDif = 3
        if abs(data.constellationLen[i] - inputCordNum) <= numPointsDif:
            data.possibleConstellations.append(data.constellations[i]) #name
            data.possibleConstellationsIndex.append(i) #index
    findTheConstellation(data)

def findTheConstellation(data):   
    mostAlikeIndex = 0
    lowestDif = 100000000 #low dif -> more alike
    for index in data.possibleConstellationsIndex:
        data.transformedPoints = transformfl.transform(data.points, data.starFarthestPoint[index])
        possibleStarPoints = data.constellationCoordinates[index]
        curDifference = comparefl.totalDifference(data.points, possibleStarPoints)
        if curDifference < lowestDif: #we don't consider ties
            lowestDif = curDifference
            mostAlikeIndex = index
    data.finalConstellation = data.constellations[mostAlikeIndex]
    data.transformedPoints = transformfl.transform(data.points, data.starFarthestPoint[mostAlikeIndex])
    data.transformedPoints = transformfl.shiftToSee(data.transformedPoints)
    print(data.finalConstellation)

def writePossibleConstellation(canvas, data):
    word = " ".join(str(starName) for starName in data.possibleConstellations)
    cx, cy = data.width // 2, data.height // 5 * 3
    rectWidth, rectHeight = 30, 15
    yesCX, yesCY = cx - 80, cy + 100
    noCX, noCY = cx + 80, cy + 100
    canvas.create_text(cx, cy, text = "You've probably drawn one of the following:", \
                        fill = data.titleTextColor, font = "Times 15 bold")
    canvas.create_text(cx , cy + 50, text = word, fill = data.titleTextColor, \
        font = "Times 18")
    canvas.create_rectangle(yesCX - rectWidth, yesCY - rectHeight, \
        yesCX + rectWidth, yesCY + rectHeight, fill = "ivory2", outline = "")
    canvas.create_rectangle(noCX - rectWidth * 2, noCY - rectHeight,\
         noCX + rectWidth * 2, noCY + rectHeight, fill = "ivory2", outline = "")
    canvas.create_text(yesCX, yesCY, text = "Yes",fill = data.headTextColor, \
        font = "Times 13 bold" )
    canvas.create_text(noCX, noCY, text = "I'd like to redraw.", \
        fill = data.headTextColor, font = "Times 13 bold" )
    
def drawAnalyze(canvas, data):
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    if data.evaluate == False:
        drawBeforeReady(canvas, data)
    if data.loading:
        drawEvaluateLoading(canvas, data)
    elif data.possibleConstellations != []:
        canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
        drawDisplayTransformed(canvas, data)
        writePossibleConstellation(canvas, data)

def drawDisplayTransformed(canvas, data):
    canvas.create_rectangle(50, 50, 750, data.height // 2, \
                                fill = "white smoke", outline = "")
    horStart, horEnd = data.transformedPoints[0], data.transformedPoints[-1]
    canvas.create_line(horStart[0], horStart[1], horEnd[0], horEnd[1], \
                fill = data.titleTextColor)
    canvas.create_line(horStart[0], horStart[1], horStart[0], 100, \
        fill = data.titleTextColor)
    canvas.create_text(horStart[0], horStart[1] + 30, text = "0, 0", \
        font = "Times 10 bold", fill = data.titleTextColor)
    drawPointsGeneral(canvas, data.transformedPoints, data.headTextColor)
    textY = ((50 + data.height // 2) // 2)
    canvas.create_text(data.width // 5 * 4, textY , text = "Transformed\nCoordinates", \
        font = "Times 15 bold", fill = data.titleTextColor)
    canvas.create_text(data.width // 5 * 4, textY + 50, \
        text = "Anchored by two farthest points on \n the horizontal axis for more accurate\n comparison with the Constellations. ", \
        font = "Times 12", fill = data.titleTextColor)
    
def drawPointsGeneral(canvas, points, color):
    for point in points:
        cx, cy, r = point[0], point[1], 3
        canvas.create_oval(cx - r, cy -r, cx + r, cy + r, fill = color, outline = "")

def drawEvaluateLoading(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.subTextColor,\
                                                        outline = "")
    rotateGraphic.redrawAll(canvas, data)
    canvas.create_text(data.width // 2, data.height // 2, \
        text = "E v a l u a t i n g . . .", font = "Times 20", fill = 'linen')

def drawConfirmEvaluate(canvas, data):
    cx, cy, offset, r, = data.width // 2, data.height // 2, data.width, 20, 5
    canvas.create_text(cx, cy, text = "E v a l u a t e", \
        font = "Times 20 bold", fill = data.titleTextColor)
    canvas.create_oval(cx - r, cy + offset - r, cx + r, cy + offset + r, \
        fill = data.titleTextColor, outline = "")

def drawBeforeReady(canvas, data):
    drawPointsGeneral(canvas, data.points, data.titleTextColor)
    tetraGraphic.redrawAll(canvas, data)
    introBackground.redrawAll(canvas, data)
    canvas.create_text(data.width // 2, data.height // 2, \
            text = "R e a d y  t o  E v a l u a t e", font = "Times 20", \
                fill = data.titleTextColor)
    r = 15
    canvas.create_oval(data.width// 2 - r, data.height // 2 + 30 - r, \
    data.width// 2 + r, data.height // 2 + 30 + r, fill = "",\
                             outline = data.titleTextColor)

def analyzeTimerFired(data):
    tetraGraphic.timerFired(data)
    introBackground.timerFired(data)
    if data.loading:
        data.analyzeTimer += 1  
        rotateGraphic.timerFired(data)
        if data.analyzeTimer >= 70:
            data.stage = "result"

######################Result############################

def drawCongrats(canvas, data):
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    canvas.create_text(data.width // 2, data.height // 2 - 50, text = "Congratulations, ", \
    fill = data.headTextColor, font = "Times 25 bold italic")

    canvas.create_text(data.width // 2, data.height // 2, \
    text = "You have successfully identified %s. \n It has now be added to your collection."%(data.finalConstellation),
    fill = data.headTextColor, font = "Times 18")

def drawGoodDay(canvas, data):
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    canvas.create_text(data.width // 2, data.height // 2, text = 
    "Have a wonderful day.", fill = data.titleTextColor, font = "Times 25 italic")

def drawEnding(canvas, data):
    canvas.create_image(data.width//2, data.height // 2, image = data.backgroundImg)
    canvas.create_text(data.width // 2, data.height // 2, text = 
        "S k y G l o w", fill = data.titleTextColor, font = "Times 30")
    canvas.create_text(data.width // 2, data.height // 2 + 50, text = "A G A I N",\
        fill = "ivory2", font = "Times 13 bold" )
    
def drawResult(canvas, data):
    if data.resultTimer <= 40:
        drawCongrats(canvas, data)
    if 40 < data.resultTimer <= 70:
        drawGoodDay(canvas, data)
    if data.resultTimer > 70:
        drawEnding(canvas,data)

def mousePressedResult(event, data):
    cx, cy = data.width // 2, data.height // 2 + 50
    space = 50
    if event.x in range(cx - space, cx + space) and event.y in range(cy - space, cy + space):
        init(data)

def resultTimerFired(data):
    data.resultTimer += 1

#Run function from CMU 15-112 Course Website
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
############################################################

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
        mouseMotion(event, data)
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

run(800, 600)
