#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is a helper file for SkyGlow's opening interactive graphics.
########################################


from tkinter import *
import math
import random
import time

#Ellipse-Line Intersection equation from
#http://mathworld.wolfram.com/Ellipse-LineIntersection.html


class Planet(object):
    def __init__(self, cx, cy, ry, rx, lC, vx, vy, decel, innerParticles):
        self.cx = cx
        self.cy = cy
        self.ry = ry
        self.rx = rx
        self.angle = 0 #offset
        self.av = 0
        self.ad = math.pi/6
        self.maxAngleVelocity = math.pi
        self.staticRY = ry
        self.staticRX = rx
        self.littleCircles = lC
        self.vx = vx
        self.vy = vy
        self.maxV = 500
        self.deceleration = decel
        self.inCollisionX = False
        self.inCollisionY = False
        self.collisionXV = 0
        self.collisionYV = 0
        self.maxCompression = 0.5
        self.lastMouseX = 0
        self.lastMouseY = 0
        self.lastMouseDeterminant = 0
        self.lastMouseTime = 0
        self.mousePlanetVelocityRatio = 1
        self.mousePlanetAVRatio = 0.15
        self.innerParticles = innerParticles
    
    def drawLittleCircles(self,canvas, data):
        a = self.rx
        b = self.ry
        littleCircles = self.littleCircles
        numCircles = len(littleCircles)
        for i in range(numCircles):
            theta = 2 * math.pi / numCircles*i+self.angle
            y0 = math.sin(theta) * 100
            x0 = math.cos(theta) * 100
            x = a*b*x0 / math.sqrt(a*a*y0*y0 + b*b*x0*x0) + self.cx
            y = a*b*y0 / math.sqrt(a*a*y0*y0 + b*b*x0*x0) + self.cy
            radius = littleCircles[i].radius
            width = littleCircles[i].width
            outline = littleCircles[i].outline
            fill = littleCircles[i].fill
            canvas.create_oval(x - radius, y - radius, x + radius, \
                y + radius,fill = fill, outline = outline, \
                                                            width = width)
        
    def drawParticles(self,canvas):
        for particle in self.innerParticles:
            x = particle.cx
            y = particle.cy
            radius = particle.radius
            width = particle.width
            outline = particle.outline
            fill = particle.fill
            canvas.create_oval(x - radius, y - radius, x + radius, \
                y + radius,fill = fill, outline = outline, width = width)
            
class LittleCircle(object):
    def __init__(self, radius, width, outline, fill):
        self.radius = radius
        self.width = width
        self.outline = outline
        self.fill = fill

class Particle(LittleCircle):
    def __init__(self, radius, width, outline, fill,cx,cy,vx,vy):
        super().__init__(radius, width, outline, fill)
        self.cx = cx
        self.cy = cy
        self.vx = vx
        self.vy = vy
        
def ellipseDeterminant(x,y,h,k,a,b):
    determinant = (x - h) ** 2 / a** 2 + (y - k) ** 2/ b ** 2
    return determinant

def init(data):
    data.littleCircleColor = "black"
    lC = []
    for i in range(40):
        fill = random.choice(["light blue", \
                                            "LightBlue2"])
        circle = LittleCircle(6,0,"gray",fill)
        lC.append(circle)

    innerParticles = []
    for i in range(500):
        cx = 400 + random.randint(-100, 100)
        cy = 300 + random.randint(-100, 100)
        vx = random.randint(50, 300)
        vy = random.randint(50, 300)
        radius = random.randint(2, 5)
        fill = random.choice(["wheat1", "LemonChiffon", "powder blue", \
                                                "misty rose"])
        particle = Particle(radius,1,"LightSkyBlue3",fill,cx,cy,vx,vy)
        innerParticles.append(particle)

    data.planet = Planet(200, 200, 150, 150, lC, 280, 280, 50,innerParticles)

#############Timer Fired Helpers###############
def sideNoCollision(planet, data, planetLeft, planetRight):
    if planet.inCollisionX == True:
        planet.inCollisionX = False
        planet.rx = planet.staticRX
        planet.vx = -planet.collisionXV

    if planet.vx > 0:
        planet.vx -= planet.deceleration * data.timerDelay / 1000
        planet.vx = max(0, planet.vx)
    elif planet.vx < 0:
        planet.vx += planet.deceleration * data.timerDelay / 1000
        planet.vx = min(0, planet.vx)

