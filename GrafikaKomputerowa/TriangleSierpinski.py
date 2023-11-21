import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# edges = (
#     (0, 1),
#     (1, 2),
#     (2, 3),
#     (3, 0),

#     (0, 4),
#     (1, 4),
#     (2, 4),
#     (3, 4),
# )

# surfaces = (
#     (0, 1, 2, 3),
#     (0, 1, 4),
#     (0, 3, 4),
#     (3, 2, 4),
#     (2, 1, 4),
    
# )
colors = (
    (1, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (0, 0, 1),
    (0, 1, 1),
)
def triangle(A, B, C):
    glBegin(GL_TRIANGLES)
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glEnd()

def drawTriangle(V1, V2, V3, V4):
    glColor3f(1, 0, 0)
    triangle(V1, V2, V3)
    glColor3f(1, 1, 0)
    triangle(V1, V3, V4)
    glColor3f(1, 0, 1)
    triangle(V2, V3, V4)
    glColor3f(0, 0, 1)
    triangle(V1, V2, V4)


def divide(V1, V2, V3, V4, n):
    V12 = [(V1[i] + V2[i]) / 2 for i in range(3)]
    V23 = [(V2[i] + V3[i]) / 2 for i in range(3)]
    V31 = [(V3[i] + V1[i]) / 2 for i in range(3)]
    V14 = [(V1[i] + V4[i]) / 2 for i in range(3)]
    V24 = [(V2[i] + V4[i]) / 2 for i in range(3)]
    V34 = [(V3[i] + V4[i]) / 2 for i in range(3)]

    if n > 0:
        divide(V1, V12, V31, V14, n - 1)
        divide(V12, V2, V23, V24, n - 1)
        divide(V31, V23, V3, V34, n - 1)
        divide(V14, V24, V34, V4, n - 1)
    else:
        drawTriangle(V1, V2, V3, V4)

def draw():
    vertices = [
        [-1, -1, -1],
        [1, -1, -1],
        [0, 1, -0.5],
        [0.5, -1, 1],
    ]
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    divide(vertices[0], vertices[1], vertices[2], vertices[3], N)
    pygame.display.flip()
       






# def pyramid():
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(vertices[vertex])
#     glEnd()

#     glBegin(GL_QUADS)
#     for surface in surfaces:
#         for i, vertex in enumerate(surface):
#             glColor3fv(colors[i])
#             glVertex3fv(vertices[vertex])
#     glEnd()

def light():
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.0, 0.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 1.0, 0.0, 1.0))
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)



def main():

    global N
    N = int(input("Enter the Number of level : "))
    move_speed = 0.1
    zoom_factor = 0.1
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glTranslatef(0.0, 0.1, 0)

                if event.key == pygame.K_DOWN:
                    glTranslatef(0.0, -0.1, 0)

                if event.key == pygame.K_PLUS:  # Zoom in
                    glTranslatef(0.0, 0.0, zoom_factor)

                if event.key == pygame.K_MINUS:  # Zoom out
                    glTranslatef(0.0, 0.0, -zoom_factor)

                if event.key == pygame.K_LEFT:  # Move to the left
                    glTranslatef(-move_speed, 0.0, 0)

                if event.key == pygame.K_RIGHT:  # Move to the right
                    glTranslatef(move_speed, 0.0, 0)

        #glRotatef(1, 1, 0, 0)  # Rotate only around the x-axis
        glRotatef(1, 0, 1, 0)  # Rotate only around the y-axis

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        light()
        #pygame.display.flip()
        pygame.time.wait(10)

main()
