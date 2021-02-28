from utilities.globals import circles

import pyglet

CHEMISTRY = 0
POLYGONS = 1

def connect_all(mode: int):
    _map = {CHEMISTRY : connect_chemistry,
            POLYGONS  : connect_polygons}

    _map[mode]()


def connect_chemistry():
    global circles
    connected = set()

    for node in circles:
        for other in node.neightbors:
            if other not in connected:
                line = pyglet.shapes.Line(node.x, node.y, other.x, other.y)
                line.draw()
                connected.add(other)


def connect_polygons():
    global circles
    connected = set()

    for node in circles:
        for other in node.neightbors:
            if (node, other) not in connected:
                line = pyglet.shapes.Line(node.x, node.y, other.x, other.y)
                line.draw()
                connected.add((node, other))