import random
import node

from utilities.globals import window, batch
from utilities.config import window_width, window_height, circle_radius, amount, RANDOM_SPEEDS, SPEED_RANGE, FPS
from utilities.config import DIVISOR as K

import pyglet


circles = []
lines = []


def create_circles(amount: int = 15):
    global circles

    for i in range(amount):
        x, y = random.randint(0, window_width), random.randint(0, window_height)

        circles.append(
            node.Node(batch, x, y, r=circle_radius)
        )


def set_speeds(x: int = None, y: int = None):
    global circles

    for node in circles:
        node.set_speed(
            x if x else random.randint(*SPEED_RANGE) / K,
            y if y else random.randint(*SPEED_RANGE) / K
        )


def tick(dt=0.1):
    if RANDOM_SPEEDS:
        for node in circles:
            node.change_speed_by(random.randint(*SPEED_RANGE) / K, random.randint(*SPEED_RANGE) / K)

    for node in circles:
        node.move(dt)
        node.keep_in_bounds(window_width, window_height)


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