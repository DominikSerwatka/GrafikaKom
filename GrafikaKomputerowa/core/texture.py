import pygame
from OpenGL.GL import *

class Texture(object):
    def __init__(self, fileName=None, properties={}):
        # pygame surface object to store image data
        self.surface = None

        # texture reference
        self.textureRef = glGenTextures(1)

        # default properties values
        self.properties = {
            "magFilter": GL_LINEAR,
            "minFilter": GL_LINEAR_MIPMAP_LINEAR,
            "wrap"     : GL_REPEAT
        }
        # overwrite default property values
        self.setProperties(properties)

        if fileName is not None:
            self.loadImage(fileName)
            self.uploadData()
    
    # load image from file
    def loadImage(self, fileName):
        self.surface = pygame.image.load(fileName)
    
    # set property values
    def setProperties(self, props):
        for name, data in props.items():
            if name in self.properties.keys():
                self.properties[name] = data
            else:
                raise Exception("No property named: "+name)
            
    # upload pixel data to GPU
    def uploadData(self):

        # store image dimensions
        width = self.surface.get_width()
        height = self.surface.get_height()

        # conver image to string buffer
        pixelData = pygame.image.tostring(self.surface, "RGBA", 1)
        # bind texture
        glBindTexture(GL_TEXTURE_2D, self.textureRef)

        # send data to texture object
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixelData)
        # mipmaps
        glGenerateMipmap(GL_TEXTURE_2D)

        # set  texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,self.properties["magFilter"])
        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,self.properties["minFilter"])

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, self.properties["wrap"])
        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, self.properties["wrap"])

        # set default border color to white
        # important for rendering shadows
        glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, [1,1,1,1])
        
        





