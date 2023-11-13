from pico2d import *


class Playground:
    def __init__(self):
        self.image = load_image('background_play_hell.png')

    def draw(self):
        self.image.draw(640, 360)

    def update(self):
        pass
