from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math, random

W_Width, W_Height = 500, 500

speed = 0.01
create_new = False
newpoints = []
point_colors = []
sp_count = 0
spacebar = False


def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b

def create_point(x,y):
    global newpoints, W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    color1 = random.random()
    color2 = random.random()
    color3 = random.random()
    x_sign = random.choice([-1,1])
    y_sign = random.choice([-1,1])
    newpoints.append([a,b,color1,color2,color3,x_sign,y_sign])
    point_colors.append(color1)
    point_colors.append(color2)
    point_colors.append(color3)
    # return a, b, color1, color2, color3

def drawAxes():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(180, 0)
    glVertex2f(0, 0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0, 180)
    glVertex2f(0, 0)
    glEnd()


def keyboardListener(key, x, y):
    global sp_count, spacebar
    if key == b' ':
        sp_count += 1
        if sp_count % 2 != 0:
            spacebar = True
        else:
            spacebar = False

    # if key==b's':
    #    print(3)
    # if key==b'd':
    #     print(4)

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global speed, spacebar
    if spacebar == False:
        if key == GLUT_KEY_UP:
            speed *= 2
            print("Speed Increased")
        if key == GLUT_KEY_DOWN:  # // up arrow key
            speed /= 2
            print("Speed Decreased")

    glutPostRedisplay()
    # if key==GLUT_KEY_RIGHT:

    # if key==GLUT_KEY_LEFT:

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
    global create_new, newpoints, point_colors, spacebar
    if button == GLUT_LEFT_BUTTON and spacebar == False:
        if (state == GLUT_DOWN):  # // 2 times?? in ONE click? -- solution is checking DOWN or UP
            for i in range(len(newpoints)):
                newpoints[i][2], newpoints[i][3], newpoints[i][4] = 0, 0, 0
        if (state == GLUT_UP):
            for i in range(len(newpoints)):
                newpoints[i][2],newpoints[i][3],newpoints[i][4] = point_colors[i],point_colors[i+1],point_colors[i+2]

    if button == GLUT_RIGHT_BUTTON and spacebar == False:
        if state == GLUT_DOWN:
            create_new = create_point(x, y)
            create_new = True
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
    glMatrixMode(GL_MODELVIEW)

    drawAxes()
    global newpoints, spacebar
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2d(180, 0)
    glVertex2d(180, 180)
    glVertex2d(180, 180)
    glVertex2d(0, 180)
    glEnd()

    if (create_new):
        # m, n, c1, c2, c3 = create_new
        for i in range(len(newpoints)):
            glPointSize(10)
            glBegin(GL_POINTS)
            glColor3f(newpoints[i][2],newpoints[i][3],newpoints[i][4])
            glVertex2f(newpoints[i][0], newpoints[i][1])
            glEnd()

    glutSwapBuffers()


def animate():
    # //codes for any changes in Models, Camera
    glutPostRedisplay()
    global speed, newpoints, spacebar
    for i in range(len(newpoints)):
        if spacebar == False:
            if newpoints[i][0] <= 0.07 or newpoints[i][1] <= 0.07:
                newpoints[i][5] *= -1
                newpoints[i][6] *= -1
                newpoints[i][0] = (newpoints[i][0] + (newpoints[i][5] * speed)) % 180
                newpoints[i][1] = (newpoints[i][1] + (newpoints[i][6] * speed)) % 180
                # pass
            else:
                newpoints[i][0] = (newpoints[i][0] + (newpoints[i][5] * speed)) % 180
                newpoints[i][1] = (newpoints[i][1] + (newpoints[i][6] * speed)) % 180
        else:
            newpoints[i][0] = (newpoints[i][0] + (newpoints[i][5]) * 0) % 180
            newpoints[i][1] = (newpoints[i][1] + (newpoints[i][6]) * 0) % 180
        # newpoints[i][0] = (newpoints[i][0] + (1 * speed)) % 180
        # newpoints[i][1] = (newpoints[i][1] + (-1 * speed)) % 180


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
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()  # The main loop of OpenGL
