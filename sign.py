import random

from pico2d import *

import game_framework
import game_world
import score_board_mode


class Ballsign:
    def __init__(self):
        self.x, self.y = 650, 600
        self.image = load_image('Ball_sign.png')
        self.wait_time = 0

    def sign_on(self):
        self.wait_time = get_time()
        self.image.draw(self.x, self.y, 190, 100)

    def update(self):
        if get_time() - self.wait_time > 1:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y, 190, 100)


class Strikesign:
    def __init__(self):
        self.x, self.y = 650, 600
        self.image = load_image('STRIKE.png')
        self.wait_time = 0

    def sign_on(self):
        self.wait_time = get_time()
        self.image.draw(self.x, self.y, 190, 100)

    def update(self):
        if get_time() - self.wait_time > 1:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y, 190, 100)


class Outsign:
    def __init__(self):
        self.x, self.y = 650, 500
        self.image = load_image('out.png')
        self.frame = 0
        self.action = 0
        self.wait_time = 0

    def sign_on(self):
        self.wait_time = get_time()
        self.image.draw(self.x, self.y, 290, 180)

    def update(self):
        if get_time() - self.wait_time > 2:
            game_world.remove_object(self)
            game_framework.change_mode(score_board_mode)

    def draw(self):
        self.image.draw(self.x, self.y, 290, 180)


class Scoresign:
    def __init__(self):
        self.x, self.y = random.randint(850, 1000), random.randint(450, 500)
        self.score = 0
        self.wait_time = 0
        self.size = 100
        self.font_rgb = [0, 0, 0]

    def sign_on(self):
        self.wait_time = get_time()
        if self.score < 280:
            self.font_rgb = [0, 153, 0]
            self.size = 100
        elif 280 <= self.score < 290:
            self.font_rgb = [0, 0, 250]
            self.size = 140
        elif 290 <= self.score < 300:
            self.font_rgb = [205, 0, 0]
            self.size = 180
        elif 300 <= self.score:
            self.font_rgb = [255, 204, 0]
            self.size = 220

        self.font_num = load_font('Lobster.ttf', self.size)

    def update(self):
        self.y += 5
        if get_time() - self.wait_time > 1:
            game_world.remove_object(self)

    def draw(self):
        self.font_num.draw(self.x, self.y, f'{self.score}', (self.font_rgb))
