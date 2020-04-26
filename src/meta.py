from typing import Iterable

from src.base import RenderableObjectBase


class ObjectList(RenderableObjectBase):
    def __init__(self, objects: Iterable[RenderableObjectBase]):
        self._objects = objects

    def render(self) -> None:
        [obj.render() for obj in self._objects]
