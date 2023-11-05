from pico2d import *

class StateMachine:
    pass

class Hitter:
    def __init__(self):
        self.x, self.y = 400, 100
        self.frame = 0
        self.action = 3 # ?
        self.image = load_image('Hitter.png')
