import pyglet


def run():
    pyglet.app.run()


class Renderer:
    def __init__(self, width, height, title):
        self.window = pyglet.window.Window(width=width, height=height, caption=title)
        self.window.event(self.on_draw)

    def on_draw(self):
        self.window.clear()


if __name__ == "__main__":
    renderer = Renderer(width=800, height=600, title="Pyglet Application")
    run()
