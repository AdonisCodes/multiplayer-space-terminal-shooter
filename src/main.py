import curses
from dataclasses import dataclass


@dataclass
class Video():
    height: int
    width: int
    screen: curses.window

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = curses.initscr()

    def get_size(self):
        return self.height, self.width

    def draw(self, x, y, pixel):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        if x > self.width or y > self.height:
            return
        self.screen.addch(y, x, pixel)

    def clear(self):
        self.screen.clear()

    def refresh(self):
        self.screen.refresh()



video = Video(20, 20)
video.draw(0, 0, "X")
video.refresh()
