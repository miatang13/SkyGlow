#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is a helper file to transform a set of given points by first selecting 
#the farthest 2 points, choose 1 as the anchor, then rotate all points followed 
#by scaling all of them to the same size as the constellation data.
########################################

import math
import numpy as np
import matplotlib.pyplot as plt
import copy

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

#The function compares all points and outputs the farthest 2 points.
def comparePoints(points):
    #Input: data as a 1D list of coordinates (tuples)
    #Return: the most distant two points, or None otherwise
    if points == [] or len(points) == 1:
        return None  
    longestDistance = -1 #the farthest distance between one point and rest
    farthestPoint1 = ()
    farthestPoint2 = ()
    for i in range(len(points)-1): 
        x1 = points[i][0]
        y1 = points[i][1]   
        for j in range(i + 1, len(points)):
            x2 = points[j][0]
            y2 = points[j][1]          
            curDistance = distance(x1, y1, x2, y2)
            if curDistance > longestDistance:
                longestDistance = curDistance
                farthestPoint1 = (x1, y1)
                farthestPoint2 = (x2, y2)
    return (farthestPoint1, farthestPoint2)

#This function outputs the shifted points with one anchor on (0, 0)
def centerPoints(anchor, farCord, remainingPoints):
    #input: anchor(tuple), the other farthest point, rest of the points
    #output: anchor, farCord, remainingPoints
    offsetX = anchor[0] - 0
    offsetY = anchor[1] - 0
    shiftedAnchor = (anchor[0] - offsetX, anchor[1] - offsetY)
    shiftedFarCord = (farCord[0] - offsetX, farCord[1] - offsetY)
    newRemainPoints = []
    for i in range(len(remainingPoints)):
        theX = remainingPoints[i][0]
        theY = remainingPoints[i][1]
        newRemainPoints.append((theX - offsetX, theY - offsetY))
    return (shiftedAnchor, shiftedFarCord, newRemainPoints)

def rotateRemain(newRemainPoints, shiftTheta):
    rotatedList = []
    for i in range(len(newRemainPoints)):
        r, theta = coordToPolar(newRemainPoints[i][0], newRemainPoints[i][1])
        newTheta = theta - shiftTheta
        newX, newY = polarToCoord(r, newTheta)
        rotatedList.append((newX, newY))
    return rotatedList

def rotateFarCord(shiftedFarCord, shiftTheta):
    r, theta = coordToPolar(shiftedFarCord[0], shiftedFarCord[1])
    newTheta = theta - shiftTheta
    newX, newY = polarToCoord(r, newTheta)
    rotatedFarCord = (newX, newY)
    return rotatedFarCord

def rotateFlat(shiftedAnchor, shiftedFarCord, newRemainPoints):
    #Input: Anchored coordinates 
    #Return: Rotate coordinates
    farX = shiftedFarCord[0]
    farY = shiftedFarCord[1]
    shiftTheta = math.atan(farY / farX)
    rotatedFarCord = rotateFarCord(shiftedFarCord, shiftTheta)
    rotatedRemain = rotateRemain(newRemainPoints, shiftTheta)
    return (shiftedAnchor, rotatedFarCord, rotatedRemain)

def scale(starFarthest, shiftedFarCord, newRemainPoints):
    #Return: scaled user input coordinates
    ratio  = starFarthest / shiftedFarCord[0]
    scaledPoints = []
    finalFarCord = starFarthest
    for i in range(len(newRemainPoints)): #all the other points
        newX = newRemainPoints[i][0] * ratio
        newY = newRemainPoints[i][1] * ratio
        scaledPoints.append((newX, newY))
    return finalFarCord, scaledPoints

##############################helpers end######################################

