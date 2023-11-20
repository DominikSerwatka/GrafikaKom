from core.matrix import Matrix

class Object3D(object):
    def __init__(self):
        self.transform = Matrix.makeIdentity()
        self.parent = None
        self.children = []
    def add(self, child):
        self.children.append(child)
        child.parent = self
    def remove(self, child):
        self.children.remove(child)
        child.parent = None
    # calculate transforamation of this object3D relative
    # to the root Object3D of the scene graph
    def getWorldMatrix(self):
        if self.parent == None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @ self.transform
    # return a single list containing all descendants
    def getDescendentList(self):
        # master list of all descendant nodes
        descendants = []
        # nodes to be added to descendants list,
        # whose chidren will be added to this list 
        nodesToPorcess = [self]
        # continue processing nodes while any left in the list 
        while len(nodesToPorcess) > 0:
            # remove first node from list
            node = nodesToPorcess.pop(0)
            # add node to descendant list 
            descendants.append(node)
            # children of this node must also be processed
            nodesToPorcess = node.children + nodesToPorcess
        return descendants
    # apply geometric transforamtions
    def applyMatrix(self, matrix, loclaCoord=True):
        if loclaCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def translate(self, x, y, z, localCoord = True):
        m = Matrix.makeTranslation(x, y, z)
        self.applyMatrix(m, localCoord)

    def rotateX(self, angle, localCoord = True):
        m = Matrix.makeRotationX(angle)
        self.applyMatrix(m, localCoord)

    def rotateY(self, angle, localCoord = True):
        m = Matrix.makeRotationY(angle)
        self.applyMatrix(m, localCoord)

    def rotateZ(self, angle, localCoord = True):
        m = Matrix.makeRotationZ(angle)
        self.applyMatrix(m, localCoord)

    def scale(self, s, localCoord = True):
        m = Matrix.makeScale(s)
        self.applyMatrix(m, localCoord)
    # get/set position componets of transform
    def getPosition(self):
        return [self.transform.item((0, 3)),
                self.transform.item((1, 3)),
                self.transform.item((2 ,3))]
    def setPosition(self, x, y, z):
        self.transform.itemset((0,3), x)
        self.transform.itemset((1,3), y)
        self.transform.itemset((2,3), z)
        


    
        




    