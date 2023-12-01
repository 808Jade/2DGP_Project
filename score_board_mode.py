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
    global score_calculator_flag

    logo_start_time = get_time()

    background = ScoreBoardBackground()
    game_world.add_object(background, 0)

    information_continue = ContinueButton()
    continue_button_flag = False

    score_calculator_flag = 0

    if title_mode.score_calculator.rank == 'S':
        title_mode.score_calculator.S_bgm.play()
    elif title_mode.score_calculator.rank == 'A':
        title_mode.score_calculator.A_bgm.play()
    elif title_mode.score_calculator.rank == 'B':
        title_mode.score_calculator.B_bgm.play()
    elif title_mode.score_calculator.rank == 'C':
        title_mode.score_calculator.C_bgm.play()
    elif title_mode.score_calculator.rank == 'DE':
        title_mode.score_calculator.DE_bgm.play()
    elif title_mode.score_calculator.rank == 'F':
        title_mode.score_calculator.F_bgm.play()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    global continue_button_flag
    global score_calculator_flag

    game_world.update()

    if get_time() - logo_start_time >= 3.0 and continue_button_flag == False:
        game_world.add_object(information_continue, 2)
        continue_button_flag = True
    if get_time() - logo_start_time >= 0.5 and score_calculator_flag == 0:
        game_world.add_object(title_mode.score_calculator, 3)
        score_calculator_flag = 1


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()


def pause(): pass


def resume(): pass