import game_framework
from pico2d import *
from sdl2 import SDL_KEYDOWN, SDLK_SPACE

import game_world
import title_mode
from score_board_background import ScoreBoardBackground


def init():
    global background
    global logo_start_time
    global information_continue
    global continue_button_flag

    logo_start_time = get_time()

    background = ScoreBoardBackground()
    game_world.add_object(background, 0)

    information_continue = Information()
    continue_button_flag = False


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    global continue_button_flag
    game_world.update()
    # delay(0.5)
    if get_time() - logo_start_time >= 2.0 and continue_button_flag == False:
        game_world.add_object(information_continue, 2)
        continue_button_flag = True


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass


def resume(): pass


class Score_calculator:
    def __init__(self):
        # self.charging = 0
        self.hit_x = 0.0
        self.hit_y = 0.0
        self.ball_x = 0.0
        self.ball_y = 0.0
        self.ball_size = 0.0

        self.max = 100.0

        self.result = 0.0

    def culculating(self):
        self.result = ((self.max - abs(self.ball_x - self.hit_x)) + (self.max - abs(self.ball_y - self.hit_y))
                       + (2 * (56 - abs(56 - self.ball_size))))
        self.result = round(self.result)
        print(f"{abs(self.ball_x - self.hit_x)} // {abs(self.ball_y - self.hit_y)} // {10 * abs(56 - self.ball_size)}")

class Information:
    def __init__(self):
        self.image = load_image('press_space_bar_to_continue.png')
        self.frame = 0
        self.action = 0
        self.y = 110
        self.y_pattern = [ 103, 96, 89, 110 ]
        self.pattern_index = 0

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.y = self.y_pattern[self.pattern_index]
        self.pattern_index = (self.pattern_index + 1) % len(self.y_pattern)

    def handle_event(self):
        pass

    def draw(self):
        self.image.clip_draw(0, self.frame * 180, 1280, 180, 640, self.y, 500, 80)