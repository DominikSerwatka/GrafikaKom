from core.mesh import Mesh
from geometry.geometry import Geometry
from materials.lineBasicMaterial import LineBasicMaterial

class GridHleper(Mesh):

    def __init__(self,size=10,divisions=10, lineWidth=4, gridColor=[1,1,1], centerColor=[1,1,0]):
        geo = Geometry()
        posData = []
        colData = []
        # creat range of values
        values = []
        deltaSize = size/divisions
        for n in range(divisions+1):
            values.append(-size/2+n*deltaSize)
        # add vertical lines
        for x in values:
            posData.append([x, -size/2, 0])
            posData.append([x, size/2, 0])
            if x == 0:
                colData.append(centerColor)
                colData.append(centerColor)  
            else:
                colData.append(gridColor)
                colData.append(gridColor)

        # add horizontal lines
        for y in values:
            posData.append([-size/2, y, 0])
            posData.append([ size/2, y, 0])
            if y == 0:
                colData.append(centerColor)
                colData.append(centerColor)  
            else:
                colData.append(gridColor)
                colData.append(gridColor)
        geo.addAttribute("vec3", "vertexPosition", posData)
        geo.addAttribute("vec3", "vertexColor", colData)
        geo.countVertices()

        mat = LineBasicMaterial({
            "useVertexColors":1,
            "lineWidth":lineWidth,
            "lineType":"segments"
        })    
        super().__init__(geo, mat)
        
