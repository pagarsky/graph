from utilities.globals import circles, batch, lines

import pyglet

CHEMISTRY = 0
POLYGONS = 1

def connect_all(mode: int):
    _map = {CHEMISTRY : connect_chemistry,
            POLYGONS  : connect_polygons}

    _map[mode]()


def connect_chemistry():
    global circles, batch, lines
    connected = set()

    for node in circles:
        for other in node.neighbors:
            if other not in connected:
                line = pyglet.shapes.Line(node.x, node.y, other.x, other.y)
                line.draw()
                connected.add(other)


def connect_polygons():
    global circles, batch, lines
    connected = set()

    for node in circles:
        for other in node.neighbors:
            if (node, other) not in connected:
                vertex_list = pyglet.graphics.vertex_list(2,
                    ('v2f', (node.x, node.y, other.x, other.y))
                )
                vertex_list.draw(pyglet.gl.GL_LINES)
                vertex_list.delete()
                # lines.append(
                # batch.add(2, pyglet.gl.GL_LINES, None,
                #     ('v2f', (node.x, node.y, other.x, other.y))
                # )
                # )
                # line = pyglet.shapes.Line(node.x, node.y, other.x, other.y)
                # line.draw()
                connected.add((node, other))