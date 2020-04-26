from typing import Optional, List, Tuple

from src.base import RenderableObjectBase
from src.meta import ObjectList
from src.shapes import Cuboid, CuboidConfig
from src.utils import Float3D


class WallConfig:
    def __init__(self, start: Float3D, end: Float3D, thickness: float, height: float):
        # Thickness extends to the right travelling from start to end
        self.start = start
        self.end = end
        self.thickness = thickness
        self.height = height

        if not start.z == end.z:
            raise ValueError("Walls must start and end at teh same height")
        if start.x != end.x and start.y != end.y:
            raise ValueError("Walls cannot be diagonal")

    def __repr__(self):
        return f"WallConfig(start={self.start}, end={self.end}, thickness={self.thickness}, height={self.height})"


class Wall(RenderableObjectBase):
    def __init__(self, config: WallConfig):
        cuboid_config = self._cuboid_config_from_wall(config)
        print(cuboid_config)
        self._cuboid = Cuboid(cuboid_config)

    def render(self) -> None:
        self._cuboid.render()

    def _cuboid_config_from_wall(self, config: WallConfig) -> CuboidConfig:
        length = abs(config.end - config.start)
        north_south_aligned = config.start.y != config.end.y

        if north_south_aligned:
            y_size = length
            x_size = config.thickness
            going_north = config.start.y < config.end.y

            if going_north:
                y_origin = config.start.y
                x_origin = config.start.x
            else:
                x_origin = config.start.x - config.thickness
                y_origin = config.end.y

        else:
            y_size = config.thickness
            x_size = length

            going_east = config.end.x > config.start.x
            if going_east:
                y_origin = config.start.y - config.thickness
                x_origin = config.start.x
            else:
                y_origin = config.start.y
                x_origin = config.end.x

        return CuboidConfig(
            origin=Float3D([x_origin, y_origin, config.start.z]),
            size=Float3D([x_size, y_size, config.height + config.start.z]),
        )


class WallSegmentConfig:
    def __init__(
        self, chain: List[Tuple[Float3D, float, float]], end: Optional[Float3D] = None
    ):
        # Thickness extends to the right travelling from start to end
        self.chain = chain
        self.end = end


class WallChain(RenderableObjectBase):
    def __init__(self, config: WallSegmentConfig):
        self.config=config
        self._make_wall_sequence_from_config()
        self.walls = self._make_wall_sequence_from_config()

    def render(self) -> None:
        self.walls.render()

    def _make_wall_sequence_from_config(self) -> RenderableObjectBase:
        wall_configs = []
        for idx in range(len(self.config.chain) - 1):
            start, thickness, height = self.config.chain[idx]
            wall_configs.append(
                WallConfig(
                    start=start,
                    end=self.config.chain[idx + 1][0],
                    thickness=thickness,
                    height=height,
                )
            )
        final_end = self.config.end if self.config.end else self.config.chain[0][0]

        start, thickness, height = self.config.chain[-1]
        wall_configs.append(
            WallConfig(start=start, end=final_end, thickness=thickness, height=height,)
        )
        return ObjectList(Wall(conf) for conf in wall_configs)
