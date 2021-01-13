#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is a helper file to compare the given user input with the data.
########################################


import math
import copy


def distance(x1, y1, x2, y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

#drawnPoints = [(0,0), (1,2),(3,8), (9, 10)]
#constellationPoints = [(5,5), (8,10), (12, 13), (7,8)]

def totalDifference (drawnPoints, constellationPoints):
    differences = abs(len(drawnPoints) - len(constellationPoints)) * 5
    starPoints = copy.deepcopy(constellationPoints)
    for i in range(len(drawnPoints) -1 ):
        drawnX = drawnPoints[i][0]
        drawnY = drawnPoints[i][1]
        closestDist = 100000
        closestPoint = 0
        for j in range(len(starPoints) - 1): #find the closest one
            pointX = starPoints[j][0]
            pointY = starPoints[j][1]
            curDistance = distance(drawnX, drawnY, pointX, pointY)
            #print(curDistance)
            if curDistance < closestDist:
                closestDist = curDistance
                closestPoint = j #index int
                theX = pointX
                theY = pointY
                #print(type(closestPoint))
        differences += (distance(drawnX, drawnY, theX, theY))
        #print(closestPoint)
        if len(starPoints) >= 1:
            starPoints.pop(closestPoint) 
    return differences

#print(totalDifference(drawnPoints, constellationPoints))

            
