import math
import sys

import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *

x0 = -2
xf = 2
y0 = -2
yf = 2

def func2(x,y):
    return math.sin(10 * (x*x+y*y))/0.05

def func1(x,y):
    return 1/(((x*x)+(y*y))+ 0.001 )

def func(x,y):
    return x *x+ y*y


def EsferaPontos(nx, ny):
    dx = (xf - x0)/nx
    dy = (yf - y0)/ny
    #glBegin(GL_POINTS)
    for i in range(0,nx):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(0,ny):
            x = x0 + i * dx
            y = y0 + j * dy
            z = func(x,y)
            glVertex3f(x, y, z)
            glVertex3f(x + dx, y, func(x + dx,y))
        glEnd()
    #glEnd()

ar = 0


def desenha():
    global ar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(ar, 1, 1, 0)
    EsferaPontos(20, 20)
    #EsferaPontos(20, 3)
    glPopMatrix()
    ar += 0.1


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Cubo", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH,
                               WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
    desenha()
    sdl2.SDL_GL_SwapWindow(window)