def sideHasCollions(planet, data, planetLeft, planetRight):
    if planet.inCollisionX == False:
        planet.collisionXV = planet.vx
        planet.inCollisionX = True
    if planetRight > data.width:
        ratio = planet.maxV/((1-planet.maxCompression)*planet.staticRX)
        newRX = data.width-planet.littleCircles[0].radius-planet.cx
        planet.rx = newRX
        if planet.vx > 10:
            planet.vx = planet.collisionXV-ratio*(planet.staticRX-newRX)
        else:
            planet.vx = -(planet.collisionXV-ratio*(planet.staticRX-newRX))
    elif planetLeft < 0:
        ratio = planet.maxV/((1-planet.maxCompression)*planet.staticRX)
        newRX = planet.cx-planet.littleCircles[0].radius
        planet.rx = newRX
        if planet.vx < -10:
            planet.vx = planet.collisionXV+ratio*(planet.staticRX-newRX)
        else:
            planet.vx = -(planet.collisionXV+ratio*(planet.staticRX-newRX))

def vertNoCollision(planet, data, planetTop, planetBottom):
    if planet.inCollisionY == True:
        planet.inCollisionY = False
        planet.ry = planet.staticRY
        planet.vy = -planet.collisionYV

    if planet.vy > 0:
        planet.vy -= planet.deceleration * data.timerDelay / 1000
        planet.vy = max(0, planet.vy)
    elif planet.vy < 0:
        planet.vy += planet.deceleration * data.timerDelay / 1000
        planet.vy = min(0, planet.vy)

def verHasCollision(planet, data, planetTop, planetBottom):
    if planet.inCollisionY == False:
        planet.collisionYV = planet.vy
        planet.inCollisionY = True
    if planetBottom > data.height:
        ratio = planet.maxV/((1-planet.maxCompression)*planet.staticRY)
        newRY = data.height-planet.littleCircles[0].radius-planet.cy
        planet.ry = newRY
        if planet.vy > 10:
            planet.vy = planet.collisionYV-ratio*(planet.staticRY-newRY)
        else:
            planet.vy = -(planet.collisionYV-ratio*(planet.staticRY-newRY))
    elif planetTop < 0:
        ratio = planet.maxV/((1-planet.maxCompression)*planet.staticRY)
        newRY = planet.cy-planet.littleCircles[0].radius
        planet.ry = newRY
        if planet.vy < -10:
            planet.vy = planet.collisionYV+ratio*(planet.staticRY-newRY)
        else:
            planet.vy = -(planet.collisionYV+ratio*(planet.staticRY-newRY))

def checkInnerParticles(planet, data):
    for particle in planet.innerParticles:
        particle.cx += (planet.vx+particle.vx)*data.timerDelay / 1000
        particle.cy += (planet.vy+particle.vy)*data.timerDelay / 1000
        h = planet.cx
        k = planet.cy
        a = planet.rx-planet.littleCircles[0].radius-particle.radius
        b = planet.ry-planet.littleCircles[0].radius-particle.radius
        determinant = ellipseDeterminant(particle.cx,particle.cy,h,k,a,b)
        if determinant >= 1:
            nx = particle.cx-planet.cx
            ny = particle.cy-planet.cy
            dot_n_v = nx*particle.vx+ny*particle.vy
            if dot_n_v > 0:
                nv_x = dot_n_v/(nx**2+ny**2)*nx
                nv_y = dot_n_v/(nx**2+ny**2)*ny
                tv_x = particle.vx-nv_x
                tv_y = particle.vy-nv_y
                particle.vx = -nv_x+tv_x
                particle.vy = -nv_y+tv_y
            x0 = nx
            y0 = ny
            x = a*b*x0 / math.sqrt(a*a*y0*y0 + b*b*x0*x0) + planet.cx
            y = a*b*y0 / math.sqrt(a*a*y0*y0 + b*b*x0*x0) + planet.cy
            particle.cx = x
            particle.cy = y

def timerFired(data):
    planet = data.planet
    planet.cx += planet.vx*data.timerDelay / 1000
    planet.cy += planet.vy*data.timerDelay / 1000
    planet.angle += planet.av*data.timerDelay / 1000
    if planet.av > 0:
        planet.av -= planet.ad * data.timerDelay / 1000
        planet.av = max(0, planet.av)
    elif planet.av < 0:
        planet.av += planet.ad * data.timerDelay / 1000
        planet.av = min(0, planet.av)
    planetLeft = planet.cx - planet.staticRX - planet.littleCircles[0].radius
    planetRight = planet.cx + planet.staticRX + planet.littleCircles[0].radius
    if planetLeft >= 0 and planetRight <= data.width:
        sideNoCollision(planet, data, planetLeft, planetRight)
    else:
        sideHasCollions(planet, data, planetLeft, planetRight)
    planetTop = planet.cy - planet.staticRY - planet.littleCircles[0].radius
    planetBottom = planet.cy + planet.staticRY + planet.littleCircles[0].radius
    if planetTop >= 0 and planetBottom <= data.height:
        vertNoCollision(planet, data, planetTop, planetBottom)
    else:
        verHasCollision(planet, data, planetTop, planetBottom)
    
    checkInnerParticles(planet, data)

    ##inner particles
    
