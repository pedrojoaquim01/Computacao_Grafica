import sys

import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),
    (-1, -1, 1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, -1, -1),
)

linhas = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (4, 1),
    (1, 2),
    (2, 3),
    (3, 4),
)

faces = (
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 1)
)


cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )


def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        # glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()
    glBegin(GL_QUADS)
    for v in (1, 2, 3, 4):
        glColor3fv(cores[v])
        glVertex3fv(vertices[v])
    glEnd()


a = 0

def desenhaDuasPiramides():
    # Cubo da Esquerda
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(-a,0,0,1)
    Piramide()
    glPopMatrix()
    # Cubo da Direita
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(a,1,0,0)
    Piramide()
    glPopMatrix()



def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0,-2,0)
    desenhaDuasPiramides()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,2,0)
    desenhaDuasPiramides()
    glPopMatrix()
    a += 1
    


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
glTranslatef(0.0, 0.0, -20)

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