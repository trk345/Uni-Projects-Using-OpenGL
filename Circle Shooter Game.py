import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500, 500

pause = False
shooter_r = 12 #shooter radius
shooter_first_call = False
shooter_cd = [] #shooter coordinates, cd[1][0]=x-coord of topmost point, cd[1][1]=y-coord of topmost point
shooter_speed = 8
shooter_moved = 0 #shooter deviation from initial position
fc1_first_call = False #falling circle first call
fc1_cd = [] #falling circle-1 coordinates
fc2_first_call = False
fc2_cd = []
fc3_first_call = False
fc3_cd = []
fc4_first_call = False
fc4_cd = []
fc5_first_call = False
fc5_cd = []
# y1,y2,y3,y4,y5 = 0,0,0,0,0
# x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0
fc_speed = 0.5
bullets = []
bullet_flag = False
bullet_start = [] #list of bullet starting x-coordinates
bullet_speed = 3
bullet_gone = 0
score = 0
circles_fell = 0
lost = False



def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b


def draw_points(x, y, s, c1=1.0, c2=0.8, c3=0.0):
    glPointSize(s)  # pixel size. by default 1 thake
    glColor3f(c1,c2,c3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def draw_circle(r):
    global shooter,shooter_c,shooter_right,shooter_left
    # if shooter == False:
    cd = []
        # shooter = True
    x = r
    y = 0
    d = 1 - r
    while y<=x:
        if d<0:
            d += 2*y + 3
            y += 1
        else:
            d += 2*y - 2*x + 5
            y+=1
            x-=1
            # shooter_c.append([x, y-230])
            # shooter_c.append([y, x-230])
            # shooter_c.append([-y, x-230])
            # shooter_c.append([-x, y-230])
            # shooter_c.append([-x, -y-230])
            # shooter_c.append([-y, -x-230])
            # shooter_c.append([y, -x-230])
            # shooter_c.append([x, -y-230])

        cd.append([x, y])
        cd.append([y, x])
        cd.append([-y, x])
        cd.append([-x, y])
        cd.append([-x, -y])
        cd.append([-y, -x])
        cd.append([y, -x])
        cd.append([x, -y])
    return cd
    # for i in range(len(shooter_c)):
    #     draw_points(shooter_c[i][0],shooter_c[i][1],3)
    # shooter_right = shooter_c[0][0]
    # shooter_left = shooter_c[3][0]

def shooter(r):
    global shooter_first_call,shooter_cd
    if shooter_first_call == False:
        shooter_first_call = True
        shooter_cd = draw_circle(r) #shooter coordinates
    # print(cd)
    if lost == False:
        for i in range(len(shooter_cd)):
            draw_points(shooter_cd[i][0],(shooter_cd[i][1]-230),3)
    else:
        for i in range(len(shooter_cd)):
            draw_points(shooter_cd[i][0],(shooter_cd[i][1]-230),3,1.0,0.0,0.0)

def bullet():
    global bullets,bullet_flag
    if bullet_flag == True:
        bullet_flag = False
        cd = draw_circle(5)
        # print(f'top-bottom:{cd[1][1]-cd[5][1]}')
        # print(f'right-left:{cd[0][0] - cd[3][0]}')
        bullets.append(cd)
        for i in range(len(bullets[-1])):
            bullets[-1][i][0] += bullet_start[-1]
            bullets[-1][i][1] -= 210
        # for i in range(len(bullets)):
        #     for j in range(len(bullets[i])):
        #         bullets[i][j][0] += bullet_start[i]
        #         bullets[i][j][1] -= 210
                # draw_points(bullets[i][j][0] + bullet_start[i], bullets[i][j][1] - 210, 3)
    for i in range(len(bullets)):
        for j in range(len(bullets[i])):
            draw_points(bullets[i][j][0],bullets[i][j][1],3)

        # print(f'bullet:{bullets[i][3][0], bullets[i][0][0]}')
        # print(f'fc1:{fc1_cd[3][0],fc1_cd[0][0]}')
        # print(f'fc2:{fc2_cd[3][0], fc2_cd[0][0]}')
        # print(f'fc3:{fc3_cd[3][0], fc3_cd[0][0]}')
        # print(f'fc4:{fc4_cd[3][0], fc4_cd[0][0]}')
        # print(f'fc5:{fc5_cd[3][0], fc5_cd[0][0]}')

def falling_circles():
    global fc1_first_call,fc1_cd,fc2_first_call,fc2_cd,fc3_first_call,fc3_cd
    global fc4_first_call,fc4_cd,fc5_first_call,fc5_cd,x1,x2,x3,x4,x5,y1,y2,y3,y4,y5
    if fc1_first_call == False:
        fc1_first_call = True
        fc1_cd = draw_circle(random.randrange(15,25))  #falling circle coordinates
        # print(f'top-bottom:{fc1_cd[1][1]-fc1_cd[5][1]}')
        # print(f'right-left:{fc1_cd[0][0] - fc1_cd[3][0]}')
        x1 = random.randrange(-210,210)
        # y1 = 240
        y1 = random.randrange(280,420)
        for i in range(len(fc1_cd)):
            fc1_cd[i][0]+=x1
            fc1_cd[i][1]+=y1
    for i in range(len(fc1_cd)):
        draw_points(fc1_cd[i][0], fc1_cd[i][1], 3)
    if fc2_first_call == False:
        fc2_first_call = True
        fc2_cd = draw_circle(random.randrange(15,30))
        x2 = random.randrange(-210, 210)
        # y2 = 290
        y2 = random.randrange(280, 420)
        # while y2==y1+20 or y2==y1-20:
        #     y2 = random.randrange(250, 290)
        # while abs(x2-x1)!=20:
        #     x2=random.randrange(-210,210)
        for i in range(len(fc2_cd)):
            fc2_cd[i][0] += x2
            fc2_cd[i][1] += y2
    for i in range(len(fc2_cd)):
        draw_points(fc2_cd[i][0], fc2_cd[i][1], 3)
    if fc3_first_call == False:
        fc3_first_call = True
        fc3_cd = draw_circle(random.randrange(15,30))
        x3 = random.randrange(-210, 210)
        # y3 = 340
        y3 = random.randrange(280, 420)
        # while abs(x3-x1)!=20 or abs(x3-x2)!=20:
        #     x3=random.randrange(-210,210)
        # while y3==y1+20 or y3==y1-20 or y3==y2+20 or y3==y2-20:
        #     y3 = random.randrange(250, 290)
        for i in range(len(fc3_cd)):
            fc3_cd[i][0] += x3
            fc3_cd[i][1] += y3
    for i in range(len(fc3_cd)):
        draw_points(fc3_cd[i][0], fc3_cd[i][1], 3)
    if fc4_first_call == False:
        fc4_first_call = True
        fc4_cd = draw_circle(random.randrange(15,30))
        x4 = random.randrange(-210, 210)
        # y4 = 390
        y4 = random.randrange(280, 420)
        # while ab
        # s(x4-x1)!=20 or abs(x4-x2)!=20 or abs(x4-x3)!=20:
        #     x4=random.randrange(-210,210)
        # while y4==y1+20 or y4==y1-20 or y4==y2+20 or y4==y2-20 or y4==y3+20 or y4==y3-20:
        #     y4 = random.randrange(250, 290)
        for i in range(len(fc4_cd)):
            fc4_cd[i][0] += x4
            fc4_cd[i][1] += y4
    for i in range(len(fc4_cd)):
        draw_points(fc4_cd[i][0], fc4_cd[i][1], 3)
    if fc5_first_call == False:
        fc5_first_call = True
        fc5_cd = draw_circle(random.randrange(15,30))
        x5 = random.randrange(-210, 210)
        # y5 = 440
        y5 = random.randrange(280, 420)
        # while abs(x5-x1)!=20 or abs(x5-x2)!=20 or abs(x5-x3)!=20 or abs(x5-x4)!=20:
        #     x5=random.randrange(-210,210)
        # while y5==y1+20 or y5==y1-20 or y5==y2+20 or y5==y2-20 or y5==y3+20 or y5==y3-20 or y5==y4+20 or y5==y4-20:
        #     y5 = random.randrange(250, 290)
        for i in range(len(fc5_cd)):
            fc5_cd[i][0] += x5
            fc5_cd[i][1] += y5
    for i in range(len(fc5_cd)):
        draw_points(fc5_cd[i][0], fc5_cd[i][1], 3)
    # for i in range(len(fc1_cd)):
    #     draw_points(fc1_cd[i][0],(fc1_cd[i][1]),3)
    # for i in range(len(fc2_cd)):
    #     draw_points(fc2_cd[i][0], (fc2_cd[i][1]), 3)
        # draw_points(fc3_cd[i][0], (fc3_cd[i][1]), 3)
        # draw_points(fc4_cd[i][0], (fc4_cd[i][1]), 3)
        # draw_points(fc5_cd[i][0], (fc5_cd[i][1]), 3)


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
        # draw_points(x,y,s)

def navbar():
    #backarrow
    drawline(-235, 230, -220, 245, 2, 0.1, 0.7, 0.8)
    drawline(-235, 230, -220, 215, 2, 0.1, 0.7, 0.8)
    drawline(-235, 230, -205, 230, 2, 0.1, 0.7, 0.8)
    # play/pause
    if pause == True:
        drawline(-10, 245, -10, 215, 2, 0.9, 0.7, 0.0)
        drawline(-10, 245, 20, 230, 2, 0.9, 0.7, 0.0)
        drawline(-10, 215, 20, 230, 2, 0.9, 0.7, 0.0)
    else:
        drawline(-5, 245, -5, 215, 2, 0.9, 0.7, 0.0)
        drawline(5, 245, 5, 215, 2, 0.9, 0.7, 0.0)
    # cross
    drawline(205, 245, 235, 215, 2, 1.0, 0.0, 0.0)
    drawline(205, 215, 235, 245, 2, 1.0, 0.0, 0.0)




def keyboardListener(key, x, y):
    global shooter_cd,shooter_moved,bullet_flag,pause,lost
    if pause == False and lost == False:
        if key == b'd': #move right
            if shooter_cd[0][0]+shooter_speed <= 250:
                for i in range(len(shooter_cd)):
                    shooter_cd[i][0] += shooter_speed
                shooter_moved += shooter_speed

        if key == b'a':
            if shooter_cd[3][0]-shooter_speed >= -250:
                for i in range(len(shooter_cd)):
                    shooter_cd[i][0] -= shooter_speed
                shooter_moved -= shooter_speed

        if key == b' ':
            bullet_flag = True
            bullet_start.append(shooter_moved)
            # print(bullet_start)
            bullet()
    # if key==b's':
    #    print(3)
    # if key==b'd':
    #     print(4)

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    # global
    if key == 'w':
        print(1)
    if key == GLUT_KEY_UP:
        # speed *= 2
        print("Speed Increased")
    if key == GLUT_KEY_DOWN:  # // up arrow key
        # speed /= 2
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
    global pause,lost,shooter_r,shooter_first_call,shooter_moved,fc1_first_call,fc2_first_call
    global fc3_first_call,fc4_first_call,fc5_first_call,circles_fell,score,bullets,bullet_flag,bullet_start
    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):  # // 2 times?? in ONE click? -- solution is checking DOWN or UP
            # print(x, y)
            c_x, c_y = convert_coordinate(x, y)
            if -235<=c_x<=-205 and 215<=c_y<=245: #start over button
                score = 0
                circles_fell = 0
                print("Starting over!")
                # shooter(shooter_r)
                shooter_first_call = False
                shooter_moved = 0
                fc1_first_call = False
                fc2_first_call = False
                fc3_first_call = False
                fc4_first_call = False
                fc5_first_call = False
                bullets = []
                bullet_flag = False
                bullet_start = []
                pause = False
                lost = False
            elif -10<=c_x<=20 and 215<=c_y<=245: #pause button
                if pause == False:
                    pause = True
                else:
                    pause = False
            elif 205<=c_x<=235 and 215<=c_y<=245: #exit button
                print(f"Goodbye! Score: {score}")
                glutLeaveMainLoop()


    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            create_new = convert_coordinate(x, y)
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


    # global
    # drawline(-30,55,100,90,3, 1, 1, 1)
    navbar()
    shooter(shooter_r)
    falling_circles()
    bullet()



    glutSwapBuffers()


