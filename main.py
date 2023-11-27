from pico2d import *
import game_framework

import logo_mode
import title_mode
import play_mode_easy  as start_mode

open_canvas(1280, 720)
game_framework.run(start_mode)
close_canvas()

# 개발 일정
# 1주차 : 리소스 스집
# 2주차 : 초기 화면 구성
# 3주차 : 타자 움직임 구현
# 4주차 : 투수, 공에 대한 구현
# 5주차 : 타격 구현
# 6주차 : 난이도 구현
# 7추자 : 타격 기록 구현
# 8주차 : 최종 점검