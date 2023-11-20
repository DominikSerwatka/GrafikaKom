import numpy 
from OpenGL.GL import *
class Attribute(object):

    def __init__(self, dataType, data):
        # type of elements in data array
        # int | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # array of data to store in buffer
        self.data = data
        # reference to available buffer in GPU
        self.bufferRef = glGenBuffers(1)

        # upload data immediately
        self.uploadData()

    # upload this data to gpu buffer
    def uploadData(self):
        # conver data to numpy array format
        data = numpy.array(self.data).astype(numpy.float32)
        # select buffer used by following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(),GL_STATIC_DRAW)

    # associate varaiable in gpu program with this buffer
    def associateVariable(self, programRef, variableName):
        # get refrence for program variable with given name 
        variableRef = glGetAttribLocation(programRef, variableName)
        # if the program does not refrence the variable, exit
        if variableRef == -1:
            return 
        # select buffer used by folowing functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        # specify how the data will be read
        # from the buffer currently bound to GL_ARRAY_BUFFER
        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception("Unknown Attribute type" + self.dataType)
        # indicate data should be streamed to variable from buffer
        glEnableVertexAttribArray(variableRef)




        





