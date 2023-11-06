from pico2d import *

# ---state event check

def entering_time_out(e):
    return e[0] == 'ENTERING_TIME_OUT'

def swing_time_out(e):
    return e[0] == 'SWING_TIME_OUT'

def left_click(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].key == SDL_BUTTON_LEFT
    # return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def right_click(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].key == SDL_BUTTON_RIGHT
    # return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_click_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONUP and e[1].key == SDL_BUTTON_RIGHT

def mouse_motion(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEMOTION

# ---state event check


class Entering:
    @staticmethod
    def enter(hitter, e):
        print("Entering enter")
        hitter.wait_time = get_time()
        pass

    @staticmethod
    def exit(hitter, e):
        print("Entering exit")
        pass

    @staticmethod
    def do(hitter):
        # hitter.frame = (hitter.frame + 1) % 8
        # hitter.x += hitter.dir * 5
        if get_time() - hitter.wait_time > 2:
            hitter.state_machine.handle_event(('ENTERING_TIME_OUT', 0))
        # print("Entering do")
        pass

    @staticmethod
    def draw(hitter):
        hitter.image.clip_draw(hitter.frame * 100, hitter.action * 100, 100, 100, hitter.x, hitter.y)


class Idle:
    @staticmethod
    def enter(hitter, e):
        print("idle enter")
        pass

    @staticmethod
    def exit(hitter, e):
        print("idle exit")
        pass

    @staticmethod
    def do(hitter):
        # print("idle do")
        pass

    @staticmethod
    def draw(hitter):
        pass


class Swing:
    @staticmethod
    def enter(hitter, e):
        hitter.wait_time = get_time()
        print("swing enter")
        pass

    @staticmethod
    def exit(hitter, e):
        print("swing exit")
        pass

    @staticmethod
    def do(hitter):
        if get_time() - hitter.wait_time > 1:
            hitter.state_machine.handle_event(('SWING_TIME_OUT', 0))
        pass

    @staticmethod
    def draw(hitter):
        pass


class Charging:
    @staticmethod
    def enter(hitter, e):
        print("charging enter")
        pass

    @staticmethod
    def exit(hitter, e):
        print("charging exit")
        pass

    @staticmethod
    def do(hitter):
        print("charging do")
        pass

    @staticmethod
    def draw(hitter):
        pass


class Moving:
    @staticmethod
    def enter(hitter, e):
        print("charging enter")
        pass

    @staticmethod
    def exit(hitter, e):
        print("charging exit")
        pass

    @staticmethod
    def do(hitter):
        print("charging do")
        pass

    @staticmethod
    def draw(hitter):
        pass


class StateMachine:
    def __init__(self, hitter):
        self.hitter = hitter
        self.cur_state = Entering
        self.transitions = {
            Idle: {left_click: Swing, right_click: Charging},
            Entering: {entering_time_out: Idle},
            Swing: {swing_time_out: Idle},
            Charging: {left_click: Swing, right_click_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.hitter, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.hitter)

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
        self.x, self.y = 400, 100
        self.frame = 0
        self.action = 3  # ?
        self.image = load_image('Hitter.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.item = None

    def swing(self):
        pass

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        # self.state_machine.draw()
        pass
