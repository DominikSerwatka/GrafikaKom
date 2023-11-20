from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh

from core.texture import Texture
from geometry.rectangleGeometry import RectangleGeometry
from geometry.sphereGeometry import SphereGeometry
from materials.textureMaterial import TextureMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHleper
# render a scene

class Test(Base):
    def initialize(self):
        print("initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()
        # pull camera towards viewer
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition(0,1,3)
        # self.camera.setPosition(0, 0, 4)
        geometry = RectangleGeometry()
        tex = Texture("image/redWave.png")
        material = TextureMaterial(tex)
        
        self.mesh = Mesh(geometry, material)
        sphereGeometry = SphereGeometry()
        earthTex = Texture("image/earth.png")
        earthMaterial = TextureMaterial(earthTex)
        self.earth = Mesh(sphereGeometry, earthMaterial)
        self.earth.setPosition(0, 1, 0)
        self.scene.add(self.earth)

        skyGeometry = SphereGeometry(radius=100)
        skyMaterial = TextureMaterial(Texture("image/horizon.jpeg"))
        sky = Mesh(skyGeometry, skyMaterial)
        self.scene.add(sky)

        # self.scene.add(self.mesh)
        grid = GridHleper( gridColor=[0,0,0])
        grid.rotateX(3.14/2)
        self.scene.add(grid)
        
        


    def update(self):
        self.rig.updata(self.input, 1/60)
        self.earth.rotateY(0.01337)
        self.renderer.render(self.scene, self.camera)
# instantiate and run class
Test().run()



    