from pico2d import *


class ScoreCalculator:
    def __init__(self):
        self.previous_mode = 'NULL'
        # self.charging = 0

        # 타격 마다 점수 산출 #
        self.hit_x = 0.0
        self.hit_y = 0.0
        self.ball_x = 0.0
        self.ball_y = 0.0
        self.ball_size = 0.0
        self.max = 100.0
        self.result = 0.0
        # 종합 점수 기록
        self.top_score = 0
        self.hit_count = 0
        self.score_list = []
        self.total_score = 0
        self.rank = 'F'
        self.rank_rgb = [0,0,0]

        self.font = load_font('BMDOHYEON_ttf.ttf', 100)
        self.font_num = load_font('Lobster.ttf', 100)
        self.font_rank = load_font('28DaysLater.ttf', 600)

        self.S_bgm = load_music('rank_S.mp3')
        self.A_bgm = load_music('rank_A.mp3')
        self.B_bgm = load_music('rank_B.mp3')
        self.C_bgm = load_music('rank_C.mp3')
        self.DE_bgm = load_music('rank_DE.mp3')
        self.F_bgm = load_music('rank_f.mp3')

        self.S_bgm.set_volume(20)
        self.A_bgm.set_volume(20)
        self.B_bgm.set_volume(20)
        self.C_bgm.set_volume(20)
        self.DE_bgm.set_volume(20)
        self.F_bgm.set_volume(20)

    def culculating(self):
        self.result = ((self.max - abs(self.ball_x - self.hit_x)) + (self.max - abs(self.ball_y - self.hit_y))
                       + (2 * (56 - abs(56 - self.ball_size))))
        self.result = round(self.result)

    def handle_total_score(self):
        if self.result > self.top_score:
            self.top_score = self.result
        self.hit_count += 1
        self.total_score += self.result

        if self.hit_count <= 1:
            self.rank = 'F'
            self.rank_rgb = [0,0,0]
        elif 2 >= self.hit_count > 1:
            self.rank = 'E'
            self.rank_rgb = [51,51,0]
        elif 3 >= self.hit_count > 2:
            self.rank = 'D'
            self.rank_rgb = [102,102,153]
        elif 5 >= self.hit_count > 3:
            self.rank = 'C'
            self.rank_rgb = [0,153,0]
        elif 7 >= self.hit_count > 5:
            self.rank = 'B'
            self.rank_rgb = [0,0,250]
        elif 10 >= self.hit_count > 7:
            self.rank = 'A'
            self.rank_rgb = [205,0,0]
        elif self.hit_count > 10:
            self.rank = 'S'
            self.rank_rgb = [255,204,0]

    def draw(self):
        self.font_num.draw(590, 570, f'TOP : {self.top_score}',(255, 255, 255))
        self.font_num.draw(590, 420, f'HIT : {self.hit_count} times',(255, 255, 255))
        self.font_num.draw(590, 270, f'TOTAL : {self.total_score}',(255, 255, 255))

        self.font_rank.draw(140,420, f'{self.rank}',(self.rank_rgb))

    def update(self):
        pass