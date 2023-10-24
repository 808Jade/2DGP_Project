# 개발 일정
# 1주차 : 리소스 스집
# 2주차 : 초기 화면 구성
# 3주차 : 타자 움직임 구현
# 4주차 : 투수, 공에 대한 구현
# 5주차 : 타격 구현
# 6주차 : 난이도 구현
# 7추자 : 타격 기록 구현
# 8주차 : 최종 점검

from pico2d import *


# 초기 화면 구성
def load_resources():
    global background_menu, background_menu_hell, background_play, background_play_hell, menu_pick
    global easy, hard, normal, hell
    global hitter, pitcher

    background_menu = load_image('background_menu.png')
    background_menu_hell = load_image('background_menu_hell.png')
    background_play = load_image('background_play.png')
    background_play_hell = load_image('background_play_hell.png')
    menu_pick = load_image('menu_pick.png')
    easy = load_image('EASY.png')
    hard = load_image('HARD.png')
    normal = load_image('NORMAL.png')
    hell = load_image('HELL.png')
    # hitter = load_image('Hitter.png')
    # pitcher = load_image('Pitcher.png)


def reset_world():
    global running
    running = True


def render_world():
    clear_canvas()
    background_menu.draw(canvas_x // 2, canvas_y // 2)
    easy.draw(196, 350, easy.w // 5, easy.h // 5)
    normal.draw(198, 280, normal.w // 4, normal.h // 4)
    hard.draw(196, 210, hard.w // 5, hard.h // 5)
    hell.draw(196, 140, hell.w // 5, hell.h // 5)

    # hard.draw()
    # hell.draw()
    update_canvas()

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, canvas_y - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

# main
canvas_x, canvas_y = 1280, 720
open_canvas(canvas_x, canvas_y)
load_resources()
reset_world()

while running:
    render_world()
    handle_events()

close_canvas()