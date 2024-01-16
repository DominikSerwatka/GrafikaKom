import math

import pygame
from OpenGL.raw.GLU import gluPerspective
from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL import Image
import sys


N = 1
texture_path = 'wood2.jpg'
only_border = False
texture_id = 0


vertices = [
    [-3/2, -1, -math.sqrt(3)/2],
    [3/2, -1, -math.sqrt(3)/2],
    [0, -1, math.sqrt(3)],
    [0, math.sqrt(6)-1, 0],
]

light_position = [2, 2, 2, 1]
light_color = [1.0, 1.0, 1.0, 1.0]



def triangle_line(V1, V2, V3, V4):
    glBegin(GL_LINES)

    vertices = [
        V1,
        V2,
        V3,
        V4,
    ]
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])

    glVertex3fv(vertices[3])
    glVertex3fv(vertices[1])

    glVertex3fv(vertices[3])
    glVertex3fv(vertices[0])

    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])

    glVertex3fv(vertices[0])
    glVertex3fv(vertices[2])

    glVertex3fv(vertices[2])
    glVertex3fv(vertices[1])
    glEnd()


def triangle(A, B, C):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_TRIANGLES)
    glTexCoord2f(0.0, 0.0)
    glVertex3fv(A)
    glTexCoord2f(1.0, 0.0)
    glVertex3fv(B)
    glTexCoord2f(1.0, 1.0)
    glVertex3fv(C)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def draw_triangle(V1, V2, V3, V4):
    if only_border:
        glColor3f(1, 0, 0)
        triangle_line(V1, V2, V3, V4)
        glColor3f(1, 0, 0)
    else:
        triangle(V1, V2, V3)
        triangle(V1, V3, V4)
        triangle(V2, V3, V4)
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
        draw_triangle(V1, V2, V3, V4)


def draw():
    divide(vertices[0], vertices[1], vertices[2], vertices[3], N)


def draw_floor_2():
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINES)

    for i in range(-10, 11):
        glVertex3f(-10, -1, i)
        glVertex3f(10, -1, i)

        glVertex3f(i, -1, -10)
        glVertex3f(i, -1, 10)

    glEnd()

def draw_floor():
    glEnable(GL_TEXTURE_2D)
    floor_texture = load_texture("grass.jpg")

    glBindTexture(GL_TEXTURE_2D, floor_texture)

    glBegin(GL_QUADS)

    for i in range(-10, 10):
        for j in range(-10, 10):
            glTexCoord2f(0, 0)
            glVertex3f(i, -1, j)

            glTexCoord2f(1, 0)
            glVertex3f(i + 1, -1, j)

            glTexCoord2f(1, 1)
            glVertex3f(i + 1, -1, j + 1)

            glTexCoord2f(0, 1)
            glVertex3f(i, -1, j + 1)

    glEnd()

    glDisable(GL_TEXTURE_2D)


# Ładowanie tekstury
def load_texture(file_path):
    image = Image.open(file_path)
    image_data = image.tobytes("raw", "RGB", 0, -1)
    width, height = image.size
    texture_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)

    return texture_id


def light():
    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 0))  # Directional light from left, top, front

    glLightfv(GL_LIGHT0, GL_AMBIENT, (1.0, 1.0, 0.3, 1.0))

    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 0.3, 1.0))

    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 0.3, 1.0))

    glLight(GL_LIGHT1, GL_POSITION, light_position)  # Point light source at position (2, 2, 2)

    glLightfv(GL_LIGHT1, GL_AMBIENT, light_color)

    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_color)

    glLightfv(GL_LIGHT1, GL_SPECULAR, light_color)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)


user_input = input("Podaj liczbe poziomow: ")
N = int(user_input)

while( not (N >= 0 and N <= 5) ):
    user_input = input("Podaj liczbe poziomow: ")
    N = int(user_input)

# Inicjalizacja Pygame
pygame.init()


# Ustawienia okna Pygame
width, height = 800, 600
pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Grafika piramida")

texture_id = load_texture(texture_path)

# Ustawienia OpenGL
glClearColor(0.0, 0.0, 0.0, 1.0)
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (width / height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -5)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)

# Zmienna do przechowywania odległości kamery od obiektu
camera_distance = 5.0
camera_position_x = 0.0
camera_position_y = 0.0

# Główna pętla renderowania
angle = 0.2
x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll w górę
                camera_distance -= 0.1
                if camera_distance < 1.0:
                    camera_distance = 1.0
            elif event.button == 5:  # Scroll w dół
                camera_distance += 0.1
                if camera_distance > 10.0:
                    camera_distance = 10.0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Zwiększenie liczby poziomow piramidy
                N += 1
            elif event.key == pygame.K_m: # Zminiejszenie liczby poziomow piramidy
                if (N != 0):
                    N -= 1
            elif event.key == pygame.K_a:  # Przesunięcie kamery w lewo
                camera_position_x += 0.1
            elif event.key == pygame.K_d:  # Przesunięcie kamery w prawo
                camera_position_x -= 0.1
            elif event.key == pygame.K_w:  # Przesunięcie kamery w górę
                camera_position_y -= 0.1
            elif event.key == pygame.K_s:  # Przesunięcie kamery w dół
                camera_position_y += 0.1
            elif event.key == pygame.K_b:  # Wylaczenie tekstur
                only_border = not only_border
            elif event.key == pygame.K_UP:  # Przesunięcie światła w górę
                light_position[1] += 0.1
            elif event.key == pygame.K_DOWN:  # Przesunięcie światła w dół
                light_position[1] -= 0.1
            elif event.key == pygame.K_LEFT:  # Przesunięcie światła w lewo
                light_position[0] -= 0.1
            elif event.key == pygame.K_RIGHT:  # Przesunięcie światła w prawo
                light_position[0] += 0.1
            elif event.key == pygame.K_c:  # Zmiana koloru światła na czerwony
                light_color = [1.0, 0.0, 0.0, 1.0]
            elif event.key == pygame.K_z:  # Zmiana koloru światła na zielony
                light_color = [0.0, 1.0, 0.0, 1.0]
            elif event.key == pygame.K_n:  # Zmiana koloru światła na niebieski
                light_color = [0.0, 0.0, 1.0, 1.0]

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Zastosowanie przekształceń kamery
    glTranslatef(camera_position_x, camera_position_y, -camera_distance)
    glRotatef(angle, 0, 0.5, 0)
    light()

    glPushMatrix()
    draw()
    glPopMatrix()

    glPushMatrix()
    glLoadIdentity()
    glTranslatef(camera_position_x, camera_position_y, -camera_distance)
    if only_border:
        draw_floor_2()
    else:
        draw_floor()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.delay(10)

    angle += 0.5
