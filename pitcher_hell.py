from pico2d import *

import game_world
from ball_hell import Ball_HELL


# ---state event check

def entering_time_out(e):
    return e[0] == 'ENTERING_TIME_OUT'


def idle_time_out(e):
    return e[0] == 'IDLE_TIME_OUT'


def pitching_time_out(e):
    return e[0] == 'PITCHING_TIME_OUT'


# ---state event check


class Entering:
    @staticmethod
    def enter(pitcher, e):
        pass

    @staticmethod
    def exit(pitcher, e):
        pass

    @staticmethod
    def do(pitcher):
        pitcher.frame = (pitcher.frame + 1) % 4
        pitcher.dir -= 0.01
        pitcher.x += pitcher.dir * 100
        pitcher.action = 5
        if pitcher.x <= 639.0:
            pitcher.state_machine.handle_event(('ENTERING_TIME_OUT', 0))

    @staticmethod
    def draw(pitcher):
        pitcher.image.clip_composite_draw(pitcher.frame * 128, pitcher.action * 128, 128, 128, 0, 'h', pitcher.x,
                                          pitcher.y, 80, 80)


class Idle:
    @staticmethod
    def enter(pitcher, e):
        pitcher.wait_time = get_time()

    @staticmethod
    def exit(pitcher, e):
        pass

    @staticmethod
    def do(pitcher):
        pitcher.frame = (pitcher.frame + 1) % 4
        pitcher.action = 5
        if get_time() - pitcher.wait_time > 2:
            pitcher.state_machine.handle_event(('IDLE_TIME_OUT', 0))

    @staticmethod
    def draw(pitcher):
        pitcher.image.clip_draw(pitcher.frame * 128, pitcher.action * 128, 128, 128, pitcher.x, pitcher.y, 80, 80)


class Pitching:
    @staticmethod
    def enter(pitcher, e):
        pitcher.wait_time = get_time()
        pitcher.pitching()

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(pitcher):
        pitcher.frame = (pitcher.frame + 1) % 16
        pitcher.action = 5
        if get_time() - pitcher.wait_time > 1:
            pitcher.state_machine.handle_event(('PITCHING_TIME_OUT', 0))

    @staticmethod
    def draw(pitcher):
        pitcher.image.clip_draw(pitcher.frame * 128, pitcher.action * 128, 128, 128, pitcher.x, pitcher.y, 80, 80)


class StateMachine:
    def __init__(self, pitcher):
        self.pitcher = pitcher
        self.cur_state = Entering
        self.transitions = {
            Idle: {idle_time_out: Pitching},
            Entering: {entering_time_out: Idle},
            Pitching: {pitching_time_out: Idle}
        }

    def start(self):
        self.cur_state.enter(self.pitcher, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pitcher)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pitcher, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pitcher, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.pitcher)


class Pitcher:
    def __init__(self):
        self.x, self.y = 1380, 410
        self.frame = 0
        self.action = 15
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('penguin.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.pitching_sound = load_wav('pitching_sound.wav')
        self.pitching_sound.set_volume(50)

    def pitching(self):
        self.pitching_sound.play(1)
        ball = Ball_HELL(self.x + 30, self.y)
        game_world.add_object(ball, 2)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
