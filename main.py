import math

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image as Image
import numpy
import time

def get_texture(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    return textID

def inner(bottom, top, height, slices):
    h = height / 2
    points = []
    for i in range(int(slices) + 1):
        angle = 2 * math.pi * (i / slices)
        points.append((bottom * math.cos(angle), bottom * math.sin(angle),
                       top * math.cos(angle), top * math.sin(angle)))
        if i == slices-3:
            points.append((1, 1, 1, 1))
        else:
            points.append((bottom * math.cos(angle), bottom * math.sin(angle),
                           top * math.cos(angle), top * math.sin(angle)))
    # points.pop(2)
    print(points)
    glEnable(GL_TEXTURE_2D)
    # glEnable(GL)


    glBegin(GL_TRIANGLE_FAN)
    # glEnable(GL_TEXTURE_2D)
    # glBindTexture(GL_TEXTURE_2D, texture)
    # glEnable(GL_TEXTURE_GEN_S)
    # glEnable(GL_TEXTURE_GEN_T)
    for (x_bottom, y_bottom, x_top, y_top) in points:
        glNormal(x_bottom, y_bottom, 1)
        # glNormal(0, 0, 1)
        glVertex(x_bottom, y_bottom, -h)

    glEnd()
    glBegin(GL_TRIANGLE_STRIP)
    for (x_bottom, y_bottom, x_top, y_top) in points:
        glNormal(x_top, y_top, 1)
        glVertex(x_top, y_top, h)
        glNormal(x_bottom, y_bottom, 1)
        glVertex(x_bottom, y_bottom, -h)

        # glEnd()
        # glBegin(GL_TRIANGLE_FAN)

    glEnd()

    # glBindTexture(GL_TEXTURE_2D, texture)
    # glEnable(GL_TEXTURE_GEN_S)
    # glEnable(GL_TEXTURE_GEN_T)
    # glBegin(GL_TRIANGLE_FAN)


    # glDisable(GL_TEXTURE_GEN_S)
    # glDisable(GL_TEXTURE_GEN_T)
    # glDisable(GL_TEXTURE_2D)

    glBegin(GL_TRIANGLE_FAN)
    for (x_bottom, y_bottom, x_top, y_top) in points:
        glNormal(x_top, y_top, 1)
        # glNormal(0, 0, 1)
        glVertex(x_top, y_top, h)

    glEnd()





def draw_cube():
    # global texture2
    # glEnable(GL_TEXTURE_2D)
    # # glEnable(GL)
    #
    # # glBindTexture(GL_TEXTURE_2D, texture2)
    # glEnable(GL_TEXTURE_GEN_S)
    # glEnable(GL_TEXTURE_GEN_T)
    glPushMatrix()
    # glTranslatef(8, -0.25, 0)               #1--------------
    glTranslatef(8, -0.2, 0)             #2--------------
    glRotatef(90, 1, 0, 0)
    glBegin(GL_TRIANGLE_FAN)

    # glNormal(-15, -15, 0)
    glVertex(-15, -15, 0)
    # glNormal(-15, 15, 0)
    glVertex(-15, 15, 0)
    # glNormal(15, -15, 0)
    glVertex(15, -15, 0)
    # glNormal(15, 15, 0)
    glVertex(15, 15, 0)
    # glVertex(4, 4, 0)
    glEnd()
    glPopMatrix()
    # glDisable(GL_TEXTURE_GEN_S)
    # glDisable(GL_TEXTURE_GEN_T)
    # glDisable(GL_TEXTURE_2D)

def drawObject():
    global texture
    glEnable(GL_TEXTURE_2D)
    # glEnable(GL)

    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glPushMatrix()
    glTranslatef(-2, 0.1, 3)
    glTranslatef(0.3 * x, 0, 0)
    glTranslatef(0, 0.1 * y, 0)
    #
    # glRotatef(45, 1, 1, 1)
    # glRotatef(-20, 1, 0, 0)
    # glRotatef(-0.5 * 60, 0.5, 1, 0.0)
    glRotatef(-moveRight, 0, 0, 1.0)
    glTranslatef(0, -0.1 * moveRightY, 0)
    glScalef(0.4, 0.4, 0.4)
    #
    # glTranslatef(2, 0, 0)
    # glTranslatef(-0.7 * x, 0, 0)
    # glTranslatef(0, -0.1 * y, 0)
    # glRotatef(-45, 1, 1, 1)
    # glRotatef(0.5 * 60, 0.5, 1, 0.0)
    # glRotatef(moveRight, 0, 0, 1.0)
    # glTranslatef(0, 0.1 * moveRightY, 0)
    # glScalef(0.1, 0.1, 0.1)
    inner(1, 1, 3, 3)



    # glTranslatef(8, -0.5, 0)
    # glRotatef(90, 1, 0, 0)
    # glBegin(GL_TRIANGLE_FAN)
    # #
    #
    # # glVertex(1, 1, 0)
    # # glVertex(0, 1, 0)
    # # glVertex(1, 0, 0)
    # # glVertex(0, 0, 0)
    # # glVertex(1, 1, 0)
    #
    # glVertex(-10, -10, 0)
    # glVertex(-10, 10, 0)
    # glVertex(10, -10, 0)
    # glVertex(10, 10, 0)
    # # glVertex(4, 4, 0)
    # glEnd()

    glPopMatrix()
    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_TEXTURE_2D)


