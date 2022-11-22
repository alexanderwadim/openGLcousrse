import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image as Image
import numpy

def drawCube():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glPushMatrix()
    glTranslated(1, 0, -13)
    glRotatef(20, 20, 20, 0)
    glEnable(GL_COLOR_MATERIAL)
    glColor4f(1.0, 0, 1.0, 0.5)
    glutSolidCube(0.5)
    glPopMatrix()
    glColor4f(1.0, 1.0, 1.0, 1.0)

def drawAnotherSphere():
    # mat_specular = (0, 0, 0, 1)
    mat_specular = (1, 1, 1, 1)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    s = gluNewQuadric()
    gluQuadricTexture(s, GL_TRUE)
    glPushMatrix()
    glTranslated(-3, 5, -30)
    gluSphere(s, 0.5, rn, rn)
    glPopMatrix()

def drawSphere():
    texture = read_texture('ww.jpg')

    mat = gluNewQuadric()
    gluQuadricTexture(mat, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)

    glPushMatrix()
    glTranslated(0, 0, -15)
    glRotatef(300, 300, 400, 100)
    gluSphere(mat, 1, rn, rn)
    gluDeleteQuadric(mat)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()


def read_texture(filename):
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

rn = 25

x = 0
y = 0
z = 0
r = 1.0
g = 1.0
b = 1.0
flag = False
flag1 =True
border = 30

pygame.init()
display = (1000, 1000)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glShadeModel(GL_SMOOTH)
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
lightZeroPosition = [x, y, z, 1.]
lightZeroColor = [r, g, b, 1.0]
mat_specular = (0.0, 0.0, 0.0, 1.0)

glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.04)
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 50)
glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 100)
glEnable(GL_LIGHT0)
glMatrixMode(GL_PROJECTION)
gluPerspective(30., 1., 1., 30.)
glMatrixMode(GL_MODELVIEW)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
while True:

    if not flag:
        if x == border:
            flag = True
        else:
            x += 6
    if flag == True:
        if x == -border:
            flag = False
        else:
            x -= 6
    lightZeroPosition = [x, y, z, 1.]
    print(flag1)
    if flag1 == True:
        g += 0.05
        b += 0.05
        lightZeroColor = [r, g, b, 1.0]
        if g + 0.1 >= 1:
            flag1 = False
        else:
            glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    else:
        g -= 0.05
        b -= 0.05
        lightZeroColor = [r, g, b, 1.0]
        if g - 0.1 <= 0.5:
            flag1 = True
        else:
            glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)


    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawSphere()
    drawAnotherSphere()
    drawCube()

    pygame.display.flip()
    pygame.time.wait(2)
