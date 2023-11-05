from pico2d import *
import game_framework

import play_mode_easy
import logo_mode as start_mode
import title_mode

open_canvas(1280, 720)
game_framework.run(start_mode)
close_canvas()