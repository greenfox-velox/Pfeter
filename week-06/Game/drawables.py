from tkinter import *
from random import randint

class RollStats(object):
    def roll_stats(self, hp_base = 0, hpc = 1, dp_base = 0, dpc = 1, sp_base = 0, spc = 1, level = 1):
        self.hp = hp_base + self.dice_6.roll(hpc) * level
        self.dp = dp_base + self.dice_6.roll(dpc) * level / 2
        self.sp = sp_base + self.dice_6.roll(spc) * level

class Dice(object):
    def roll(self, number_of_rolls):
        if number_of_rolls <= 1:
            return randint(1,6)
        else:
            return randint(1,6) + self.roll(number_of_rolls - 1)

class StatPrint(object):
    def stat_print(self, canvas, which_row, map_size):
        canvas.create_text(map_size[0] * 72 / 2, map_size[1] * 72 + which_row * 20, text = self.stat())

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
        self.image = PhotoImage(file='wall.png')

class FloorTile(Drawable):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        self.accessible = True
        self.image = PhotoImage(file='floor.png')
