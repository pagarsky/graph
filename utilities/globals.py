import pyglet
from .config import window_width, window_height, FULLSCREEN

window_config = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(window_width, window_height, fullscreen=FULLSCREEN, config=window_config)
batch = pyglet.graphics.Batch()

circles = []