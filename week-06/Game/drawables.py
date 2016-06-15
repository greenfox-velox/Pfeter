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


class Character(StatPrint):
    def __init__(self):
        self.dice_6 = Dice()

    def stat(self):
        return (self.name + ' (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.full_hp) + ' | DP: ' + str(self.dp) +' | SP: ' + str(self.sp))

    def strike(self, enemy):
        sv = self.sp + self.dice_6.roll(2)
        if sv > enemy.dp:
            enemy.hp -= sv - enemy.dp

class Hero(Drawable, Character):
    def __init__(self, x, y):
        Drawable.__init__(self, x, y)
        Character.__init__(self)
        self.image = PhotoImage(file='hero-down.png')
        self.name = 'Hero'
        self.level = 1
        RollStats.roll_stats(self, hp_base = 20, hpc = 3, dpc = 2, sp_base = 5)
        self.full_hp = self.hp

    def move(self, direction):
        if direction == 'down':
            self.image = PhotoImage(file='hero-down.png')
            self.y += 1
        if direction == 'up':
            self.image = PhotoImage(file='hero-up.png')
            self.y -= 1
        if direction == 'left':
            self.image = PhotoImage(file='hero-left.png')
            self.x -= 1
        if direction == 'right':
            self.image = PhotoImage(file='hero-right.png')
            self.x += 1

class Skeleton(Drawable, Character):
    def __init__(self, x, y, has_the_key, level = 1):
        Drawable.__init__(self, x, y)
        Character.__init__(self)
        self.image = PhotoImage(file='skeleton.png')
        self.has_the_key = has_the_key
        self.name = 'Skeleton'
        self.level = level
        RollStats.roll_stats(self, hpc = 2, dpc = 1/2, level = self.level)
        self.full_hp = self.hp

class Boss(Drawable, Character):
    def __init__(self, x, y, level = 1):
        Drawable.__init__(self, x, y)
        Character.__init__(self)
        self.image = PhotoImage(file='boss.png')
        self.name = 'Boss'
        self.level = level
        RollStats.roll_stats(self, hp_base = self.dice_6.roll(1), hpc = 2, dp_base = self.dice_6.roll(1)/2, dpc = self.level/2, sp_base = self.level, spc = self.level, level = self.level)
        self.full_hp = self.hp
