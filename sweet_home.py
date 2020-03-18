from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import PySimpleGUI as sg
import math
import sys


pontos = np.array([
    [2,2,1,2,2.5,2.5,4,4,6.5,7.5,6.5,6.5,2], # X
    [2.5,4.5,4.5,6,6,7,7,6,6,4.5,4.5,2.5,2.5], # Y
])

def Escala(tecla):
    for x in range(len(pontos[0])):
        if(tecla.decode('utf-8') == 'o'):
            pontos[0][x] *= 1.5;
            pontos[1][x] *= 1.5;
        
        if(tecla.decode('utf-8') == 'i'):
            pontos[0][x] /= 2.0;
            pontos[1][x] /= 2.0;


def Translacao(tecla):
    for y in range(len(pontos[0])):
        if(tecla.decode('utf-8') == '8'):
            pontos[1][y] += 1;
        if(tecla.decode('utf-8') == '2'):
            pontos[1][y] -= 1;
        if(tecla.decode('utf-8') == '4'):
            pontos[0][y] -= 1;
        if(tecla.decode('utf-8') == '6'):
            pontos[0][y] += 1;


def Rotacao(angulo):
    for y in range(len(pontos[0])):
        pontos[0][y] = (pontos[0][y] * math.cos(angulo)) - (pontos[1][y] * math.sin(angulo))
        pontos[1][y] = (pontos[0][y] * math.sin(angulo)) + (pontos[1][y] * math.cos(angulo))

def Espelhamento(tecla):
    for x in range(len(pontos[0])):
        if(tecla.decode('utf-8') == '7'):
            pontos[0][x] *= -1;
        if(tecla.decode('utf-8') == '1'):
            pontos[1][x] *= -1;

def Cisalhamento(tecla):
    for x in range(len(pontos[0])):
        if(tecla.decode('utf-8') == 'k'):
            if(x == 0 or x == len(pontos[0]) -1): continue;
            pontos[0][x] += 2;

        if(tecla.decode('utf-8') == 'l'):
            if(x == 0 or x == len(pontos[0]) -1): continue;
            pontos[1][x] += 2;


def KeyBoard(tecla,x,y):
    print(tecla)
    if(tecla == 36): # F12
        sys.exit(0)
    if(tecla.decode('utf-8') == 'n' or tecla.decode('utf-8') == 'N'):
        Rotacao(-2)
    if(tecla.decode('utf-8') == 'm' or tecla.decode('utf-8') == 'M'):
        Rotacao(2)
    
    Escala(tecla)
    Translacao(tecla)
    Espelhamento(tecla)
    Cisalhamento(tecla)

    glutPostRedisplay()

def Draw_The_Home():
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(3.0)             
    glBegin(GL_LINE_LOOP)
    for x in range(len(pontos[0])):
        glVertex2f(pontos[0][x],pontos[1][x])
    glEnd()  

    glutSwapBuffers();

def refresh():
    glClearColor(0.0,0.0,0.0,1.0)
    win = 10.0
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-win,win,-win,win)
    glMatrixMode(GL_MODELVIEW)
                            
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(720, 720)                      # set window size
glutInitWindowPosition(300, 300)                           # set window position
glutCreateWindow("Second App on OpenGL")              # create window with title
glutDisplayFunc(Draw_The_Home) 
glutKeyboardFunc(KeyBoard)  
refresh()
glutMainLoop()   
