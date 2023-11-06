from pico2d import *

# ---state event check

def time_out(e):
    return e[0] == 'TIME_OUT'

def left_click(e):
    return e[0] == 'INPUT' and e[1].type == SDL_MOUSEBUTTONDOWN and e[1].key == SDL_BUTTON_LEFT

# ---state event check

class Entering:
    @staticmethod
    def enter(hitter, e):
        pass

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(hitter):
        hitter.frame = (hitter.frame + 1) % 8
        hitter.x += hitter.dir * 5
        pass

    @staticmethod
    def draw(hitter):
        hitter.image.clip_draw(hitter.frame * 100, hitter.action * 100, 100, 100, hitter.x, hitter.y)


class Idle:
    @staticmethod
    def enter(hitter, e):
        pass

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(hitter):
        pass

    @staticmethod
    def draw(hitter):
        pass


class Swing:
    @staticmethod
    def enter(hitter,e):
        pass

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(hitter):
        pass

    @staticmethod
    def draw(hitter):
        pass


class StateMachine:
    def __init__(self, hitter):
        self.hitter = hitter
        self.cur_state = Entering
        self.transitions = {
            Idle: {left_click: Swing},
            Entering: {time_out: Idle},
            Swing: {}
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

    def swing(self):
        pass

    def update(self):
        pass

    def handle_event(self, e):
        pass

    def draw(self):
        pass