def transform(points, starFarthest):
    farPoints = comparePoints(points) #tuple
    for i in range(len(farPoints)-1): #try both
        anchor = farPoints[i]
        farCord = farPoints[1 - i]
        remainingPoints = copy.deepcopy(points)
        remainingPoints.remove(anchor)
        remainingPoints.remove(farCord)
        shiftedAnchor =  centerPoints(anchor, farCord, remainingPoints)[0]
        shiftedFarCord = centerPoints(anchor, farCord, remainingPoints)[1]
        newRemainPoints = centerPoints(anchor, farCord, remainingPoints)[2]
        shiftedAnchor = rotateFlat(shiftedAnchor, shiftedFarCord, newRemainPoints)[0]
        rotatedFarCord = rotateFlat(shiftedAnchor, shiftedFarCord, newRemainPoints)[1]
        rotatedRemain = rotateFlat(shiftedAnchor, shiftedFarCord, newRemainPoints) [2]
        finalFarCord = scale(starFarthest, shiftedFarCord, newRemainPoints)[0]
        scaledPoints = scale(starFarthest, shiftedFarCord, newRemainPoints)[1]
        transformed = [rotatedFarCord] + rotatedRemain + [shiftedAnchor]
    return transformed


def shiftToSee(points):
    allX, allY = [], []
    for point in points:
        allX.append(point[0])
        allY.append(point[1])
    minX, minY = min(allX), min(allY)
    buffer = 100
    shiftX, shiftY = 0 - minX + 100, 0 - minY + 100
    newPoints = []
    for point in points:
        newX, newY = point[0] + shiftX, point[1] + shiftY
        newPoints.append((newX, newY))
    return newPoints


###################################tests######################################
#points = [(289, 34), (275, 171), (248, 293), (147, 396), (437, 461)]   
#print(transform(points))
#transformed = transform(points)

def plotGraph(points):
    plt.axis([-1000, 1000, -1000, 1000])
    for p in points:
        plt.plot(p[0], p[1], "bo")
    plt.show()

#plotGraph(points)
#plotGraph(transformed)

##############Graph Testing###############
'''
anchor = (0.0, 0.0)
farCoord = (5.0, 5.0)
remains = [(0.9, 1.1), (2.1, 2.0), (-4.0, -4.1), (-1.0, 1.0), (-2.0, 2.0)]

#newAnchor, newCoord, newRemain = rotateFlat(anchor, farCoord, remains)

def plotGraph(anchor, farCoord, remains):
    plt.axis([-10, 10, -10, 10])
    plt.plot(anchor[0], anchor[1], "bo")
    plt.plot(farCoord[0], farCoord[1], "bo")
    for p in remains:
        plt.plot(p[0], p[1], "bo")
    #plt.show()


#plotGraph(anchor, farCoord, remains)
#plotGraph(newAnchor, newCoord, newRemain)
'''
'''
#########################################

def testcomparePoints():
    print("Testing comparePoints()...", end="")
    assert(comparePoints([]) == None)
    assert(comparePoints([(0, 0)]) == None)
    assert(comparePoints([(0, 0), (2, 2), (1, 1)]) == ((0, 0), (2, 2)))
    assert(comparePoints([(0, 0), (2, 2), (8,8)]) == ((0, 0), (8, 8)))
    assert(comparePoints([(9, 5), (50, 30), (0, 0)]) == ((50, 30), (0, 0)))
    assert(comparePoints([(9, 2), (9, 3), (50, 50)]) == ((9, 2), (50, 50)))
    print("Passed!")

def testCenterPoints():
    print("Testing centerPoints()...", end="")
    assert(centerPoints((3,3), (8,5),[(2,1),(5,5),(80,80)]) == ((0,0), \
                                            (5,2), [(-1,-2),(2,2),(77,77)]))
    assert(centerPoints((13,11), (5,9),[(2,1),(5,5),(80,80)]) == ((0,0), \
                                        (-8,-2), [(-11,-10),(-8,-6),(67,69)]))
    print("Passed!")

def testScale():
    print("Testing scale()...", end="")
    assert(scale(5, [10, 8], [(20,16),(3,5),(6,8),(14,18)]) == ((5, [(10, 8), \
                                                    (1.5, 2.5),(3,4),(7,9)])))
    print("Passed!")



testcomparePoints()
testCenterPoints()
testScale()
'''





    

