from pico2d import *
import game_framework

import game_world
import title_mode
from hitter import Hitter
from pitcher_hell import Pitcher
from playground_hell import Playground
from strike_zone import Strike_zone


# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            hitter.handle_event(event)


def init():
    global background
    global hitter
    global pitcher_hell
    global  strke_zone

    playground = Playground()
    game_world.add_object(playground, 0)

    hitter = Hitter()
    game_world.add_object(hitter, 1)

    pitcher_hell = Pitcher()
    game_world.add_object(pitcher_hell, 1)

    strike_zone = Strike_zone()
    game_world.add_object(strike_zone, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