def draw():
    global moveUp
    global moveRight
    global x
    global y
    global moveRightY

    # time.sleep(1.53)
    time.sleep(0.33)
    # time.sleep(0.1)
    # time.sleep(0.04)
    glClearColor(1, 0.9, 5.0, 1.0)
    glPushMatrix()
    glColor3f(0, 0, 0)
    glPopMatrix()

    glClearColor(1, 0.9, 5.0, 1.0)

    glPushMatrix()


    # glEnd()
    glPopMatrix()


    glPushMatrix()
    draw_cube()
    drawObject()


    glPopMatrix()

    if moveRight < 270:
        # y += 0.16
        x += 0.1
        moveRight += 5
        if -5 < moveRight <= 30:
            y -= 0.19
            x -= 0.02
        #     moveRightY += 0.1
        #     if moveRight >= 25:
        #         moveRightY += 0.1
        #         x += 0.05
        #         if moveRight >= 40:
        #             moveRightY += 0.1
        elif 30 < moveRight <= 90:
            # x += 10
            y += 0.22
            x -= 0.02
            if moveRight > 60:
                y -= 0.07
                x += 0.02
                if moveRight > 70:
                    y -= 0.05

        #     moveRightY /= 1.01
        #     x -= 0.03
        elif 90 < moveRight < 125:
            y += 0.29
            if moveRight > 105:
                y -= 0.1
                x += 0.03
            x += 0.02
        #     pass
            # if moveRight <= 110:
            #     moveRightY -= 0.09
            # y += 0.06
            # moveRightY += 0.15
            # x += 0.04
            # if moveRight >= 110:
            #     y -= 0.02
        elif 125 <= moveRight <= 185:
            y += 0.03
            x += 0.05
            if moveRight > 135:
                y -= 0.09
                x += 0.02
                if moveRight > 150:
                    y -= 0.06
                    x -= 0.02
                    if moveRight > 155:
                        y -= 0.09
                        # x += 0.01
                        x -= 0.01
                        if moveRight > 165:
                            y -= 0.08


        #     moveRightY -= 0.1
        #     x += 0.01
        #     y += 0.12
        #     if moveRight >=120:
        #         pass
        elif 185 < moveRight < 280:
            y += 0.065
            x += 0.01
            if moveRight > 205:
                y -= 0.12
                if moveRight > 215:
                    y += 0.01
                    if moveRight > 230:
                        # y += 0.05
                        # x += 0.02
                        y -= 0.14
                        if moveRight > 245:
                            x -= 0.02
                            # y += 0.05
                            if moveRight > 255:
                                y -= 0.1






        # elif 360 <= moveRight <= 410:
        #     # moveRightY += 0.1
        #     if moveRight >= 385:
        #         moveRightY += 0.19
        #         x += 0.05
        #         if moveRight >= 390:
        #             moveRightY -= 0.05
        #         # pass
        # elif 410 < moveRight < 450:
        #     moveRightY -= 0.15
        #     x -= 0.03
        #
        # elif 450 <= moveRight < 475:
        #     if moveRight <= 470:
        #         moveRightY -= 0.09
        #     moveRightY += 0.15
        #     x += 0.04
        #
        # elif 475 <= moveRight < 520:
        #     moveRightY -= 0.1
        #     x += 0.02
        #     y += 0.12
        #     if moveRight >= 480:
        #         # y += 0.2
        #         pass

    # if x < 6.7:



moveUp = 0
moveRight = -5
moveRightY = 0
x = 0
y = 0


def main():
    global texture, texture2
    d_x = 1
    d_y = 1
    d_z = 10

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    texture = get_texture('checks.jpg')
    # texture2 = get_texture('ground.jpg')

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_CULL_FACE)
    glEnable(GL_NORMALIZE)
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 1)
    glEnable(GL_LIGHTING)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, [5, 1, 2, 1])
    # glLightfv(GL_LIGHT0, GL_POSITION, [-2, 1, 4, 1.1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.1])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.01)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 50)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 128)

    glEnable(GL_LIGHT0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60., 1., 1., 30.)
    glTranslatef(0, 0, -7)
    # glTranslatef(0, 1, 0)
    # glTranslatef(-0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glMatrixMode(GL_MODELVIEW)
    glRotatef(10, 1, 1, 0)
    glRotatef(20, 1, 1, 0)
    # glRotatef(-10, 1, 0, 0)
    f = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
