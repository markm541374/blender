import bpy
import sys

sys.path.append("/home/mark/PycharmProjects/blender")

from src.shapes import CuboidConfig, Cuboid
from src.meta import ObjectList
from src.utils import Float3D

a = Float3D([1.0, 0.0, 0.0])
render_object = ObjectList(
    Cuboid(
        CuboidConfig(origin=Float3D([idx, 0.0, 0.0]), size=Float3D([0.5, idx, idx]),)
    )
    for idx in range(100)
)


bpy.ops.object.delete()
render_object.render()
