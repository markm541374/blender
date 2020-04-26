import bpy

from src.base import RenderableObjectBase
from src.utils import Float3D


class CuboidConfig:
    def __init__(self, origin: Float3D, size: Float3D):
        self.origin = origin
        self.size = size

    def __repr__(self):
        return f"CuboidConfig(origin={self.origin}, size={self.size})"


class Cuboid(RenderableObjectBase):
    def __init__(self, config: CuboidConfig):
        self.config = config

    def __repr(self):
        return f"Cuboid({self.config})"
    def render(self):
        bpy.ops.mesh.primitive_cube_add(
            radius=0.5,
            location=(self.config.origin + self.config.size / 2.0).as_tuple(),
        )
        bpy.ops.transform.resize(value=self.config.size.as_tuple())
