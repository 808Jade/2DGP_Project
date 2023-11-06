from pico2d import *
import game_framework

import game_world
from hitter import Hitter
from pitcher import Pitcher
from playground import Playground

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            hitter.handle_event(event)


def init():
    global background
    global hitter
    # global pitcher


    playground = Playground()
    game_world.add_object(playground, 0)

    hitter = Hitter()
    game_world.add_object(hitter, 1)

    # pitcher = Pitcher()
    # game_world.add_object(pitcher, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    delay(0.05)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass