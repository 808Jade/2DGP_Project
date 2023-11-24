from pico2d import *

import random
import game_framework
import game_world
import play_mode_easy
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector

# 변화구 : 타이밍, 위치, 움직임
# 타이밍 : 공 사이즈 56 전후!
# 위치 : 공 사이즈 56일 때의 공의 x, y 좌표


class Ball:
    image = None

    def __init__(self, x=440, y=380):
        self.x, self.y = x, y
        self.size = 10
        self.wait_time = 0.0

        self.strike_sign = Strikesign()
        self.strike_sign_on = False
        self.strike_sign_on_count = 0

        self.hit_sign = False
        self.hit_pos = 0

        self.ball_sign = Ballsign()

        self.build_behavior_tree()

        # 공 객체가 생성될 때마다, 던져질 좌표, 구질 생성 !
        self.strike_or_ball = random.choice([True, False])  # True == strike / False == Ball
        if self.strike_or_ball:
            self.arrive_x, self.arrive_y = random.randint(545, 725), random.randint(110, 325)
        else:
            self.arrive_x, self.arrive_y = random.randint(500, 800), random.randint(150, 400)
        print(self.arrive_x, self.arrive_y)
        self.start_point_x = 609
        self.start_point_y = 435

        self.mode = random.choice(['Straight', 'Curve', 'Slider', 'Knuckle'])

        self.Straight_size = 2.8
        self.Curve_size = 2
        self.Slider_size = 2
        self.Knuckle_size = 1.5

        # Straight 직구
        if self.mode == 'Straight':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Straight_size)
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Straight_size)
        elif self.mode == 'Curve':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Curve_size)
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Curve_size)
        elif self.mode == 'Slider':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Slider_size)
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Slider_size)
        elif self.mode == 'Knuckle':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Knuckle_size)
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Knuckle_size)
        print(self.move_x, self.move_y)

        if Ball.image is None:
            Ball.image = load_image('Ball.png')

    def update(self):
        if self.mode == 'Straight':
            self.size += self.Straight_size
            self.x += self.move_x # 0
            self.y -= self.move_y # self.size * 0.4
        elif self.mode == 'Curve':
            self.size += self.Curve_size
            self.x -= self.move_x
            self.y -= self.move_y
            if self.size > 20:
                self.size += 1
                self.x += self.move_x + 3
                self.y -= 4
        elif self.mode == 'Slider':
            self.size += self.Slider_size
            self.x += self.move_x
            self.y -= self.move_y
            if self.size > 30:
                self.x += 8
                self.y -= 0
        elif self.mode == 'Knuckle':
            self.size += self.Knuckle_size
            self.x += self.move_x
            self.y -= self.move_y
            if self.size > 20:
                self.x += self.size * 0.2
                if self.size > 36:
                    self.x -= self.size * 0.2


        if self.size > 64:
            # print(self.x, self.y, self.size)
            print("remove")

            game_world.remove_object(self)

        if self.strike_sign_on:
            if get_time() - self.wait_time > 0.5:
                # print(self.strike_sign_on)
                game_world.remove_object(self.strike_sign)
                self.strike_sign_on = False

        if self.hit_sign:
            self.size -= 7
            self.x -= self.hit_pos * 3
            self.y += 1.5 * self.size
            if self.size < 10:
                game_world.remove_object(self)

        self.bt.run()

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)
        draw_rectangle(self.x - 20, self.y - 20, self.x+20,self.y+20)

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
        if 545 < self.x < 725 and 110 < self.y < 325:  # (545, 110, 725, 325)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_swing(self):
        if play_mode_easy.hitter.swing_x != 0:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_nice_swing_pos(self):
        if self.x - 30 < play_mode_easy.hitter.swing_mem_x < self.x + 30 \
                and self.y - 30 < play_mode_easy.hitter.swing_mem_y < self.y + 30:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def print_ball_sign(self):
        print("BALL !")
        pass

    def print_strike_sign(self):
        # if not self.strike_sign_on:
        #     self.strike_sign_on_count += 1
        #     if self.strike_sign_on_count == 2:
        #         game_world.add_object(self.strike_sign, 3)
        #         self.strike_sign_on_count = 0
        #         self.strike_sign_on = True
        self.strike_sign.sign_on()
        print("STRIKE!")
        return BehaviorTree.SUCCESS

    def hit_action(self):
        swing_x = play_mode_easy.hitter.swing_mem_x
        swing_y = play_mode_easy.hitter.swing_mem_y

        self.hit_sign = True
        self.hit_pos = swing_x - self.x
        return BehaviorTree.SUCCESS
    # -----------------------------------------------------------------------------------------

    def build_behavior_tree(self):
        c1 = Condition('스윙 하였는가?', self.is_swing)
        c2 = Condition('스윙 타이밍이 유효한가?', self.is_ball_reach_for_hit)
        c3 = Condition('스윙 위치가 유효한가?', self.is_nice_swing_pos)
        a1 = Action('Print Hit sign', self.hit_action)
        SEQ_hit = Sequence('Hit', c1, c2, c3, a1)

        c4 = Condition('공이 도착했는가?(size>60)', self.is_ball_reach)
        c5 = Condition('공이 Strike Zone 안에 있는가?', self.is_ball_in_strike_zone)
        a2 = Action('Print Strike sign', self.print_strike_sign)
        SEQ_strike = Sequence('Strike', c4, c5, a2)

        a3 = Action('Print Ball sign', self.print_ball_sign)
        SEQ_ball = Sequence('Ball', c4, a3)

        SEQ_Fly = Sequence('Flying')

        root = SEL_ball_or_strike_or_hit = Selector('볼/스트라이크/타격', SEQ_hit, SEQ_strike, SEQ_ball, SEQ_Fly)

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
        self.wait_time = 0.0
        self.duration = 1.0  # Set the duration for the sign to be visible

    def sign_on(self):
        self.wait_time = get_time()
        print("SIGNON!!!")

    def update(self):
        elapsed_time = get_time() - self.wait_time
        if 0 <= elapsed_time <= self.duration:
            self.image.draw(650, 600, 190, 100)
            print("UPDATE!!!")

    def draw(self):
        pass