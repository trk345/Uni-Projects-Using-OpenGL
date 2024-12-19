from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random

W_Width, W_Height = 500, 500


score = 0
speed = 1.0
pause = False
bucketx1,bucketx2,bucketx3,bucketx4 = -60,60,-45,45
lost = False
diamondx = random.uniform(-240,240)
diamondy1,diamondy2,diamondy3,diamondy4 = 250,235,235,220
diamondc1,diamondc2,diamondc3= random.random(),random.random(),random.random()
if diamondc1 <= 0.4 or diamondc2 <= 0.4 or diamondc3 <=0.4:
    diamondc1 += 0.5
    diamondc2 += 0.6
    diamondc3 += 0.1

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b

def draw_points(x, y, s, c1, c2, c3):
    glColor3f(c1,c2,c3)
    glPointSize(s)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()

def findzone(x1,y1,x2,y2):
    dy = y2 - y1
    dx = x2 - x1
    if abs(dy) > abs(dx):
        if dy>0 and dx>=0:
            return 1
        elif dy>0 and dx<=0:
                return 2
        elif dy<0 and dx<=0:
                return 5
        else:
            return 6
    else:
        if dy>=0 and dx>0:
            return 0
        elif dy>=0 and dx<0:
                return 3
        elif dy<=0 and dx<0:
                return 4
        else:
            return 7


def drawline(x1,y1,x2,y2,s,c1,c2,c3):
    zone = findzone(x1,y1,x2,y2)
    # print(zone)
    if zone == 0:
        x1,x2 = x1,x2
        y1,y2 = y1,y2
    elif zone == 1:
        temp1,temp2 = x1,x2
        x1,x2 = y1,y2
        y1,y2 = temp1,temp2
    elif zone == 2:
        temp1,temp2 = x1,x2
        x1,x2 = y1,y2
        y1,y2 = -temp1,-temp2
    elif zone == 3:
        x1,x2 = -x1,-x2
        y1,y2 = y1,y2
    elif zone == 4:
        x1,x2 = -x1,-x2
        y1,y2 = -y1,-y2
    elif zone == 5:
        temp1,temp2 = x1,x2
        x1,x2 = -y1,-y2
        y1,y2 = -temp1,-temp2
    elif zone == 6:
        temp1, temp2 = x1, x2
        x1,x2 = -y1,-y2
        y1,y2 = temp1,temp2
    else:
        x1, x2 = x1, x2
        y1, y2 = -y1, -y2

    dx = x2 - x1
    dy = y2 - y1

    coordinates = []
    d  = 2*dy - dx
    incE   = 2*dy
    incNE = 2*(dy - dx)

    for x in range(int(x1),int(x2+1)):
        coordinates.append([x,y1])
        if d>0:
            d = d + incNE
            # x += 1
            y1 += 1
        else:
            # x += 1
            d = d + incE
    for i in range(len(coordinates)):
        if zone == 0:
            x = coordinates[i][0]
            y = coordinates[i][1]
        elif zone == 1:
            x = coordinates[i][1]
            y = coordinates[i][0]
        elif zone == 2:
            x = -coordinates[i][1]
            y = coordinates[i][0]
        elif zone == 3:
            x = -coordinates[i][0]
            y = coordinates[i][1]
        elif zone == 4:
            x = -coordinates[i][0]
            y = -coordinates[i][1]
        elif zone == 5:
            x = -coordinates[i][1]
            y = -coordinates[i][0]
        elif zone == 6:
            x = coordinates[i][1]
            y = -coordinates[i][0]
        elif zone == 7:
            x = coordinates[i][0]
            y = -coordinates[i][1]

        draw_points(x,y,s,c1,c2,c3)

