from geometry.geometry import Geometry

class ParametricGeometry(Geometry):
    def __init__(self, uStart, uEnd, uResolution, vStart, vEnd, vResolution, S):
        super().__init__()
        # generate a set of points on the function
        deltaU = (uEnd - uStart)/uResolution # resolution is number of points, delta is how large point is 
        deltaV = (vEnd - vStart)/vResolution

        positions = []
        uvs = []

        for uIndex in range(uResolution+1):
            vArray = []
            for vIndex in range(vResolution+1):
                u = uStart + uIndex * deltaU
                v = vStart + vIndex * deltaV
                vArray.append(S(u, v))
            positions.append(vArray)
        
        for uIndex in range(uResolution+1):
            vArray = []
            for vIndex in range(vResolution+1):
                u = uIndex/uResolution
                v = vIndex/vResolution
                vArray.append([u,v])
            uvs.append(vArray)

        # store vertex data
        positionData = []
        colorData = []
        uvData = []

        # default vertex colors
        C1, C2, C3 = [1,0,0], [0,1,0], [0,0,1]
        C4, C5, C6 = [0,1,1], [1,0,1], [1,1,0]
        # group vertex data into triangles
        for xIndex in range(uResolution):
            for yIndex in range(vResolution):
                # position data
                pA = positions[xIndex][yIndex]
                pB = positions[xIndex+1][yIndex]
                pC = positions[xIndex+1][yIndex+1]
                pD = positions[xIndex][yIndex+1]
                positionData += [pA, pB, pC, pA, pC, pD]
                colorData += [C1, C2, C3, C4, C5, C6]
                # uv coordinates
                uvA = uvs[xIndex][yIndex]
                uvB = uvs[xIndex+1][yIndex]
                uvC = uvs[xIndex+1][yIndex+1]
                uvD = uvs[xIndex][yIndex+1]
                uvData += [uvA, uvB, uvC, uvA, uvC, uvD]
        
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.addAttribute("vec2", "vertexUV", uvData)
        self.countVertices()



            

        
