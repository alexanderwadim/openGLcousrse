from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import pygame
import math
import time


def draw():
    global yellow, white1, white2, middle, upper, ending, cn, slc, p
    time.sleep(0.3)

    def inner(bottom, top, height, slices):
        h = height / 2
        points = []
        for i in range(int(slices) + 1):
            angle = 2 * math.pi * (i / slices)
            points.append((bottom * math.cos(angle), bottom * math.sin(angle),
                           top * math.cos(angle), top * math.sin(angle)))

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

    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0, 0.0, -0.5)
    glRotatef(60, 1.0, 1.0, 1.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, white2)
    inner(0.1 + middle * 15, 0.1 + middle * 15, 0.25, 31 - slc)
    glTranslatef(0.0, 0.0, 0.1)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, white1)
    inner(0.1 + middle * 25, 0.1 + middle * 10, 0.2 - middle * 10, 31 - slc)
    glTranslatef(0.0, 0.0, 0.2)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, white2)
    inner(0.1 + middle * 10, 0.1 + middle * 10, 0.2, 31 - slc)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, white1)
    glTranslatef(0.0, 0.0, 0.15)
    inner(0.1 + upper, 0.05 + upper * 0.3, 0.1 + upper * 0.3, 31 - slc)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, yellow)
    glTranslatef(0.0, 0.0, 0.105 - p)
    inner(0.015 + ending, 0.001 + ending, 0.06 + ending * 5, 31 - slc)
    glPopMatrix()
    if upper < 0.16:
        w1 = list(white1)
        w2 = list(white2)
        y = list(yellow)
        w1[0] -= 0.11
        w1[1] -= 0.12
        w1[2] -= 0.12
        w2[0] -= 0.094
        w2[1] -= 0.1
        w2[2] -= 0.108
        y[0] -= 0.12
        y[1] -= 0.123
        y[3] += 0.125
        white2 = tuple(w2)
        white1 = tuple(w1)
        yellow = tuple(y)
        p -= 0.01
        ending += 0.002
        cn += 0.008
        slc += 3
        middle += 0.001
        upper += 0.02


middle = upper = ending = cn = slc = p = 0
yellow, white1, white2 = (1.0, 1.0, 0.0, 0.0), (1, 1, 1, 1), (1, 1, 1, 1)

glutInit()
pygame.init()
display = (800, 800)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(1, 0.9, 5.0, 1.0)
glRotatef(90, 0.0, 0.0, 1.0)
glRotatef(22.1, 0.0, 0.0, 1.0)
glRotatef(15, 0.0, 1.0, 0.0)
glShadeModel(GL_SMOOTH)
glEnable(GL_CULL_FACE)
glEnable(GL_LIGHTING)
mat_specular = (0.0, 0.0, 0.0, 1.0)
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
glLightfv(GL_LIGHT0, GL_POSITION, [0.2, 0.4, 1, 1.0])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 0])
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.09)
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 50)
glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 100)
glEnable(GL_LIGHT0)
flag = False
count = 0
while True:
    if flag == True or count < 1:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(1)
        count += 1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            flag = True
