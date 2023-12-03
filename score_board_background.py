from pico2d import *


class ScoreBoardBackground:
    def __init__(self):
        self.image = load_image('score_board.png')
        self.x = 640
        self.y = 360

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.image.draw(self.x, self.y)
        