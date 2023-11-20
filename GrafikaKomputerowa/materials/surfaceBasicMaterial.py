from materials.material import Material
from materials.basicMaterial import BasicMaterial
from OpenGL.GL import *

class SurfaceBasicMaterial(BasicMaterial):

    def __init__(self, properties={}):
        super().__init__()
        # render vertecies as triangles
        self.settings["drawStyle"] = GL_TRIANGLES
        # render both sides?
        self.settings["doubleSide"] = True
        # render as wireframe?
        self.settings["wireframe"] = False
        # line thickness
        self.settings["lineWidth"] = 4

        self.setProperties(properties)

    def updateRenderSettings(self):
        if self.settings["doubleSide"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)

        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        
        glLineWidth(self.settings["lineWidth"])
        

        



