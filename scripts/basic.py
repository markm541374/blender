import bpy

bpy.ops.mesh.primitive_cube_add(radius=2, location=(0, 0, 0))
bpy.ops.transform.rotate(value=-0.261911, axis=(0, 0, 1))
bpy.ops.object.modifier_add(type="BEVEL")
