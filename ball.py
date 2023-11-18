from pico2d import *
import game_world
from hitter import Hitter
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector

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
# 타이밍 : 공 사이즈 56 전후!
# 위치 : 공 사이즈 56일 때의 공의 x, y 좌표
def Culculater(size):
    if size < 50 or size > 60:
        pass # hit !


class Ball:
    image = None

    def __init__(self, x=440, y=380):
        self.x, self.y = x, y
        self.size = 10

        if Ball.image is None:
            Ball.image = load_image('Ball.png')

    def update(self):
        # if
        self.size += 2
        self.x += 1
        self.y -= 10
        # print(f"TEST{abs(self.hitter.swing_x - self.x)}, {abs(self.hitter.swing_y - self.y)}")
        #
        # # hitter 객체가 None이 아니고, hitter 객체에 'swing_x'와 'swing_y' 속성이 있다면 실행
        # if self.hitter and hasattr(self.hitter, 'swing_x') and hasattr(self.hitter, 'swing_y'):
        #     if abs(self.hitter.swing_x - self.x) < 50 and abs(self.hitter.swing_y - self.y) < 50:
        #         print(f"HIT! {abs(self.hitter.swing_x - self.x)}")
        #     else:
        #         print(f"{abs(self.hitter.swing_x)}")

        if self.size > 80:
            print(self.x, self.y, self.size)
            print("remove")
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

    def build_behavior_tree(self):
        c1 = Condition('공이 도착했는가?(size>60)', self.is_ball_reach)
        c2 = Condition('공이 Strike Zone 밖에 있는가?', self.is_ball_in_strike_zone)
        c3 = Condition('타자가 Swing하지 않았는가?', self.is_hitter_doesnt_swing)
        a1 = Action('Print Ball sign', self.print_ball_sign)
        SEQ_ball = Sequence('Ball', c1, c2, c3, a1)

        c4 = Condition('공이 Strike Zone 안에 있는가?', self.is_ball_out_strike_zone)
        c5 = Condition('타자가 공을 못맞췄는가?', self.is_hitter_doesnt_hit_ball)
        a2 = Action('Print Strike sign', self.print_strike_sign)
        SEQ_strike = Sequence('Strike', c1, c5, c4)

        c6 = Condition('타자가 공을 맞췄는가?', self.is_hitter_hit_ball)
        a3 = Action('Print Hit sign', self.print_hit_sign)
        SEQ_hit = Sequence('Hit', c6, a3)

        root = SEL_ball_or_strike_or_hit = Selector('볼 스트라이크 타격', SEQ_ball, SEQ_strike, SEQ_hit)

        self.bt = BehaviorTree(root)


class Curve:
    image = None

    def __init__(self, x=440, y=380):
        self.x, self.y = x, y
        self.size = 10

        self.hitter = hitter  # hitter 객체 저장
        if Curve.image is None:
            Curve.image = load_image('Ball.png')

    def update(self):
        self.size += 2
        self.x += 1
        self.y -= 10
        if abs(self.hitter.swing_x - self.x) < 50 and abs(self.hitter.swing_y - self.y) < 50:
            print(f"HIT! {abs(self.hitter.swing_x - self.x)}")
        else:
            print(f"{abs(self.hitter.swing_x)}")

        if self.size > 80:
            print(self.x, self.y, self.size)
            print("remove")
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)


class Fast:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class Slider:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class Snake:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if Ball.image == None:
            Ball.image = load_image('Ball.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)




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

