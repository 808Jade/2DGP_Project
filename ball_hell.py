import random

from pico2d import *

import game_world
import play_mode_hell
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
from sign import Strikesign, Ballsign, Scoresign


# ========================================================================= #
# =============================== HELL MODE =============================== #
# ========================================================================= #

# 송구 정책 #
# 위치가 정해지지 않은 변화구 투구
# 공 속력 약 1.5 배

# 타격 정책 #
# Ball.size 가 62 일 때, Strike / Ball 판정
# Ball.size 가 48 이상 부터, 타격 가능
# Ball.x / Ball.y 의 +- 20, 타격 가능


class Ball_HELL:
    image = None

    def __init__(self, x=440, y=380):
        self.x, self.y = x, y
        self.size = 10
        self.wait_time = 0.0
        self.angle = 0

        self.hit_sign = False
        self.hit_pos = 0

        self.build_behavior_tree()

        self.swinged = False

        # 공 객체가 생성될 때마다, 던져질 좌표, 구질 결정
        self.strike_or_ball = random.choice([True, False])  # True == strike / False == Ball
        if self.strike_or_ball:
            self.arrive_x, self.arrive_y = random.randint(545, 725), random.randint(110, 325)
        else:
            self.arrive_x, self.arrive_y = random.randint(500, 800), random.randint(150, 400)

        self.start_point_x = 609
        self.start_point_y = 435

        self.mode = random.choice(['Straight', 'Curve', 'Slider', 'Knuckle'])

        self.Straight_size = 4
        self.Curve_size = 3
        self.Slider_size = 3
        self.Knuckle_size = 2.5

        self.hit_sound = load_wav('Hit_sound.wav')
        self.strike_sound = load_wav('referee-whistle.wav')
        self.meat_sound = load_wav('strike_and_ball.wav')

        if self.mode == 'Straight':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Straight_size) + 2.5
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Straight_size)
        elif self.mode == 'Curve':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Curve_size) + 2.5
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Curve_size)
        elif self.mode == 'Slider':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Slider_size) + 2.5
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Slider_size)
        elif self.mode == 'Knuckle':
            self.move_x = (self.start_point_x - self.arrive_x) // (50 // self.Knuckle_size) + 2.5
            self.move_y = (self.start_point_y - self.arrive_y) // (50 // self.Knuckle_size)

        if Ball_HELL.image is None:
            Ball_HELL.image = load_image('Ball.png')

    def update(self):
        if self.mode == 'Straight':
            self.size += self.Straight_size
            self.x += self.move_x
            self.y -= self.move_y
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

        if self.hit_sign:
            self.size -= 7
            self.x -= self.hit_pos * 3
            self.y += 1.5 * self.size
            if self.size < 10:
                game_world.remove_object(self)

        if self.size > 62:
            game_world.remove_object(self)

        self.angle += 10

        self.bt.run()

    def draw(self):
        self.image.rotate_draw(math.radians(self.angle), self.x, self.y, self.size, self.size)

# ----------------------------------------Behavior-Tree----------------------------------------
    def is_ball_reach(self):
        if self.size > 62:
            self.meat_sound.set_volume(50)
            self.meat_sound.play(1)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_ball_reach_for_hit(self):
        if self.size > 48:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_ball_in_strike_zone(self):
        if 545 < self.x < 725 and 110 < self.y < 325:  # (545, 110, 725, 325)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_swing(self):
        if play_mode_hell.hitter.swing_x != 0:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_swinged(self):
        if play_mode_hell.hitter.swing_x != 0:
            self.swinged = True
        if self.swinged == True:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_nice_swing_pos(self):
        if self.x - 20 < play_mode_hell.hitter.swing_mem_x < self.x + 20 \
                and self.y - 20 < play_mode_hell.hitter.swing_mem_y < self.y + 20:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def print_ball_sign(self):
        ball_sign = Ballsign()
        game_world.add_object(ball_sign, 2)
        ball_sign.sign_on()
        return BehaviorTree.SUCCESS

    def print_strike_sign(self):
        strike_sign = Strikesign()
        game_world.add_object(strike_sign, 2)
        strike_sign.sign_on()
        play_mode_hell.strike_counter.count += 1
        self.strike_sound.set_volume(50)
        self.strike_sound.play(1)
        return BehaviorTree.SUCCESS

    def hit_action(self):  # 공을 때린 X 좌표의 위치에 따라 날아가는 방향 결정
        swing_x = play_mode_hell.hitter.swing_mem_x
        swing_y = play_mode_hell.hitter.swing_mem_y

        import title_mode
        title_mode.score_calculator.ball_x = self.x
        title_mode.score_calculator.ball_y = self.y
        title_mode.score_calculator.hit_x = swing_x
        title_mode.score_calculator.hit_y = swing_y
        title_mode.score_calculator.ball_size = self.size
        title_mode.score_calculator.culculating()
        title_mode.score_calculator.handle_total_score()
        print(title_mode.score_calculator.result)
        print(title_mode.score_calculator.total_score)

        score_sign = Scoresign()
        score_sign.score = title_mode.score_calculator.result
        game_world.add_object(score_sign, 2)
        score_sign.sign_on()

        self.hit_sound.set_volume(50)
        self.hit_sound.play(1)

        self.hit_sign = True
        self.hit_pos = swing_x - self.x
        return BehaviorTree.SUCCESS

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

        c6 = Condition('스윙 하였었는가?', self.is_swinged)
        SEQ_strike_s = Sequence('Strike', c6, c4, a2)

        a3 = Action('Print Ball sign', self.print_ball_sign)
        SEQ_ball = Sequence('Ball', c4, a3)

        SEQ_Fly = Sequence('Flying')

        root = SEL_ball_or_strike_or_hit = Selector('볼/스트라이크/타격', SEQ_hit, SEQ_strike, SEQ_strike_s, SEQ_ball, SEQ_Fly)

        self.bt = BehaviorTree(root)
# ----------------------------------------Behavior-Tree----------------------------------------
