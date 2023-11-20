import pygame
import sys
from core.input import Input
class Base(object):

    def __init__(self):
        # initialize all pygame modules
        pygame.init()
        #  width and height of window
        screenSize = (512,512)
        # indicate rendering options
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # initialize buffers to perform antialiasing
        # pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        # pygame.display.gl_get_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # creat window and display
        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        # set the text title bar of window
        pygame.display.set_caption("pygame window")
        # determine if main loop is activ
        self.running = True
        # manage time-related data and operations
        self.clock = pygame.time.Clock()
        # manage user input
        self.input = Input()
        
    # implement by extending class
    def initialize(self):
        pass
    # implement by extening class
    def update(self):
        pass
    def run(self):
        # startup 
        self.initialize()
        # main loop
        while self.running:
            # process input
            # self.input.update()
            self.input.update()
            if self.input.quit:
                self.running = False

            # upadate
            self.update()
            # render

            # display image
            pygame.display.flip()
            # pause if necessery to achive 60 FPS
            self.clock.tick(60)

        # shutdown 
        pygame.quit()
        sys.exit()


            


