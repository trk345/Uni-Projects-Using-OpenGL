from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500, 500

dropx1, dropy1 = 0, 220
dropx2, dropy2 = 0, 250
raindrops = [[0,250,0,220], [30,220,30,190], [-50,260,-50,230], [70,170,70,140],
             [-80,220,-80,190], [120,100,120,70], [-150,120,-150,90], [200,30,200,0],
             [-225,40,-225,10], [-210,90,-210,60], [220,55,220,25], [150,230,150,200],
             [-125,200,-125,170], [-190,200,-190,170],] #[[x2,y2,x1,y1]]
speed_2 = 0.05
dark = 0.0
key_count = 0

def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b


# def draw_house(dark, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5,
#                 x6, y6, x7, y7, x8, y8, x9, y9, x10, y10,
#                 x11, y11, x12, y12, x13, y13, x14, y14, x15, y15,
#                 x16, y16, x17, y17, x18, y18, x19, y19, x20, y20,
#                ):
def draw_house(dark, x1=-150, y1=50, x2=0, y2=100, x3=150, y3=50,
                x4=-135, y4=50, x5=-135, y5=-100, x6=135, y6=50, x7=135, y7=-100,
                x8=-75, y8=-10, x9=-75, y9=-100, x10=-30, y10=-10, x11=-30, y11=-100,
                x12=-40, y12=-65,
                x13=30, y13=15, x14=30, y14=-25, x15=75, y15=15, x16=75, y16=-25,
                x17=52.5, y17=15, x18=52.5, y18=-25, x19=30, y19=-5, x20=75, y20=-5,):
    glColor3f(dark, dark, dark)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel, start roof from here
    glVertex2f(x2,y2)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x1, y1)
    glVertex2f(x3, y3) #end roof here
    glVertex2f(x4, y4) #start house body here
    glVertex2f(x5, y5)
    glVertex2f(x6, y6)
    glVertex2f(x7, y7)
    glVertex2f(x5-5, y5)
    glVertex2f(x7+5, y7)
    glEnd() #end house body here
    #start door
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x8, y8)
    glVertex2f(x9, y9)
    glVertex2f(x10, y10)
    glVertex2f(x11, y11)
    glVertex2f(x8, y8)
    glVertex2f(x10, y10)
    glEnd()
    glPointSize(3)
    glBegin(GL_POINTS) #for doorknob
    glVertex2f(x12, y12)
    glEnd() #end door

    glLineWidth(2) #window outline
    glBegin(GL_LINES)
    glVertex2f(x13, y13)
    glVertex2f(x14, y14)
    glVertex2f(x15, y15)
    glVertex2f(x16, y16)
    glVertex2f(x13, y13)
    glVertex2f(x15, y15)
    glVertex2f(x14, y14)
    glVertex2f(x16, y16)
    glEnd()
    glLineWidth(1)  # window grid
    glBegin(GL_LINES)
    glVertex2f(x17, y17)
    glVertex2f(x18, y18)
    glVertex2f(x19, y19)
    glVertex2f(x20, y20)
    glEnd()

def draw_rain(rain, x):
    glLineWidth(1)
    glColor3f(x,x,x)
    glBegin(GL_LINES)
    # glVertex2f(x1, y1)
    # glVertex2f(x2, y2)
    for i in range(len(rain)):
        glVertex2f(rain[i][0], rain[i][1])
        glVertex2f(rain[i][2], rain[i][3])
    glEnd()

def keyboardListener(key, x, y):
    global raindrops, dark

    if key == b'd':
        if dark <= 1:
            dark += 0.05
            draw_rain(raindrops, dark)
            draw_house(dark, )
            print('darkened')

    if key==b'b':
        if dark >= 0:
            dark -= 0.05
            print('brightened')
            draw_rain(raindrops, dark)

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global key_count
    if key == GLUT_KEY_RIGHT:
        if key_count <= 4:
            key_count += 1
            for i in range(len(raindrops)):
                if raindrops[i][0]-raindrops[i][2] == 0 or abs((raindrops[i][1]-raindrops[i][3])/(raindrops[i][0]-raindrops[i][2])) >= 1: #theta>=45degrees
                    raindrops[i][0] += 1.0
                    raindrops[i][1] -= 1.0
                    raindrops[i][2] -= 1.0
                    raindrops[i][3] += 1.0
    if key == GLUT_KEY_LEFT:
        if key_count >= -4:
            key_count -= 1
            for i in range(len(raindrops)):
                if raindrops[i][0] - raindrops[i][2] == 0 or abs((raindrops[i][1] - raindrops[i][3]) / (raindrops[i][0] - raindrops[i][2])) >= 1:  # theta<=45degrees
                    raindrops[i][0] -= 1.0
                    raindrops[i][1] -= 1.0
                    raindrops[i][2] += 1.0
                    raindrops[i][3] += 1.0
    glutPostRedisplay()

def display():
    # //clear the display
    global dark
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0-dark, 1.0-dark, 1.0-dark, 1.0-dark)
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
    glMatrixMode(GL_MODELVIEW)

    # draw_house(-150, 50, 0, 100, 150, 50, #roof
    #             -135, 50, -135, -100, 135, 50, 135, -100, #house_body
    #             -75, -10, -75, -100, -30, -10, -30, -100, #door
    #             -40, -65, #doorknob
    #             30, 15, 30, -25, 75, 15, 75, -25,#window
    #             52.5, 15, 52.5, -25, 30, -5, 75, -5, #window_grid
    #             )
    global dropx1, dropy1, dropx2, dropy2, raindrops
    draw_house(dark)
    # draw_rain(dropx1, dropy1, dropx2, dropy2)
    draw_rain(raindrops, dark)

    glutSwapBuffers()


def animate():
    # //codes for any changes in Models, Camera
    glutPostRedisplay()
    global dropy1, dropy2, speed_2, raindrops

    for i in range(len(raindrops)):
        if 0<=raindrops[i][3]<=0.1:  #y2<=0.1
            raindrops[i][1] = 250    #y2=250
            raindrops[i][3] = 220    #y1=220
        else:
            raindrops[i][1] = (raindrops[i][1]-speed_2)%250
            raindrops[i][3] = (raindrops[i][3]-speed_2)%220


def init():
    # //clear the screen
    glClearColor(1.0, 1.0, 1.0, 1.0)
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
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()  # The main loop of OpenGL
