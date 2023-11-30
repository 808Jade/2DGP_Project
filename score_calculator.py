from pico2d import load_font


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

        self.font = load_font('BMDOHYEON_ttf.ttf', 50)

    def culculating(self):
        self.result = ((self.max - abs(self.ball_x - self.hit_x)) + (self.max - abs(self.ball_y - self.hit_y))
                       + (2 * (56 - abs(56 - self.ball_size))))
        self.result = round(self.result)
        # print(f"{abs(self.ball_x - self.hit_x)} // {abs(self.ball_y - self.hit_y)} // {10 * abs(56 - self.ball_size)}")

    def handle_total_score(self):
        if self.result > self.top_score:
            self.top_score = self.result
        self.hit_count += 1
        self.total_score += self.result

    def draw(self):
        self.font.draw(100, 100, "안녕하세요 !")

    def show_score(self):
        pass