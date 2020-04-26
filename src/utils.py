from typing import Tuple, Union, List
import numpy as np


class Float3D:
    def __init__(self, value):
        self._value = np.array(value)
        if not self._value.shape == (3,):
            raise ValueError("must be 3vector")

    def __repr__(self):
        return f"Float3D([{list(self._value)}])"
    @property
    def x(self):
        return self._value[0]

    @property
    def y(self):
        return self._value[1]

    @property
    def z(self):
        return self._value[2]

    def as_tuple(self) -> Tuple[float, float, float]:
        return self.x, self.y, self.z

    def __truediv__(self, other: float) -> "Float3D":
        return Float3D(self._value / other)

    def __sub__(self, other: "Float3D") -> "Float3D":
        if not isinstance(other, Float3D):
            raise TypeError
        return Float3D(self._value - other._value)

    def __add__(self, other: "Float3D") -> "Float3D":
        if not isinstance(other, Float3D):
            raise TypeError
        return Float3D(self._value + other._value)

    def __abs__(self):
        return np.linalg.norm(self._value)
