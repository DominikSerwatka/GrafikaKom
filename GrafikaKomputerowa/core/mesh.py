from core.object3D import Object3D
from OpenGL.GL import *

class Mesh(Object3D):
    def __init__(self, geometry, material):
        super().__init__()
        self.geometry = geometry
        self.material = material
        # should this object be rendered?
        self.visible = True
        # set up associations between
        # attributes in geometry shader variables in material
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        for variableName, AttributeObject in geometry.attributes.items():
            AttributeObject.associateVariable(material.programRef, variableName )
        # unbind the vertex array object
        glBindVertexArray(0)
        


