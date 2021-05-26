import math

import pyglet

from utilities.config import window_threshold, CONNECTION_DISTANCE

class Node:

    def __init__(
        self,
        batch,
        x: int = 0,
        y: int = 0,
        r: int = 1
    ):
        self._circle = pyglet.shapes.Circle(x=x, y=y, radius=r, batch=batch)
        self.radius = r
        self.speed = [0, 0]
        self.neighbors = set()

    def set_coords(self, x: int, y: int):
        self._circle.x = x
        self._circle.y = y

    def set_speed(self, x: int = 0, y: int = 0):
        self.speed = [x, y]

    def change_speed_by(self, x: int = 0, y: int = 0):
        self.speed[0] += x
        self.speed[1] += y

    def move(self, dt: float):
        self._circle.x += self.speed[0] * dt
        self._circle.y += self.speed[1] * dt

    def keep_in_bounds(self, width: int, height: int):
        self._circle.x = self._clip_bounds(self._circle.x, width)
        self._circle.y = self._clip_bounds(self._circle.y, height)

    def distance_to(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    @property
    def x(self) -> float:
        return self._circle.x

    @property
    def y(self) -> float:
        return self._circle.y

    def _clip_bounds(self, param: float, limit: int) -> float:
        param = -window_threshold if param > limit + window_threshold else param

        return limit + window_threshold if param < -window_threshold else param