def animate():
    # //codes for any changes in Models, Camera
    glutPostRedisplay()
    global fc1_cd,fc1_first_call,fc2_cd,fc2_first_call,fc3_cd,fc3_first_call
    global fc4_cd,fc4_first_call,fc5_cd,fc5_first_call,bullets,bullet_speed,bullet_flag,bullet_start
    global circles_fell,lost,score,bullet_gone

    if pause == False and lost == False:
        for i in range(len(fc1_cd)):
            fc1_cd[i][1] -= fc_speed
        if fc1_cd[3][0]<=shooter_cd[3][0]<=fc1_cd[0][0] or fc1_cd[3][0]<=shooter_cd[0][0]<=fc1_cd[0][0]:
            if fc1_cd[5][1]<=-230:
                lost = True
                # print('you lost')
        # if lost == False:
        if fc1_cd[5][1]<=-255:
            circles_fell+=1
            # print(circles_fell)
            if circles_fell==3:
                lost = True
            fc1_first_call = False
        if lost == False:
            for i in range(len(fc2_cd)):
                fc2_cd[i][1] -= fc_speed
            if fc2_cd[3][0]<=shooter_cd[3][0]<=fc2_cd[0][0] or fc2_cd[3][0]<=shooter_cd[0][0]<=fc2_cd[0][0]:
                if fc2_cd[5][1] <= -230:
                    lost = True
            if fc2_cd[5][1]<=-255:
                circles_fell+=1
                if circles_fell==3:
                    lost = True
                # print(circles_fell)
                fc2_first_call = False
            if lost == False:
                for i in range(len(fc3_cd)):
                    fc3_cd[i][1] -= fc_speed
                if fc3_cd[3][0]<=shooter_cd[3][0]<=fc3_cd[0][0] or fc3_cd[3][0]<=shooter_cd[0][0]<=fc3_cd[0][0]:
                    if fc3_cd[5][1] <= -230:
                        lost = True
                if fc3_cd[5][1]<=-255:
                    circles_fell+=1
                    if circles_fell==3:
                        lost = True
                    # print(circles_fell)
                    fc3_first_call = False
                if lost == False:
                    for i in range(len(fc4_cd)):
                        fc4_cd[i][1] -= fc_speed
                    if fc4_cd[3][0]<=shooter_cd[3][0]<=fc4_cd[0][0] or fc4_cd[3][0]<=shooter_cd[0][0]<=fc4_cd[0][0]:
                        if fc4_cd[5][1] <= -230:
                            lost = True
                    if fc4_cd[5][1]<=-255:
                        circles_fell+=1
                        if circles_fell==3:
                            lost = True
                        # print(circles_fell)
                        fc4_first_call = False
                    if lost == False:
                        for i in range(len(fc5_cd)):
                            fc5_cd[i][1] -= fc_speed
                        if fc5_cd[3][0]<=shooter_cd[3][0]<=fc5_cd[0][0] or fc5_cd[3][0]<=shooter_cd[0][0]<=fc5_cd[0][0]:
                            if fc5_cd[5][1] <= -230:
                                lost = True
                        if fc5_cd[5][1]<=-255:
                            circles_fell+=1
                            if circles_fell==3:
                                lost = True
                            # print(circles_fell)
                            fc5_first_call = False

        for i in range(len(bullets)):
            for j in range(len(bullets[i])):
                bullets[i][j][1] += bullet_speed
            if bullets[i][1][1]>=250:
                bullet_gone += 1
                # print('yeet')         #bonus task
                bullets.pop(i)
                bullet_start.pop(i)
                if bullet_gone == 3:
                    lost = True
                    bullet_gone = 0
                break
            if fc1_cd[3][0]<=bullets[i][3][0]<=fc1_cd[0][0] or fc1_cd[3][0]<=bullets[i][0][0]<= fc1_cd[0][0]:
                # print('in1')
                if fc1_cd[5][1]<=bullets[i][1][1]<=fc1_cd[1][1]:
                    # print('fc1')
                    score += 1
                    print(f"Score: {score}")
                    fc1_first_call = False
                    bullets.pop(i)
                    bullet_start.pop(i)
                    break
            if fc2_cd[3][0]<=bullets[i][3][0]<=fc2_cd[0][0] or fc2_cd[3][0]<=bullets[i][0][0]<=fc2_cd[0][0]:
                # print('in2')
                if fc2_cd[5][1]<=bullets[i][1][1]<=fc2_cd[1][1]:
                    # print('fc2')
                    score += 1
                    print(f"Score: {score}")
                    fc2_first_call = False
                    bullets.pop(i)
                    bullet_start.pop(i)
                    break
            if fc3_cd[3][0]<=bullets[i][3][0]<=fc3_cd[0][0] or fc3_cd[3][0]<=bullets[i][0][0]<=fc3_cd[0][0]:
                # print('in3')
                if fc3_cd[5][1]<=bullets[i][1][1]<=fc3_cd[1][1]:
                    # print('fc3')
                    score += 1
                    print(f"Score: {score}")
                    fc3_first_call = False
                    bullets.pop(i)
                    bullet_start.pop(i)
                    break
            if fc4_cd[3][0]<=bullets[i][3][0]<=fc4_cd[0][0] or fc4_cd[3][0]<=bullets[i][0][0]<=fc4_cd[0][0]:
                # print('in4')
                if fc4_cd[5][1]<=bullets[i][1][1]<=fc4_cd[1][1]:
                    # print('fc4')
                    score += 1
                    print(f"Score: {score}")
                    fc4_first_call = False
                    bullets.pop(i)
                    bullet_start.pop(i)
                    break
            if fc5_cd[3][0]<=bullets[i][3][0]<=fc5_cd[0][0] or fc5_cd[3][0]<=bullets[i][0][0]<=fc5_cd[0][0]:
                # print('in5')
                if fc5_cd[5][1]<=bullets[i][1][1]<=fc5_cd[1][1]:
                    # print('fc5')
                    score += 1
                    print(f"Score: {score}")
                    fc5_first_call = False
                    bullets.pop(i)
                    bullet_start.pop(i)
                    break
        if lost == True:
            fc1_cd = []
            fc2_cd = []
            fc3_cd = []
            fc4_cd = []
            fc5_cd = []
            bullets = []
            bullet_flag = False
            bullet_start = []
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
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()  # The main loop of OpenGL
