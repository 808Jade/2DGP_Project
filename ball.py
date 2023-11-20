from pico2d import *
import game_world
import play_mode_easy
from hitter import Hitter
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector


# random으로 1~5 숫자 중에 하나를 생성한다.
# 이에 따라서 구성된 변화구 움직임을 출력한다.
# 변화구 : 타이밍, 위치, 움직임
# 타이밍 : 공 사이즈 56 전후!
# 위치 : 공 사이즈 56일 때의 공의 x, y 좌표
# hit이 발생하는 바로 그 순간의 좌표를 저장해야함. << 결국 이 방법밖에 없는데..

class Ball:
    image = None

    def __init__(self, x=440, y=380):
        self.x, self.y = x, y
        self.size = 10
        self.wait_time = 0.0

        self.strike_sign = Strikesign()
        self.strike_sign_on = False
        self.strike_sign_on_count = 0

        self.hit_sign_on = False
        self.ball_sign = Ballsign()

        self.build_behavior_tree()

        if Ball.image is None:
            Ball.image = load_image('Ball.png')

    def update(self):
        if self.hit_sign_on == False:
            self.size += 2
            self.x += 1
            self.y -= 10

        if self.size > 64:
            print(self.x, self.y, self.size)
            print("remove")
            if self.strike_sign_on:
                print(self.strike_sign_on)
                game_world.remove_object(self.strike_sign)
                self.strike_sign_on = False

            game_world.remove_object(self)

        self.bt.run()

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)
    # ------------------------------------------------------------------------------------
    def is_ball_reach(self):
        if self.size > 60:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_ball_reach_for_hit(self):
        if self.size > 50:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_ball_in_strike_zone(self):
        if 250 < self.x < 635 and 220 < self.y < 300:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_hitter_doesnt_swing(self):
        if play_mode_easy.hitter.swing_x == 0:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def print_ball_sign(self):
        print("BALL !")
        pass

    def is_ball_out_strike_zone(self):
        if 250 < self.x < 635 and 220 < self.y < 300:
            return BehaviorTree.FAIL
        else:
            return BehaviorTree.SUCCESS

    def is_hitter_doesnt_hit_ball(self):
        if self.x - 30 < play_mode_easy.hitter.swing_x < self.x + 30:
            return BehaviorTree.FAIL
        else:
            return BehaviorTree.SUCCESS

    def print_strike_sign(self):
        if not self.strike_sign_on:
            self.strike_sign_on_count += 1
            if self.strike_sign_on_count == 2:
                game_world.add_object(self.strike_sign, 3)
                self.strike_sign_on_count = 0
                self.strike_sign_on = True
        print("STRIKE!")
        pass

    def is_hitter_hit_ball(self):
        #and 50 < self.size < 60
        if self.x - 30 < play_mode_easy.hitter.swing_x < self.x + 30:
            self.hit_sign_on = True
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def print_hit_sign(self):
        # 코드 추가
        swing_x = play_mode_easy.hitter.swing_mem_x
        swing_y = play_mode_easy.hitter.swing_mem_y
        print(swing_x, swing_y)
        # if self.x - 10 < swing_x < self.x +10 and self.y -10 < swing_y < self.y + 10:
            # self.y += 50
        if swing_x < self.x:
            self.x += 10
            self.y += 50
            return BehaviorTree.SUCCESS
        elif swing_x > self.x:
            self.x -= 10
            self.y += 50
            return BehaviorTree.SUCCESS

        self.size -= 12
        if self.size < 20:
            game_world.remove_object(self)
        print("HIT!")
        return BehaviorTree.RUNNING
    # -----------------------------------------------------------------------------------------
    def build_behavior_tree(self):
        c1 = Condition('공이 도착했는가?(size>60)', self.is_ball_reach)
        c2 = Condition('공이 Strike Zone 밖에 있는가?', self.is_ball_in_strike_zone)
        c3 = Condition('타자가 Swing하지 않았는가?', self.is_hitter_doesnt_swing)
        a1 = Action('Print Ball sign', self.print_ball_sign)
        SEQ_ball = Sequence('Ball', c1, c2, c3, a1)

        c4 = Condition('공이 Strike Zone 안에 있는가?', self.is_ball_out_strike_zone)
        c5 = Condition('타자가 공을 못 맞췄는가?', self.is_hitter_doesnt_hit_ball)
        a2 = Action('Print Strike sign', self.print_strike_sign)
        SEQ_strike = Sequence('Strike', c1, c4, a2)

        c6 = Condition('타자가 공을 맞췄는가?', self.is_hitter_hit_ball)
        a3 = Action('Print Hit sign', self.print_hit_sign)
        SEQ_hit = Sequence('Hit', c6, a3)

        root = SEL_ball_or_strike_or_hit = Selector('볼/스트라이크/타격', SEQ_ball, SEQ_hit, SEQ_strike)

        self.bt = BehaviorTree(root)


class Ballsign:
    def __init__(self):
        self.image = load_image('BALL_sign.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 428, 70, 70)


class Strikesign:
    def __init__(self):
        self.image = load_image('STRIKE.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(650, 600, 190, 100)