def navbar():
    #backarrow
    drawline(-235, 230, -220, 245, 2, 0.1, 0.7, 0.8)
    drawline(-235, 230, -220, 215, 2, 0.1, 0.7, 0.8)
    drawline(-235, 230, -205, 230, 2, 0.1, 0.7, 0.8)

    # glLineWidth(2)
    # glBegin(GL_LINES)
    # glColor3f(0.1, 0.7, 0.8)
    # glVertex2f(-235, 230)
    # glVertex2f(-220, 245)
    # glVertex2f(-235, 230)
    # glVertex2f(-220, 215)
    # glVertex2f(-235, 230)
    # glVertex2f(-205, 230)
    # glEnd()
    #play/pause
    if pause == True:
        drawline(-10, 245, -10, 215, 2, 0.9, 0.7, 0.0)
        drawline(-10, 245, 20, 230, 2, 0.9, 0.7, 0.0)
        drawline(-10, 215, 20, 230, 2, 0.9, 0.7, 0.0)
        # glLineWidth(2)
        # glBegin(GL_LINES)
        # glColor3f(0.9, 0.7, 0.0)
        # glVertex2f(-10, 245)
        # glVertex2f(-10, 215)
        # glVertex2f(-10, 245)
        # glVertex2f(20, 230)
        # glVertex2f(-10, 215)
        # glVertex2f(20, 230)
        # glEnd()
    else:
        drawline(-5, 245, -5, 215, 2, 0.9, 0.7, 0.0)
        drawline(5, 245, 5, 215, 2, 0.9, 0.7, 0.0)
        # glLineWidth(2)
        # glBegin(GL_LINES)
        # glColor3f(0.9, 0.7, 0.0)
        # glVertex2f(-5, 245)
        # glVertex2f(-5, 215)
        # glVertex2f(5, 245)
        # glVertex2f(5, 215)
        # glEnd()
    #cross
    drawline(205, 245, 235, 215, 2, 1.0, 0.0, 0.0)
    drawline(205, 215, 235, 245, 2, 1.0, 0.0, 0.0)
    # glLineWidth(2)
    # glBegin(GL_LINES)
    # glColor3f(1.0, 0.0, 0.0)
    # glVertex2f(205, 245)
    # glVertex2f(235, 215)
    # glVertex2f(205, 215)
    # glVertex2f(235, 245)
    # glEnd()

def draw_bucket(y1,y2,y3,y4):
    global bucketx1,bucketx2,bucketx3,bucketx4,bucketred,lost
    x1,x2,x3,x4 = bucketx1,bucketx2,bucketx3,bucketx4
    if lost == False:
        c1, c2, c3 = 1.0, 1.0, 1.0
    else:
        c1, c2, c3 = 1.0, 0.0, 0.0
    drawline(x1, y1, x2, y2, 2, c1, c2, c3)
    drawline(x1, y1, x3, y3, 2, c1, c2, c3)
    drawline(x2, y2, x4, y4, 2, c1, c2, c3)
    drawline(x3, y3, x4, y4, 2, c1, c2, c3)
    # glLineWidth(2)
    # glBegin(GL_LINES)
    #
    # glVertex2f(x1, y1)
    # glVertex2f(x2,y2)
    # glVertex2f(x1, y1)
    # glVertex2f(x3, y3)
    # glVertex2f(x2, y2)
    # glVertex2f(x4, y4)
    # glVertex2f(x3, y3)
    # glVertex2f(x4, y4)
    # glEnd()

def diamond():
    global diamondx, diamondy1, diamondy2, diamondy3, diamondy4, diamondc1, diamondc2, diamondc3
    x1 = diamondx
    x2 = diamondx-10
    x3 = diamondx+10
    x4 = diamondx
    y1,y2,y3,y4 = diamondy1,diamondy2,diamondy3,diamondy4
    drawline(x1, y1, x2, y2, 2, diamondc1, diamondc2, diamondc3)
    drawline(x1, y1, x3, y3, 2, diamondc1, diamondc2, diamondc3)
    drawline(x2, y2, x4, y4, 2, diamondc1, diamondc2, diamondc3)
    drawline(x3, y3, x4, y4, 2, diamondc1, diamondc2, diamondc3)
    # glLineWidth(2)
    # glBegin(GL_LINES)
    # glColor3f(diamondc1, diamondc2, diamondc3)
    # glVertex2f(x1, y1)
    # glVertex2f(x2, y2)
    # glVertex2f(x1, y1)
    # glVertex2f(x3, y3)
    # glVertex2f(x2, y2)
    # glVertex2f(x4, y4)
    # glVertex2f(x3, y3)
    # glVertex2f(x4, y4)
    # glEnd()

