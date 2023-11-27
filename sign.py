import game_framework
import game_world
from pico2d import *

import score_board_mode


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

class Outsign:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('out.png')
        self.frame = 0
        self.action = 0
        self.wait_time = 0

    def sign_on(self):
        self.wait_time = get_time()
        self.image.draw(650, 500, 290, 200)

    def update(self):
        if get_time() - self.wait_time > 2:
            game_framework.change_mode(score_board_mode)

    def draw(self):
        self.image.draw(650, 500, 290, 200)