import pyglet
import random
import glob
from enum import Enum
from typing import Tuple

from pyglet.window.key import LEFT, RIGHT, UP, DOWN, LCTRL
from pyglet.window.mouse import LEFT as MouseLEFT

import pyglet.window.key
import pyglet.window.mouse

window = pyglet.window.Window(width=1500, height=800)
batch = pyglet.graphics.Batch()  # pro optimalizované vyreslování objektů

class MeteorColor(Enum):
    BROWN = 1
    GREY = 2

class MeteorSize(Enum):
    TINY = 1
    SMALL = 2
    MEDIUM = 3
    BIG = 4

class Spaceobject():
    speed_x = 0 #rychlost ve směru osy x
    speed_y = 0
    def __init__(self, image_path, speed: Tuple[int, int] = (0,0), position: Tuple[int, int] = (0,0)):
          
        self.speed_x = speed[0]
        self.speed_y = speed[1]

        self.img = pyglet.image.load(image_path)
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2

        self.sprite = pyglet.sprite.Sprite(self.img, batch = batch)
        self.sprite.x = position[0]
        self.sprite.y = position[1]
  
    def move(self, dt:float):
        self.sprite.x += self.speed_x * dt * 10
        self.sprite.y += self.speed_y * dt * 10

class Meteor(Spaceobject):
    color_dict = {MeteorColor.BROWN: "Brown", MeteorColor.GREY: "Grey"}
    size_dict = {MeteorSize.TINY: "tiny", MeteorSize.SMALL: "small", MeteorSize.MEDIUM: "med", MeteorSize.BIG: "big"}

    def __init__(self, size: MeteorSize, color: MeteorColor, variant: int, speed: Tuple[int, int] = (0,0), position: Tuple[int, int] = (0,0)):
        super().__init__(f"pokrocile/7 spacegame/img/meteor{self.color_dict[color]}_{self.size_dict[size]}{variant}.png", speed)

class BrownMeteor(Meteor):
    def __init__(self, size, variant=1, speed=(0,0), position=(0,0)):
        super().__init__(size, MeteorColor.BROWN, variant, speed, position)

class GreyMeteor(Meteor):
    def __init__(self, size, variant=1, speed=(0,0), position=(0,0)):
        super().__init__(size, MeteorColor.GREY, variant, (speed[0] * 2, speed[1] * 1.5), position)

objects = []

for i in range(15):
    objects.append(
        Meteor(random.choice(list(MeteorSize)),
         random.choice(list(MeteorColor)),
         random.randint(1,2),
          (random.randint(0,10), random.randint(0,10)), 
           (random.randint(0,200), random.randint(0,200))))

@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(sym, mod):
    print(sym, mod)


@window.event
def on_key_release(sym, mod):
    print(sym, mod)


@window.event
def on_mouse_press(x, y, button, mod):
    print(x, y, button)


def tick(dt):
    for item in objects:
        item.move(dt)
    # print(dt)


# funkce tick se spustí 30x za sekundu
pyglet.clock.schedule_interval(tick, 1 / 30)

# nekonečná smyčka ve které se čeká na události, které se následně obsluhují
pyglet.app.run()