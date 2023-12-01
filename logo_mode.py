from pico2d import *

import game_framework
import game_world
import title_mode


def init():
    global image
    global logo_start_time
    image = load_image('logo.png')
    logo_start_time = get_time()


def finish():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(title_mode)
        elif event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_QUIT:
            game_framework.quit()


def update():
    pass


def draw():
    clear_canvas()
    image.draw(640, 360)
    update_canvas()


def pause(): pass


def resume(): pass