##############Motion Helpers#################
def updateMouseDeterminant(planet, milli_sec, event, data):
    planet.lastMouseTime = milli_sec
    planet.lastMouseX = event.x
    planet.lastMouseY = event.y
    a = planet.rx+planet.littleCircles[0].radius
    b = planet.ry+planet.littleCircles[0].radius
    x = planet.lastMouseX
    y = planet.lastMouseY
    h = planet.cx
    k = planet.cy
    planet.lastMouseDeterminant = ellipseDeterminant(x,y,h,k,a,b)
    return

def updateVXVY(planet, data, nv_x, nv_y):
    newVX = planet.vx + nv_x * planet.mousePlanetVelocityRatio
    if newVX > planet.maxV:
        newVX = planet.maxV
    elif newVX < -planet.maxV:
        newVX = - planet.maxV
    newVY = planet.vy + nv_y * planet.mousePlanetVelocityRatio
    if newVY > planet.maxV:
        newVY = planet.maxV
    elif newVY < - planet.maxV:
        newVY = - planet.maxV
    planet.vx = newVX
    planet.vy = newVY

def calcDeterminant(planet, event, data, dt):
    dx = event.x - planet.lastMouseX
    dy = event.y - planet.lastMouseY
    vx = round(dx * 1000 / dt)
    vy = round(dy * 1000 / dt)
    h = planet.cx
    k = planet.cy
    a = planet.rx+planet.littleCircles[0].radius
    b = planet.ry+planet.littleCircles[0].radius
    determinant = ellipseDeterminant(event.x,event.y,h,k,a,b)
    return (determinant, dx, dy, vx, vy)
        
def updateLastDeterminant(planet, milli_sec, event, data):
    planet.lastMouseTime = milli_sec
    planet.lastMouseX = event.x
    planet.lastMouseY = event.y
    a = planet.rx+planet.littleCircles[0].radius
    b = planet.ry+planet.littleCircles[0].radius
    x = planet.lastMouseX
    y = planet.lastMouseY
    h = planet.cx
    k = planet.cy
    planet.lastMouseDeterminant = ellipseDeterminant(x,y,h,k,a,b)

def motion(event, data):
    planet = data.planet
    milli_sec = time.time() * 1000  
    if planet.lastMouseTime == 0:
        updateMouseDeterminant(planet, milli_sec, event, data)      
    dt = milli_sec - planet.lastMouseTime  
    if dt > 0:
        result = calcDeterminant(planet, event, data, dt)
        determinant, dx, dy, vx, vy = result[0], result[1], result[2], result[3], result[4]
        if planet.lastMouseDeterminant >= 1 and determinant < 1:  
            nx = planet.cx - planet.lastMouseX 
            ny = planet.cy - planet.lastMouseY
            dot_n_v = nx * vx + ny * vy
            if dot_n_v > 0:
                nv_x = dot_n_v/(nx**2+ny**2)*nx
                nv_y = dot_n_v/(nx**2+ny**2)*ny
                tv_x = vx - nv_x
                tv_y = vy - nv_y
                inCollisionX = planet.inCollisionX
                inCollisionY = planet.inCollisionY
                if inCollisionX == False and inCollisionY == False:
                    updateVXVY(planet, data, nv_x, nv_y)           
                cross_n_tv = tv_x * ny - tv_y * nx
                tv_m = math.sqrt(tv_x * tv_x + tv_y * tv_y)
                if cross_n_tv > 0:
                    aRadius = (planet.rx+planet.ry)/2
                    newAV = planet.av+tv_m/aRadius*planet.mousePlanetAVRatio
                    planet.av = min(planet.maxAngleVelocity, newAV)
                elif cross_n_tv < 0:
                    aRadius = (planet.rx+planet.ry)/2
                    newAV = planet.av-tv_m/aRadius*planet.mousePlanetAVRatio
                    planet.av = max(-planet.maxAngleVelocity, newAV)
        updateLastDeterminant(planet, milli_sec, event, data)
        

def redrawAll(canvas, data):
    planet = data.planet
    planet.drawParticles(canvas)
    planet.drawLittleCircles(canvas, data)
     
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
                                fill='black', width=0)
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
       ## redrawAllWrapper(canvas, data)

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

#run(800, 600)