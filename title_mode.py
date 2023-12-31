from pico2d import *

import game_framework
import game_world
import play_mode_easy
import play_mode_hard
import play_mode_hell
import play_mode_normal
from score_calculator import ScoreCalculator


# 초기 화면 구성
def init():
    global background_menu, background_menu_hell, background_play, background_play_hell, menu_pick
    global easy, hard, normal, hell
    global menu_picking_easy, menu_picking_normal, menu_picking_hard, menu_picking_hell
    global prev_menu_picking_easy, prev_menu_picking_normal, prev_menu_picking_hard, prev_menu_picking_hell
    menu_picking_easy, menu_picking_normal, menu_picking_hard, menu_picking_hell = False, False, False, False
    prev_menu_picking_easy, prev_menu_picking_normal, prev_menu_picking_hard, prev_menu_picking_hell = False, False, False, False
    global canvas_x, canvas_y
    canvas_x, canvas_y = 1280, 720

    background_menu = load_image('background_menu.png')
    background_menu_hell = load_image('background_menu_hell.png')
    background_play = load_image('background_play.png')
    background_play_hell = load_image('background_play_hell.png')
    menu_pick = load_image('menu_pick.png')
    easy = load_image('EASY.png')
    hard = load_image('HARD.png')
    normal = load_image('NORMAL.png')
    hell = load_image('HELL.png')

    global background_bgm, volume, picking_bgm
    background_bgm = load_music('titlemode_background.mp3')
    volume = 20
    background_bgm.set_volume(volume)
    background_bgm.repeat_play()
    picking_bgm = load_wav('menu_pick.wav')
    picking_bgm.set_volume(volume + 20)

    global score_calculator
    score_calculator = ScoreCalculator()


def render_world():
    background_menu.draw(canvas_x // 2, canvas_y // 2)
    if menu_picking_hell == True:
        background_menu_hell.draw(canvas_x // 2, canvas_y // 2)
    if menu_picking_easy == True:
        menu_pick.draw(100, 350, menu_pick.w // 5, menu_pick.h // 11)
    elif menu_picking_normal == True:
        menu_pick.draw(100, 280, menu_pick.w // 5, menu_pick.h // 11)
    elif menu_picking_hard == True:
        menu_pick.draw(100, 210, menu_pick.w // 5, menu_pick.h // 11)
    elif menu_picking_hell == True:
        menu_pick.draw(100, 140, menu_pick.w // 5, menu_pick.h // 11)

    easy.draw(196, 350, easy.w // 5, easy.h // 5)
    normal.draw(198, 280, normal.w // 4, normal.h // 4)
    hard.draw(196, 210, hard.w // 5, hard.h // 5)
    hell.draw(196, 140, hell.w // 5, hell.h // 5)


def handle_events():
    global x, y
    global volume, background_bgm
    global menu_picking_easy, menu_picking_normal, menu_picking_hard, menu_picking_hell
    global prev_menu_picking_easy, prev_menu_picking_normal, prev_menu_picking_hard, prev_menu_picking_hell

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, canvas_y - 1 - event.y
            menu_picking_easy = 100 < x < 300 and 330 < y < 370
            menu_picking_normal = 100 < x < 300 and 260 < y < 300
            menu_picking_hard = 100 < x < 300 and 190 < y < 230
            menu_picking_hell = 100 < x < 300 and 120 < y < 160

            # 각각의 이전 상태가 False이고 현재 상태가 True일 때만 효과음 재생
            if not prev_menu_picking_easy and menu_picking_easy:
                picking_bgm.play(1)
                prev_menu_picking_easy = menu_picking_easy
            if not prev_menu_picking_normal and menu_picking_normal:
                picking_bgm.play(1)
            if not prev_menu_picking_hard and menu_picking_hard:
                picking_bgm.play(1)
            if not prev_menu_picking_hell and menu_picking_hell:
                picking_bgm.play(1)
            # 현재 메뉴 픽킹 상태를 이전 상태로 저장
            prev_menu_picking_easy, prev_menu_picking_normal, prev_menu_picking_hard, prev_menu_picking_hell = (
                menu_picking_easy, menu_picking_normal, menu_picking_hard, menu_picking_hell
            )

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_y - 1 - event.y
            if 100 < x < 300 and 330 < y < 370:
                background_bgm.stop()
                game_framework.change_mode(play_mode_easy)
            elif 100 < x < 300 and 260 < y < 300:
                background_bgm.stop()
                game_framework.change_mode(play_mode_normal)
            elif 100 < x < 300 and 190 < y < 230:
                background_bgm.stop()
                game_framework.change_mode(play_mode_hard)
            elif 100 < x < 300 and 120 < y < 160:
                background_bgm.stop()
                game_framework.change_mode(play_mode_hell)

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_EQUALS:  # '=' 키
                volume += 10
                background_bgm.set_volume(volume)
            elif event.key == SDLK_MINUS:  # '-' 키
                volume -= 10
                background_bgm.set_volume(volume)
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()


def update():
    game_world.update()


def draw():
    clear_canvas()
    render_world()
    update_canvas()


def finish():
    game_world.clear()


def pause(): pass


def resume(): pass
