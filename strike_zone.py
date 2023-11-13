from pico2d import *


class Strike_zone:
    def __init__(self):
        self.image = load_image('Strike_zone.png')

    def draw(self):
        self.image.draw(635, 220, 250, 300)

    def update(self):
        pass