from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform
from OpenGL.GL import *

class Material(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.programRef = OpenGLUtils.initializeProgram(vertexShaderCode,fragmentShaderCode)

        # store Uniform objects
        self.uniforms = {}

        # standard uniform objects (matrices)
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)
        # store OpenGL render settigns
        self.settings = {}
        self.settings["drawStyle"] = GL_TRIANGLES
        

    def addUniform(self,dataType, variableName, data):
        self.uniforms[variableName] = Uniform(dataType, data)
    # initialize all uniform variable refrences
    def locateUniforms(self):
        for variableName, uniformObejct in self.uniforms.items():
            uniformObejct.locateVariable(self.programRef, variableName)
    # configure OpenGL render settings
    def updateRenderSettings(self):
        pass
    # convenience metod for settings multiple "properties":
    # uniform and render settings values
    def setProperties(self, properties={}):
        for name, data in properties.items():
            # update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            # updata render settings
            elif name in self.settings.keys():
                self.settings[name] = data
            # unknown property 
            else:
                raise Exception("Material has no property: " + name) 
            
            
            
