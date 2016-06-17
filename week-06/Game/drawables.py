from tkinter import *

class Drawable(object):
    def __init__(self, x, y):
            self.x = x
            self.y = y

    def draw(self, canvas):
        canvas.create_image(self.x * 72, self.y * 72, image = self.image, anchor = NW)

class WallTile(Drawable):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        self.accessible = False
        self.image = PhotoImage(file='images/wall.png')

class FloorTile(Drawable):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        self.accessible = True
        self.image = PhotoImage(file='images/floor.png')
