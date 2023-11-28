import game_framework
from pico2d import *

import game_world
import title_mode


def init():
    global image
    global logo_start_time
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()


def finish():
    game_world.clear()


def handle_events():
    events = get_events()
    pass


def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.change_mode(title_mode)


def draw():
    clear_canvas()
    image.draw(640, 360)
    update_canvas()


def pause(): pass


def resume(): pass


class Score_calculator:
    def __init__(self):
        # self.charging = 0
        self.hit_x = 0
        self.hit_y = 0
        self.ball_x = 0
        self.ball_y = 0
        self.ball_size = 0
        pass

    def culculating(self):
        pass