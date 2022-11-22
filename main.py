import math

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image as Image
import numpy
import time


def inner(bottom, top, height, slices):
    h = height / 2
    points = []
    for i in range(int(slices) + 1):
        angle = 2 * math.pi * (i / slices)

        points.append((bottom * math.cos(angle), bottom * math.sin(angle),
                       top * math.cos(angle), top * math.sin(angle)))
        if i == slices-3:
            # points.append((bottom * math.cos(angle) + 1, bottom * math.sin(angle) + 1,
            #                top * math.cos(angle) + 1, top * math.sin(angle) + 1))
            points.append((1, 1, 1, 1))
        else:
            points.append((bottom * math.cos(angle), bottom * math.sin(angle),
                           top * math.cos(angle), top * math.sin(angle)))
    print(points)
    glBegin(GL_TRIANGLE_FAN)
    for (x_bottom, y_bottom, x_top, y_top) in points:
        glVertex(x_top, y_top, h)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    for (x_bottom, y_bottom, x_top, y_top) in points:
        glVertex(x_bottom, y_bottom, -h)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    for (x_bottom, y_bottom, x_top, y_top) in points:
        glVertex(x_bottom, y_bottom, -h)
        glVertex(x_top, y_top, h)
    glEnd()



def get_texture(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    text_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, text_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    img.close()

    return text_id


def draw_cube():

    glPushMatrix()
    glTranslated(0.35, -5, -1)
    glRotatef(10, 1, 0, 0)
    glutSolidCube(8)
    glPopMatrix()


def draw_icosahedron():
    global texture

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glPushMatrix()

    glTranslatef(-2, -2, -10)
    glTranslatef(0.3 * x, 0, 0)
    glTranslatef(0, 0.1 * y, 0)

    # glRotatef(60, 1, 1, 1.0)
    # glRotatef(30, 1, 1, 1.0)
    # glRotatef(45, 1, 1, 1.0)
    glRotatef(45, 1, 1, 1)
    glRotatef(-0.5 * 60, 0.5, 1, 0.0)
    glRotatef(-moveRight, 0, 0, 1.0)
    glTranslatef(0, -0.1 * moveRightY, 0)
    # glRotatef(-moveUp, 0, 1, 0)

    glScalef(0.4, 0.4, 0.4)
    # glutWireIcosahedron()
    # glutSolidIcosahedron()
    inner(1, 1, 3, 3)

    # glTranslatef(4, 0, 0)
    # inner(1, 1, 1, 5)
    # inner(1, 1, 1, 5)
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

    # time.sleep(0.34)
    time.sleep(0.04)
    glClearColor(0, 0, 0, 1)
    glPushMatrix()
    glColor3f(1, 1, 1)
    glPopMatrix()

    glClearColor(0, 0, 0, 1)

    glPushMatrix()
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    draw_icosahedron()

    glPopMatrix()

    # if moveRight < 110:  # 55 - первый поворот
    #     moveRight += 5
    #     if -5 < moveRight < 25:
    #         moveRightY += 0.05
    #     elif 65 < moveRight < 70:
    #         moveRightY += 0.05
    #     elif 30 < moveRight < 60:
    #         moveRightY -= 0.05
    #
    # if moveRight >= 110 and moveUp < 16:
    #     moveUp += 2
    #     y += 0.1
    #
    # if x < 2.3:
    #     x += 0.1

    if moveRight < 470:  # 55 - первый поворот
        moveRight += 5
        if -5 < moveRight <= 50:
            moveRightY += 0.1
            if moveRight >= 25:
                moveRightY += 0.1
                x += 0.05
                if moveRight >= 40:
                    moveRightY += 0.1
            # pass
        elif 50 < moveRight < 90:
            moveRightY -= 0.15
            x -= 0.03

        elif 90 <= moveRight < 115:
            if moveRight <= 110:
                moveRightY -= 0.09
            y += 0.06
            moveRightY += 0.15
            x += 0.04
            if moveRight >= 110:
                y -= 0.02

        elif 115 <= moveRight < 160:
            moveRightY -= 0.1
            x += 0.02
            y += 0.12
            if moveRight >=120:
                # y += 0.2
                pass
            # if moveRight > 150:
            #     moveRightY -= 0.1
            # x += 0.1
        elif 160 <= moveRight < 210:
            y -= 0.12
            x += 0.04
            if moveRight > 180:
                # x -= 0.02
                y -= 0.1

        elif 210 <= moveRight <= 259:
            # y += 0.2
            x += 0.005
            if moveRight > 240:
                y -= 0.1
            # if moveRight > 180:
            #     x -= 0.04
            #     y -= 0.2

        elif 260 < moveRight <= 290:
            y -= 0.14
            # x -= 0.01
            if moveRight > 280:
                y -= 0.07

        elif 290 < moveRight < 360:
            y += 0.15
            x -= 0.02
            if moveRight > 300:
                x += 0.04
                y -= 0.04

        elif 360 <= moveRight <= 410:
            # moveRightY += 0.1
            if moveRight >= 385:
                moveRightY += 0.19
                x += 0.05
                if moveRight >= 390:
                    moveRightY -= 0.1
                # pass
        elif 410 < moveRight < 450:
            moveRightY -= 0.15
            x -= 0.03

        elif 450 <= moveRight < 475:
            if moveRight <= 470:
                moveRightY -= 0.09
            moveRightY += 0.15
            x += 0.04

        elif 475 <= moveRight < 520:
            moveRightY -= 0.1
            x += 0.02
            y += 0.12
            if moveRight >= 480:
                # y += 0.2
                pass
            # if moveRight > 180:
            #     x -= 0.04
            #     y -= 0.2
            # x -= 0.01
            # if moveRight >=125:
            #     y += 0.3
        # elif 160 <= moveRight < 270:
        #     moveRightY += 0.05

        #     moveRightY += 0.15
        #     # x += 0.1
        # elif 540 <= moveRight < 599:
        #     moveRightY -= 0.15
        #     x += 0.1
        # elif 600 <= moveRight < 659:
        #     moveRightY += 0.15
        #     # x += 0.1
        # elif 660 <= moveRight < 719:
        #     moveRightY -= 0.15
        #     x += 0.1
        # elif 720 <= moveRight < 779:
        #     moveRightY += 0.15
        #     # x += 0.1
        # elif 840 <= moveRight < 899:
        #     moveRightY -= 0.15
        #     x += 0.1


    # if moveRight >= 110 and moveUp < 16:
    #     moveUp += 2
    #     y += 0.1

    if x < 10.8:
        x += 0.1


moveUp = 0
moveRight = -5
moveRightY = 0
x = 0
y = 0


def main():
    global texture
    d_x = 1
    d_y = 1
    d_z = 10

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    texture = get_texture('mars.jpg')

    glEnable(GL_CULL_FACE)

    glEnable(GL_LIGHTING)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, [-2, 5, 4, 1.1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 0.1])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 50)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 128)

    glEnable(GL_LIGHT0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(25., 1., 1., 80.)
    glTranslatef(-0.25, 0.14, -4.5)
    glMatrixMode(GL_MODELVIEW)
    f = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    d_x = d_x - 1
                    print('d_x = ', d_x)

                if event.key == pygame.K_d:
                    d_x = d_x + 1
                    print('d_x = ', d_x)

                if event.key == pygame.K_w:
                    d_y = d_y + 1
                    print('d_y = ', d_y)

                if event.key == pygame.K_s:
                    d_y = d_y - 1
                    print('d_y = ', d_y)

                if event.key == pygame.K_e:
                    d_z = d_z - 1
                    print('d_z = ', d_z)

                if event.key == pygame.K_q:
                    d_z = d_z + 1
                    print('d_z = ', d_z)

        _ = pygame.key.get_pressed()
        # glLightfv(GL_LIGHT0, GL_POSITION, [d_x, d_y, d_z, 1.0])
        # glLightfv(GL_LIGHT0, GL_POSITION, [-200+x, w1, 0, 1.0])
        # x += 0.3
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
