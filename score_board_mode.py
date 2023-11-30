import game_framework
from pico2d import *
from sdl2 import SDL_KEYDOWN, SDLK_SPACE

import game_world
import title_mode
from continue_button import ContinueButton
from score_board_background import ScoreBoardBackground


def init():
    global background
    global logo_start_time
    global information_continue
    global continue_button_flag

    logo_start_time = get_time()

    background = ScoreBoardBackground()
    game_world.add_object(background, 0)

    information_continue = ContinueButton()
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


class ShowScore:
    def __init__(self):
        self.hit_count = 0
        self.total_score = 0
        pass

    def update(self):
        pass

    def handle_event(self):
        pass

    def draw(self):
        pass