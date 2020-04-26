import bpy
import sys


sys.path.append("/home/mark/PycharmProjects/blender")
bpy.ops.object.delete()


from src.features import WallConfig, Wall, WallSegmentConfig, WallChain
from src.utils import Float3D

def test_single_wall_alignment():
    walls=[]
    walls.append(Wall(WallConfig(
        start=Float3D([1, 5, 2]), end=Float3D([7, 5, 2]), thickness=0.5, height=4
    )))

    walls.append(Wall(WallConfig(
        start=Float3D([1, 5, 2]), end=Float3D([-6, 5, 2]), thickness=0.5, height=3
    )))
    walls.append(Wall(WallConfig(
        start=Float3D([1, 5, 2]), end=Float3D([1, 9, 2]), thickness=1.5, height=3
    )))
    walls.append(Wall(WallConfig(
        start=Float3D([1, 5, 2]), end=Float3D([1, 2, 2]), thickness=1.5, height=3
    )))



    [wall.render() for wall in walls]

def test_wall_sequence():
    config = WallSegmentConfig(chain=[(Float3D([0, 0, 0]), 0.25, 4),
                                             (Float3D([0, 5, 0]), 0.5, 4),
                                             (Float3D([7, 5, 0]), 0.25, 4),
                                             (Float3D([7, 6, 0]), 0.25, 4),
                                             (Float3D([8, 6, 0]), 0.25, 6),
                                             (Float3D([8, 0, 0]), 0.25, 4),
                                             ])
    walls = WallChain(config)
    walls.render()


# test_single_wall_alignment()
test_wall_sequence()
