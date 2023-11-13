from pico2d import *

# ---state event check

# ---state event check

# def handle_events(self, e):
#     global running
#     global x, y
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_MOUSEMOTION:
#             x, y = event.x, 1280 - 1 - event.y
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             running = False
#     pass
#
#
# class Playing:
#     @staticmethod
#     def enter(bat, e):
#         print("Playing")
#         pass
#
#     @staticmethod
#     def exit(bat, e):
#         print("Exit")
#         pass
#
#     @staticmethod
#     def do(bat):
#         global mx, my
#         events = get_events()
#         for event in events:
#             if event.type == SDL_MOUSEMOTION:
#                 mx, my = event.x, 700 - event.y
#                 print(mx, my)
#         pass
#
#     @staticmethod
#     def draw(bat):
#         pass
#
#
#
# class StateMachine:
#     def __init__(self, bat):
#         self.bat = bat
#         self.cur_state = Playing
#         # self.transitions
#
#     def start(self):
#         self.cur_state.enter(self.bat, ('NONE', 0))
#
#     def update(self):
#         self.cur_state.do(self.bat)
#
#     def handle_event(self, e):
#         for check_event, next_state in self.transitions[self.cur_state].items():
#             if check_event(e):
#                 self.cur_state.exit(self.bat, e)
#                 self.cur_state = next_state
#                 self.cur_state.enter(self.bat, e)
#                 return True
#         return False
#
#     def draw(self):
#         self.cur_state.draw(self.bat)


class Bat:
    def __init__(self, mx = 0, my = 0):
        self.x, self.y = 0, 0
        self.mx, self.my = 0, 0
        self.image = load_image('Bat.png')

    def update(self):
        # update 로직 추가 필요
        pass

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.mx, self.my = event.x, 700 - event.y
            print(self.mx, self.my)
        pass

    def draw(self):
        self.image.draw(self.mx, self.my, 80, 30)
        print("2")
