from pico2d import *

class Playground:
    def __init__(self):
        self.image = load_image('background_play.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 360)