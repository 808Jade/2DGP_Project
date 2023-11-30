from pico2d import *


class ContinueButton:
    def __init__(self):
        self.image = load_image('press_space_bar_to_continue.png')
        self.frame = 0
        self.action = 0
        self.y = 110
        self.y_pattern = [ 103, 96, 89, 110 ]
        self.pattern_index = 0

    def update(self):
        delay(0.1)
        self.frame = (self.frame + 1) % 4
        self.y = self.y_pattern[self.pattern_index]
        self.pattern_index = (self.pattern_index + 1) % len(self.y_pattern)

    def handle_event(self):
        pass

    def draw(self):
        self.image.clip_draw(0, self.frame * 180, 1280, 180, 640, self.y, 500, 80)