def keyboardListener(key, x, y):

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global speed, bucketx1, bucketx2, bucketx3, bucketx4
    glutPostRedisplay()
    if key==GLUT_KEY_RIGHT and pause == False and lost == False:
        if bucketx2 <= 250:
            bucketx1 += 4
            bucketx2 += 4
            bucketx3 += 4
            bucketx4 += 4

    if key==GLUT_KEY_LEFT and pause == False and lost == False:
        if bucketx1 >= -250:
            bucketx1 -= 4
            bucketx2 -= 4
            bucketx3 -= 4
            bucketx4 -= 4
    # if key==GLUT_KEY_PAGE_UP:

    # if key==GLUT_KEY_PAGE_DOWN:

    # case GLUT_KEY_INSERT:
    #
    #
    # case GLUT_KEY_HOME:
    #
    # case GLUT_KEY_END:
    #


def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    global speed,score,pause,lost,bucketx1,bucketx2,bucketx3,bucketx4,diamondx,diamondy1,diamondy2,diamondy3,diamondy4,diamondc1,diamondc2,diamondc3
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            c_x, c_y = convert_coordinate(x, y)
            if -235<=c_x<=-205 and 215<=c_y<=245:
                lost = False
                score = 0
                speed = 1
                print("Starting over!")
                draw_bucket(-235, -235, -250, -250)
                bucketx1,bucketx2,bucketx3,bucketx4 = -60,60,-45,45
                diamondx = random.uniform(-240, 240)
                diamondy1, diamondy2, diamondy3, diamondy4 = 250, 235, 235, 220
                diamondc1, diamondc2, diamondc3 = random.random(), random.random(), random.random()
                if diamondc1 <= 0.4 or diamondc2 <= 0.4 or diamondc3 <= 0.4:
                    diamondc1 += 0.5
                    diamondc2 += 0.6
                    diamondc3 += 0.1

            elif -10<=c_x<=20 and 215<=c_y<=245:
                if pause == False:
                    pause = True
                else:
                    pause = False
            elif 205<=c_x<=235 and 215<=c_y<=245:
                print(f"Goodbye! Score: {score}")
                glutLeaveMainLoop()

    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()


def display():
    # //clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)  # //color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # //load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    # //initialize the matrix
    glLoadIdentity()
    # //now give three info
    # //1. where is the camera (viewer)?
    # //2. where is the camera looking?
    # //3. Which direction is the camera's UP direction?
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    # glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

    navbar()
    draw_bucket(-235, -235, -250, -250)
    diamond()
    glutSwapBuffers()


def animate():
    # //codes for any changes in Models, Camera
    glutPostRedisplay()
    global score,speed,pause,lost,diamondx,diamondy1,diamondy2,diamondy3,diamondy4,diamondc1,diamondc2,diamondc3,bucketx1,bucketx2
    if pause == False and lost == False:
        if diamondy4 >= -249.5:
            diamondy1 = (diamondy1 - speed)
            diamondy2 = (diamondy2 - speed)
            diamondy3 = (diamondy3 - speed)
            diamondy4 = (diamondy4 - speed)
            if bucketx1<=diamondx-10<=bucketx2 or bucketx1<=diamondx+10<=bucketx2:
                if -236<=diamondy2<=-235 or -236<=diamondy3<=-235 or -236<=diamondy4<=-235:
                    score += 1
                    speed += 0.01
                    diamondy1 = 250
                    diamondy2 = 235
                    diamondy3 = 235
                    diamondy4 = 220
                    print(f"Score: {score}")
                    diamondx = random.uniform(-240, 240)
                    diamondc1, diamondc2, diamondc3 = random.random(), random.random(), random.random()
                    if diamondc1 <= 0.2 and diamondc2 <= 0.2 and diamondc3 <= 0.2:
                        diamondc1 += 0.4
                        diamondc2 += 0.4
                        diamondc3 += 0.4
        else:
            lost = True
            diamondc1, diamondc2, diamondc3 = 0.0,0.0,0.0
            print(f"Game Over! Score: {score}")

def init():
    # //clear the screen
    glClearColor(0, 0, 0, 0)
    # //load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    # //initialize the matrix
    glLoadIdentity()
    # //give PERSPECTIVE parameters
    gluPerspective(104, 1, 1, 1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    # //near distance
    # //far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Catching Diamonds")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()  # The main loop of OpenGL
