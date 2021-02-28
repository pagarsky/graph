import random
import node

from utilities.globals import window, batch, circles
from utilities.config import window_width, window_height, circle_radius, amount
from utilities.config import CONNECTION_DISTANCE, RANDOM_SPEEDS, SPEED_RANGE, FPS
from utilities.config import DIVISOR as K

from modes import CHEMISTRY, POLYGONS, connect_all # TODO: rework naming or import for connect_all

import pyglet


def create_circles(amount: int = 15):
    for i in range(amount):
        x, y = random.randint(0, window_width), random.randint(0, window_height)

        circles.append(
            node.Node(batch, x, y, r=circle_radius)
        )


def set_speeds(x: int = None, y: int = None):
    for node in circles:
        node.set_speed(
            x if x else random.randint(*SPEED_RANGE) / K,
            y if y else random.randint(*SPEED_RANGE) / K
        )


def check_neighbors():
    l = len(circles)
    for i in range(l):
        this = circles[i]
        for j in range(i + 1, l):
            other = circles[j]
            if this.distance_to(other) < CONNECTION_DISTANCE:
                this.neightbors.add(other)
                other.neightbors.add(this)
            else:
                try:
                    this.neightbors.remove(other)
                    other.neightbors.remove(this)
                except KeyError:
                    pass


def tick(dt=0.1):
    if RANDOM_SPEEDS:
        for node in circles:
            node.change_speed_by(random.randint(*SPEED_RANGE) / K, random.randint(*SPEED_RANGE) / K)

    for node in circles:
        node.move(dt)
        node.keep_in_bounds(window_width, window_height)
    check_neighbors()
    connect_all(CHEMISTRY)


pyglet.clock.schedule_interval(tick, 1.0 / FPS)


@window.event
def on_draw():
    window.clear()
    batch.draw()

    tick()


if __name__ == '__main__':
    create_circles(amount)
    set_speeds()

    pyglet.app.run()