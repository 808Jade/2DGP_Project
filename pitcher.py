from pico2d import *

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
        print("Entering enter")
        pitcher.wait_time = get_time()
        pass

    @staticmethod
    def exit(pitcher, e):
        print("Entering exit")
        pass

    @staticmethod
    def do(pitcher):
        pitcher.frame = (pitcher.frame + 1) % 6
        pitcher.dir = 0.1
        pitcher.x += pitcher.dir * 100
        pitcher.action = 3
        if get_time() - pitcher.wait_time > 2:
            pitcher.state_machine.handle_event(('ENTERING_TIME_OUT', 0))
        # print("Entering do")
        pass

    @staticmethod
    def draw(pitcher):
        pitcher.image.clip_draw(pitcher.frame * 170, pitcher.action * 170, 170, 170, pitcher.x, pitcher.y, 500, 500)


class Idle:
    @staticmethod
    def enter(pitcher, e):
        print("idle enter")
        pass

    @staticmethod
    def exit(pitcher, e):
        print("idle exit")
        pass

    @staticmethod
    def do(pitcher):
        pitcher.frame = (pitcher.frame + 1) % 3
        pitcher.action = 6
        # print("idle do")
        pass

    @staticmethod
    def draw(pitcher):
        pitcher.image.clip_draw(pitcher.frame * 170, pitcher.action * 170, 170, 170, pitcher.x, pitcher.y, 500, 500)
        pass


class Pitching:
    @staticmethod
    def enter(pitcher, e):
        pitcher.wait_time = get_time()

    @staticmethod
    def exit(hitter, e):
        pass

    @staticmethod
    def do(pitcher):
        pass

    @staticmethod
    def draw(pitcher):
        pitcher.image.clip_draw()


class StateMachine:
    def __init__(self, pitcher):
        self.pitcher = pitcher
        self.cur_state = Entering
        self.transitions = {
            Idle: {idle_time_out : Pitching},
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
        self.x, self.y = 400, 100
        self.frame = 0
        self.action = 3
        self.image = load_image('Pitcher.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
