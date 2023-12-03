from pico2d import *


class Playground:
    def __init__(self):
        self.image = load_image('background_play.png')
        self.x = 640
        self.y = 360

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.image.draw(self.x, self.y)
        