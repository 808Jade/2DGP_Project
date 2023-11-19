from pico2d import *


# ---state event check

def entering_time_out(e):
    return e[0] == 'ENTERING_TIME_OUT'


def swing_time_out(e):
    return e[0] == 'SWING_TIME_OUT'


def left_click(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_LEFT


def right_click(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].button == SDL_BUTTON_RIGHT


def right_click_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].button == SDL_BUTTON_RIGHT


def mouse_motion(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEMOTION

# ---state event check


class Entering:
    @staticmethod
    def enter(hitter, e):
        hitter.wait_time = get_time()
        pass

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(hitter):
        hitter.frame = (hitter.frame + 1) % 6
        hitter.dir = 0.1
        hitter.x += hitter.dir * 100
        hitter.action = 3
        if get_time() - hitter.wait_time > 2:
            hitter.state_machine.handle_event(('ENTERING_TIME_OUT', 0))
        # print("Entering do")
        pass

    @staticmethod
    def draw(hitter):
        hitter.image.clip_draw(hitter.frame * 170, hitter.action * 170, 170, 170, hitter.x, hitter.y, 500, 500)


class Idle:
    @staticmethod
    def enter(hitter, e):
        pass

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(hitter):
        hitter.frame = (hitter.frame + 1) % 3
        hitter.action = 6
        # print("idle do")
        pass

    @staticmethod
    def draw(hitter):
        hitter.image.clip_draw(hitter.frame * 170, hitter.action * 170, 170, 170, hitter.x, hitter.y, 500, 500)
        pass


class Swing:
    @staticmethod
    def enter(hitter, e):
        hitter.wait_time = get_time()
        hitter.swing_x, hitter.swing_y = e[1].x, 720 - e[1].y
        print(hitter.swing_x, hitter.swing_y)
        pass

    @staticmethod
    def exit(hitter, e):
        hitter.swing_x = 0
        hitter.swing_y = 0
        pass

    @staticmethod
    def do(hitter):
        hitter.frame = (hitter.frame + 1) % 6
        hitter.action = 5
        if get_time() - hitter.wait_time > 0.25:
            hitter.state_machine.handle_event(('SWING_TIME_OUT', 0))
        pass

    @staticmethod
    def draw(hitter):
        hitter.image.clip_draw(hitter.frame * 170, hitter.action * 170, 170, 170, hitter.x, hitter.y, 500, 500)
        pass


class Charging:
    @staticmethod
    def enter(hitter, e):
        pass

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(hitter):
        hitter.frame = (hitter.frame + 1) % 3
        hitter.action = 0
        pass

    @staticmethod
    def draw(hitter):
        hitter.image.clip_draw(hitter.frame * 170, hitter.action * 170, 170, 170, hitter.x, hitter.y, 500, 500)
        pass


class Moving:
    @staticmethod
    def enter(hitter, e):
        pass

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(hitter):
        hitter.frame = (hitter.frame + 1) % 6
        hitter.action = 6
        pass

    @staticmethod
    def draw(hitter):
        hitter.image.clip_draw(hitter.frame * 170, hitter.action * 170, 170, 170, hitter.x, hitter.y, 500, 500)
        pass

class StateMachine:
    def __init__(self, hitter):
        self.hitter = hitter
        self.cur_state = Entering
        self.transitions = {
            Idle: {left_click: Swing, right_click: Charging},
            Entering: {entering_time_out: Idle},
            Swing: {swing_time_out: Idle},
            Charging: {left_click: Swing, right_click_up: Idle},
        }

    def start(self):
        self.cur_state.enter(self.hitter, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.hitter)
        pico2d.delay(0.05)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.hitter, e)
                self.cur_state = next_state
                self.cur_state.enter(self.hitter, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.hitter)


class Hitter:
    def __init__(self):
        self.x, self.y = -100, 250
        self.frame = 0
        self.action = 7
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('Hitter.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.swing_x, self.swing_y = 0, 0

    def swing_point(self):
        return self.swing_x, self.swing_y, self.swing_x + 20, self.swing_y + 20

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.swing_point())

    def handle_collision(self, group, other):
        pass
