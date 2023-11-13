from pico2d import *

# ---state event check

# ---state event check

def handle_events(self, e):
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 1280 - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


# class StateMachine:
#     def __init__(self, bat):
#         self.hitter = bat
#         self.cur_state = Entering
#         self.transitions = {
#         }
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
#         self.cur_state.draw(self.hitter)


class Bat:
    def __init__(self):
        self.x, self.y = -100, 250
        self.image = load_image('Bat.png')
        # self.state_machine = StateMachine(self)
        # self.state_machine.start()

    def update(self):
        # self.state_machine.update()
        pass

    def handle_event(self, event):
        global mx, my
        # self.state_machine.handle_event(('INPUT', event))
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                mx, my = event.x, 1280 - 1 - event.y
                self.set_cursor_image(mx, my)
        print(mx, my)
        pass

    def draw(self):
        # self.state_machine.draw()
        pass