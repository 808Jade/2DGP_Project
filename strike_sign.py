import game_world
import pitcher
from pico2d import *

def sign_time_out(e):
    return e[0] == 'SWING_TIME_OUT'


class Ballsign:
    def __init__(self):
        self.image = load_image('BALL_sign.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 428, 70, 70)


class Strikesign:
    def __init__(self):
        self.x, self.y = 650, 600
        self.image = load_image('STRIKE.png')
        self.wait_time = 0

    def sign_on(self):
        self.wait_time = get_time()
        self.image.draw(650, 600, 190, 100)
        if get_time() - pitcher.wait_time > 1:
            game_world.remove_object(self)
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(650, 600, 190, 100)