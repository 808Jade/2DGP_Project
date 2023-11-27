from pico2d import *

class Strike_counter:
    def __init__(self):
        self.image_0 = load_image('strike_counter_000.png')
        self.image_1 = load_image('strike_counter_100.png')
        self.image_2 = load_image('strike_counter_110.png')
        self.image_3 = load_image('strike_counter_111.png')
        self.x, self.y = 100, 100 # mac 환경이라 좌표 변경 필요함..
        self.size_x, self.size_y = 200, 100
        self.count = 0

    def draw(self):
        if self.count == 0:
            self.image_0.draw(self.x, self.y, self.size_x, self.size_y)
        elif self.count == 1:
            self.image_1.draw(self.x, self.y, self.size_x, self.size_y)
        elif self.count == 2:
            self.image_2.draw(self.x, self.y, self.size_x, self.size_y)
        elif self.count == 3:
            self.image_3.draw(self.x, self.y, self.size_x, self.size_y)

    def update(self):
        if self.count == 0:
            self.image_0.draw(self.x, self.y, self.size_x, self.size_y)
        elif self.count == 1:
            self.image_1.draw(self.x, self.y, self.size_x, self.size_y)
        elif self.count == 2:
            self.image_2.draw(self.x, self.y, self.size_x, self.size_y)
        elif self.count == 3:
            self.image_3.draw(self.x, self.y, self.size_x, self.size_y)