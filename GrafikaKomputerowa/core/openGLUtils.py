from OpenGL import GL

# satic methods to load/complie opengl shaders 
# and link to creat gpu programs

class OpenGLUtils(object):
    
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        # specify OpenGl version and requirements
        extension = "#extension GL_ARB_shading_language_420pack: require \n"
        shaderCode = "#version 130 \n" + extension + shaderCode

        # creat empty shder object and return  refrenece value
        shaderRef = GL.glCreateShader(shaderType)
        # store sorce code in shader
        GL.glShaderSource(shaderRef, shaderCode)
        # compile source code stored in shader
        GL.glCompileShader(shaderRef)
        # query whether compilation was successful
        compileSuccess = GL.glGetShaderiv(shaderRef, GL.GL_COMPILE_STATUS)

        if not compileSuccess:
            # retrive error message
            errorMessage = GL.glGetShaderInfoLog(shaderRef)
            # free memory used to source shader program
            GL.glDeleteShader(shaderRef)
            # convert byte string to character string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt program, print error message
            raise Exception(errorMessage)
        # complitaion was successful
        return shaderRef
    

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        # compile shaders and store refrences
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL.GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL.GL_FRAGMENT_SHADER)

        # creat program object
        programRef = GL.glCreateProgram()
        # attach previously compiled shaders
        GL.glAttachShader(programRef, vertexShaderRef)
        GL.glAttachShader(programRef, fragmentShaderRef)
        # link vertex shader to fragment shader
        GL.glLinkProgram(programRef)
        # query if linking was successful
        linkSuccess = GL.glGetProgramiv(programRef, GL.GL_LINK_STATUS)

        if not linkSuccess:
            # retrive error message
            errorMessage = GL.glGetProgramInfoLog(programRef)
            # free memory used to store program 
            GL.glDeleteProgram(programRef)
            # convert byte string to character string
            errorMessage = "\n" + errorMessage.decode("utf-8")
            # raise exception, halt program, print error message
            raise Exception(errorMessage)
        # linking was successful, returtn program reference
        return programRef









