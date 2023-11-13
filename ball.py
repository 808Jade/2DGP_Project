from pico2d import *
import game_world

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

# random으로 1~5 숫자 중에 하나를 생성한다.
# 이에 따라서 구성된 변화구 움직임을 출력한다.
# 변화구 : 타이밍, 위치, 움직임


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
    def enter(ball, e):
        print("idle enter")
        pass

    @staticmethod
    def exit(ball, e):
        print("idle exit")
        pass

    @staticmethod
    def do(ball):
        # ball.x, ball.y 위치 만지기
        # print("idle do")
        pass

    @staticmethod
    def draw(ball):
        ball.image.draw(ball.x, ball.y, 50, 50)
        pass


class StateMachine:
    def __init__(self, ball):
        self.ball = ball
        self.cur_state = Entering
        self.transitions = {
        }

    def start(self):
        self.cur_state.enter(self.ball, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.ball)
        pico2d.delay(0.05)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.ball, e)
                self.cur_state = next_state
                self.cur_state.enter(self.ball, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.ball)


class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('ball.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()


class Curve:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('ball.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()


class Fast:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('ball.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()


class Slider:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('ball.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()


class Snake:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('ball.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()