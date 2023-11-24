import game_world
from pico2d import *


def sign_time_out(e):
    return e[0] == 'SWING_TIME_OUT'


class Ballsign:
    def __init__(self):
        self.x, self.y = 650, 600
        self.image = load_image('Ball_sign.png')
        self.wait_time = 0

    def sign_on(self):
        self.wait_time = get_time()
        self.image.draw(650, 600, 190, 100)

    def update(self):
        if get_time() - self.wait_time > 1:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(650, 600, 190, 100)


class Strikesign:
    def __init__(self):
        self.x, self.y = 650, 600
        self.image = load_image('STRIKE.png')
        self.wait_time = 0

    def sign_on(self):
        self.wait_time = get_time()
        self.image.draw(650, 600, 190, 100)

    def update(self):
        if get_time() - self.wait_time > 1:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(650, 600, 190, 100)