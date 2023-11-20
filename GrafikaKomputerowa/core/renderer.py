from OpenGL.GL import *
from core.mesh import Mesh

class Renderer(object):

    def __init__(self, clearColor = [0,0,0]):

        glEnable(GL_DEPTH_TEST)
        glClearColor(clearColor[0], clearColor[1], clearColor[2], 1.0)
        # support transparent textures
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        

    def render(self, scene, camera):

        # clear buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # update camera view matrix
        camera.updateViewMatrix()
        # extract list of Mesh objects in scene
        descendentList = scene.getDescendentList()
        meshFilter = lambda x : isinstance(x, Mesh)
        meshList = list(filter(meshFilter, descendentList))

        for mesh in meshList:
            # if mesh is not visible, continue to next object in list
            if not mesh.visible:
                continue
            glUseProgram(mesh.material.programRef)
            # bind vao - vertrex array object
            glBindVertexArray(mesh.vaoRef)
            # update uniform matrices
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projectionMatrix
            # updata uniforms stored in material
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()
            # updata render settings
            mesh.material.updateRenderSettings()
            glDrawArrays(mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)



            


